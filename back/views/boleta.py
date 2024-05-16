from transbank.webpay.webpay_plus.transaction import Transaction
import uuid
import requests

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
        
        buy_order = self.generate_buy_order()
        boleta = Boleta.objects.get(id=response.data['id'])
        boleta.buy_order = buy_order
        boleta.save()

        transaccion = (Transaction()).create(
            buy_order=buy_order, 
            session_id=self.generate_buy_order(), 
            amount=response.data['valor_total'], 
            return_url='http://localhost:8000/api/boleta/commit/'
        )
        response = requests.post(transaccion['url'], { 'token_ws': transaccion['token'] })
        if response.status_code == 200:
            html = response.text
            return Response(html, content_type='text/html')

        return Response(404)
    
    @action(detail=False, methods=['GET'])
    def commit(self, request):
        token = request.query_params.get('token_ws')
        resultado = (Transaction()).commit(token=token)
        boleta = Boleta.objects.get(buy_order=resultado['buy_order'])
        boleta.pagado = True if resultado['status'] == 'AUTHORIZED' else False
        boleta.save()
        
        if boleta.pagado:
            return redirect('http://localhost:4200/pago_confirmado/')
        
        return redirect('http://localhost:4200/pago_rechazado/')