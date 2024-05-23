from transbank.webpay.webpay_plus.transaction import Transaction
import uuid
import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer, ModelSerializer, CharField, IntegerField, SerializerMethodField
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.exceptions import ValidationError
from django.shortcuts import redirect
from django.conf import settings

from back.models import Boleta, Pedido, Producto


class EliminarPedidoSerializer(Serializer):
    pedido_id = IntegerField(min_value=1)

    def validate_pedido_id(self, pedido_id):
        pedido = Pedido.objects.filter(pk=pedido_id)
        if not pedido:
            raise ValidationError('Pedido no existe')
        
        return pedido_id


class AgregarProductoSerializer(Serializer):
    producto_id = IntegerField(min_value=1)
    cantidad = IntegerField(min_value=1)

    def validate_producto_id(self, producto_id):
        producto = Producto.objects.filter(pk=producto_id)
        if not producto:
            raise ValidationError('Producto no existe')
        
        return producto_id


class ProductoCarritoSerializer(ModelSerializer):
    nombre_producto = CharField(read_only=True, source='producto.nombre')
    valor_unitario = CharField(read_only=True, source='producto.valor')
    imagen_producto = SerializerMethodField()
    
    class Meta:
        model = Pedido
        fields = ['id', 'producto', 'nombre_producto', 'valor_unitario', 'cantidad', 'valor_total', 'imagen_producto']

    def get_imagen_producto(self, obj: Pedido):
        if obj.producto.imagen:
            return f'http://localhost:8000{obj.producto.imagen.url}'
        
        return None


class BoletaSerializer(ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


class CarritoSerializer(ModelSerializer):
    pedidos = ProductoCarritoSerializer(many=True)

    class Meta:
        model = Boleta
        fields = ['id', 'valor_total', 'pedidos']


class BoletaViewSet(ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    
    def generate_buy_order(self):
        return str(uuid.uuid4().int)[:10]
    
    def create(self, request, *args, **kwargs):
        return Response(status=404)
    
    def update(self, request, *args, **kwargs):
        return Response(status=404)
    
    def partial_update(self, request, *args, **kwargs):
        return Response(status=404)
    
    @action(detail=False, methods=['GET'])
    def get_carrito(self, request):
        usuario = self.request.user

        carrito_query = Boleta.objects.filter(usuario=usuario, es_carrito=True)
        if not carrito_query:
            carrito = Boleta.objects.create(
                valor_total=0,
                usuario=usuario,
                direccion_entrega='',
            )
        else:
            carrito = carrito_query.first()

        serializer = CarritoSerializer(carrito)
        return Response(serializer.data, status=HTTP_200_OK)
    
    @action(detail=True, methods=['POST'])
    def agregar_editar_producto(self, request, pk):
        carrito = self.get_object() 

        serializer = AgregarProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Pedido.objects.update_or_create(
            defaults={
                'cantidad': serializer.data['cantidad'],
                'valor_total': Producto.objects.get(pk=serializer.data['producto_id']).valor * serializer.data['cantidad']
            },
            boleta_id=pk,
            producto_id=serializer.data['producto_id'],
        )

        valor_total = 0
        for pedido in carrito.pedidos.all():
            valor_total += pedido.valor_total

        carrito.valor_total = valor_total
        carrito.save()
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data, status=HTTP_200_OK)
    
    @action(detail=False, methods=['PUT'])
    def eliminar_pedido(self, request):
        serializer = EliminarPedidoSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        
        Pedido.objects.filter(id=serializer.validated_data['pedido_id']).delete()

        return Response(status=HTTP_204_NO_CONTENT)

            
    @action(detail=True, methods=['GET'])
    def pagar(self, request, pk):
        boleta: Boleta = self.get_object()
        
        buy_order = self.generate_buy_order()
        boleta.buy_order = buy_order
        boleta.save()

        transaccion = (Transaction()).create(
            buy_order=boleta.buy_order, 
            session_id=boleta.buy_order, 
            amount=boleta.valor_total, 
            return_url='http://localhost:8000/api/boleta/commit/'
        )
        response = requests.post(transaccion['url'], { 'token_ws': transaccion['token'] })
        if response.status_code == 200:
            html = response.text
            return Response(html, content_type='text/html')

        return Response(404)
    
    @swagger_auto_schema(
        operation_description="Confirmar una transacción y actualizar el estado del pago",
        manual_parameters=[
            openapi.Parameter('token_ws', openapi.IN_QUERY, description="Token transaccion", type=openapi.TYPE_STRING)
        ],
        responses={302: "Redirigir a la página de confirmación o rechazo de pago"}
    )
    @action(detail=False, methods=['GET'])
    def commit(self, request):
        token = request.query_params.get('token_ws')
        resultado = (Transaction()).commit(token=token)
        boleta = Boleta.objects.get(buy_order=resultado['buy_order'])
        boleta.pagado = True if resultado['status'] == 'AUTHORIZED' else False
        boleta.es_carrito = False
        boleta.save()
        
        if boleta.pagado:
            return redirect('http://localhost:4200/pago_confirmado/')
        
        return redirect('http://localhost:4200/pago_rechazado/')