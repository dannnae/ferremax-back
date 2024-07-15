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
    class Meta:
        model = Factura
        fields = '__all__'

class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, AdminPermission]

