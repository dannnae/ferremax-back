from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.conf import settings

from back.models import Producto

class ProductoSerializer(ModelSerializer):
    valor_usd = SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    def get_valor_usd(self, obj: Producto):
        return round(obj.valor / settings.USD_TODAY, 1)


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
