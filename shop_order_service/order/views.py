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
        return Response({'detail': 'No Order items'}, status=status.HTTP_404_NOT_FOUND)

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


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    """
    Retrieve, update or delete a code order.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = OrderSerializer(order)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
