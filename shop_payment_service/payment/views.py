# import apps
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from payment.autentication import paypalToken
from payment import repository


class PaymentOrderCreate(APIView):
    name = 'payment-service'
    def post(self, request, pk, token, format=None):
        order = repository.get_order(pk=pk, token=token)
        if order.status_code == 200:
            response = repository.paypal_payment(request=request)
            if response.status_code == 201:
                repository.get_order(pk=pk, token=token, data={
                    'paidAt': datetime.now(),
                    'isPaid': True,
                })
                return Response(response.json())
        return Response({'errors': response.json()['name'], 'status': response.status_code})
