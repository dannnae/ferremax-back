from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from back.models import Tienda

class TiendaSerializer(ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'
        

class TiendaViewSet(ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer