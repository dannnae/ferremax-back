from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.permissions import AllowAny
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
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.query_params.get('categoria', None)
        if categoria is not None:
            queryset = queryset.filter(categoria_id=categoria)
        return queryset
