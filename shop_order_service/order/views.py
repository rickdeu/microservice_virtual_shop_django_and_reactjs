from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from .repository import get_product, get_user_auth


class OrderCreate(APIView):
    name = 'order-create'

    """ Create a order   """

    def post(self, request, format=None):

        user = get_user_auth(token=request.data['token'])
        if user.status_code == 200:
            #request.session['user'] = user.json()
            serializer = OrderItemSerializer(
                data=request.data['orderItems'], many=True)
            if serializer.is_valid():
                order = Order.objects.create(user=user.json()['pk'])
                [OrderItem.objects.create(
                    product_id=get_product(i['product_id']).json()['pk'],
                    product_name=get_product(i['product_id']).json()['name'],
                    order=order,
                    qty=i['qty'],
                    price=get_product(i['product_id']).json()['price'],
                    image=get_product(i['product_id']).json()['image']
                )for i in serializer.validated_data]
                serializer = OrderSerializer(order)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class OrderDetail(APIView):
    name = 'order-detail'
    """
    Retrieve, update or delete a  order.
    """
    
    

    def get_object(self, pk, token):
        try:
            user = get_user_auth(token=token)
            if user.status_code == 401:
                return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return Order.objects.get(pk=pk, user=user.json()['pk'])
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        serializer = OrderSerializer(order)

        return Response(serializer.data)

    def put(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, token, format=None):
        order = self.get_object(pk=pk, token=token)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserOrders(APIView):
    name = 'user-orders'
    def get(self, request, token, format=None):
        try:
            user = get_user_auth(token=token)
        except:
            return Response({'detail': f'No connection with '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            if user.status_code == 200:
                order = Order.objects.filter(user=user.json()['pk'])
                serializer = OrderSerializer(order, many=True)
                return Response(serializer.data)
        return Response({'error': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)






class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'orders': reverse(OrderCreate.name, request=request),

            }
        )
