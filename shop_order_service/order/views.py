from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Order, OrderItem
from .serializers import OrderSerializer


def get_product(product_id):
    product_url = f'http://127.0.0.1:8000/api/product-detail/{product_id}'
    response = requests.get(product_url)
    if response.status_code == 200:
        return response  # .json()
    return Response({'detail': 'No products'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def orderCreate(request):
    data = request.data
    orderItems = data
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(user=1)
        for i in orderItems:

            product = get_product(i['product'])
            item = OrderItem.objects.create(
                product_id=product.json()['pk'],
                product_name=product.json()['name'],
                order=order,
                qty=i['qty'],
                price=product.json()['price'],
                image=product.json()['image']
            )

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
