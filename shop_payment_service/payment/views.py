# import apps
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from shop_payment_service import settings
import base64
import requests

class PayPalPaymentServiceAPI(APIView):
    name = 'paypal-service'

    def paypalToken(self, client_secret=settings.SECRET_KEY_PAYPAL, client_id=settings.CLIENT_ID):
        url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {0}".format(base64.b64encode((client_id + ":" + client_secret).encode()).decode())
        }
        response = requests.post(url, data, headers=headers)
        return response.json()['access_token']

    def post(self, request, format=None):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.paypalToken()}', 
            }

        response = requests.post(
            'https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, json=request.data)
        if response.status_code == 201:
            return Response(response.json())
        return Response({'errors': response.json()['name'], 'status': response.status_code})
    def get(self, request, pk, format=None):
        headers = {
            'Authorization': f'Bearer {self.paypalToken()}', 
        }
        response = requests.get(f'https://api-m.sandbox.paypal.com/v2/checkout/orders/{pk}', headers=headers)
        return Response(response.json())


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'payments': reverse(PayPalPaymentServiceAPI.name, request=request),


            }
        )
