from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

from .repository import get_product



@api_view(['POST'])
def orderCreate(request):
    data = request.data

    if not data:
        return Response({'detail': 'No Order items'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderItemSerializer(data=data, many=True)

    if serializer.is_valid():
        order = Order.objects.create(user=1)
        for i in serializer.validated_data:
            product = get_product(i['product_id']).json()
            OrderItem.objects.create(
                product_id=product['pk'],
                product_name=product['name'],
                order=order,
                qty=i['qty'],
                price=product['price'],
                image=product['image']
            )
        serializer = OrderSerializer(order)
        return Response({'status': 'sucess', 'data': serializer.data})
    return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
