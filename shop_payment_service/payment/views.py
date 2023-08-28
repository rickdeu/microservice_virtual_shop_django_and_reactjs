# import apps
from datetime import datetime
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from shop_payment_service import settings
import base64
import requests
from rest_framework import status

from payment.paypalauth import paypalToken
from payment import repository


class PaymentOrderCreate(APIView):
    name = 'payment-service'

    def post(self, request, pk, token, format=None):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {paypalToken()}',
        }
        order = repository.get_order(pk=pk, token=token)
        if order.status_code == 200:
            response = requests.post(
                'https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, json=request.data)
            if response.status_code == 201:
                repository.get_order(pk=pk, token=token, data={
                    'paidAt': datetime.now(),
                    'isPaid': True,
                })
                return Response(response.json())
        return Response({'errors': response.json()['name'], 'status': response.status_code})
