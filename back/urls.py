from rest_framework.routers import DefaultRouter

from back.views import ProductoViewSet, TiendaViewSet, BoletaViewSet, CategoriaViewSet, PedidoViewSet

router = DefaultRouter()

router.register(r'producto', ProductoViewSet, basename='Producto')
router.register(r'tienda', TiendaViewSet, basename='Tienda')
router.register(r'boleta', BoletaViewSet, basename='Boleta')
router.register(r'categoria', CategoriaViewSet, basename='Categoria')
router.register(r'pedido', PedidoViewSet, basename='Pedido')