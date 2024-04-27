from .producto import ProductoViewSet
from .tienda import TiendaViewSet
from .boleta import BoletaViewSet
from .categoria import CategoriaViewSet
from .pedido import PedidoViewSet
from .usuario import UserViewSet


__all__ = [
    'ProductoViewSet',
    'TiendaViewSet',
    'BoletaViewSet',
    'CategoriaViewSet',
    'PedidoViewSet',
    'UserViewSet'
]