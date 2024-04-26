from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from back.models import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
