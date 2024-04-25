from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from back.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
