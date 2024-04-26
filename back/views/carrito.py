from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from back.models import Producto, Pedido
from .pedido import PedidoSerializer

class CarritoView(APIView):
    def post(self, request):
        # Obtener datos del producto a agregar al carrito desde la solicitud
        producto_id = request.data.get("producto_id")
        cantidad = request.data.get("cantidad")
        usuario = request.user  # Obtener usuario autenticado
        
        # Verificar si el producto existe y está en stock
        producto = Producto.objects.get(pk=producto_id)
        if producto.stock < cantidad:
            return Response({"error": "Producto fuera de stock"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Crear un nuevo pedido en el carrito
        Pedido.objects.create(
            producto=producto,
            cantidad=cantidad,
            valor_total=producto.valor * cantidad,
            usuario=usuario,
            en_carrito=True
        )
        return Response({"message": "Producto agregado al carrito"}, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        # Obtener el ID del pedido a eliminar del carrito desde la solicitud
        pedido_id = request.data.get("pedido_id")
        
        # Verificar si el pedido existe y está en el carrito
        try:
            pedido = Pedido.objects.get(pk=pedido_id, usuario=request.user, en_carrito=True)
        except Pedido.DoesNotExist:
            return Response({"error": "Pedido no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # Eliminar el pedido del carrito
        pedido.delete()
        return Response({"message": "Pedido eliminado del carrito"}, status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request):
        # Obtener todos los pedidos en el carrito del usuario actual
        pedidos = Pedido.objects.filter(usuario=request.user, en_carrito=True)
        # Serializar los pedidos para enviarlos como respuesta
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
