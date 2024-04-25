from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from back.models import Boleta

class BoletaSerializer(ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


class BoletaViewSet(ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

