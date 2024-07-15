from rest_framework import serializers
from rest_framework.permissions import BasePermission, IsAuthenticated
from back.models import Factura
from rest_framework.viewsets import ModelViewSet

class AdminPermission(BasePermission):

    def has_permission(self, request, view):  
        if request.user.is_authenticated and request.user.type == 'ADMIN':
            return True
        return False

class FacturaSerializer(serializers.ModelSerializer):
    pedidos = serializers.SerializerMethodField()
    iva = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()
    valor_total = serializers.CharField(read_only=True, source='boleta.valor_total')
    
    class Meta:
        model = Factura
        fields = '__all__'

    def get_pedidos(self, factura):
        return [{
            'codigo': pedido.producto.codigo,
            'nombre': pedido.producto.nombre,
            'cantidad': pedido.cantidad,
            'valor': pedido.producto.valor,
            'valor_total': pedido.valor_total,
        } for pedido in factura.boleta.pedidos.all()]
    
    def get_iva(self, factura):
        return factura.boleta.valor_total * 0.19
    
    def get_subtotal(self, factura):
        return factura.boleta.valor_total * 0.81

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.prefetch_related('boleta__pedidos__producto').all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, AdminPermission]

