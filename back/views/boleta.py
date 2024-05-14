from transbank.webpay.webpay_plus.transaction import Transaction
import uuid

from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect

from back.models import Boleta

class BoletaSerializer(ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


class BoletaViewSet(ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    
    def generate_buy_order(self):
        return str(uuid.uuid4().int)[:10]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        transaccion = (Transaction()).create(
            buy_order=self.generate_buy_order(), 
            session_id=self.generate_buy_order(), 
            amount=response.data['valor_total'], 
            return_url='http://localhost:8000/api/boleta/commit/'
        )

        return Response(transaccion)
    
    @action(detail=False, methods=['POST'])
    def commit(self, request):
        token = request.data.get('token_ws')
        resultado = (Transaction()).commit(token=token)

        return redirect('http://localhost:4200/pago_confirmado/')