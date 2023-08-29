from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.response import Response

from order.models import Order, OrderItem
from order import views
from .repository import get_product, get_user_auth, login_user
from datetime import datetime

class OrderAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(views.OrderCreate.name)
        self.product_id = 2
        self.token =  login_user(email='user@gmail.com', password='ndh*8987979878').json()['access']

        self.orderItems = {
            'token': self.token,
            "orderItems": [
                {
                    'product_id': 2,
                    'product_name': 'pera',
                    'image': 'data.image',
                    'price': 2,
                    'qty': 38,
                },
                {
                    'product_id': 3,
                    'product_name': 'maca',
                    'image': 'data.image',
                    'price': 2,
                    'qty': 8,
                }

            ]
        }

    def test_get_product(self):
        """Ensure we can retrieve a product"""
        response = get_product(product_id=self.product_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Alto Falante')

    def test_get_product_no_exists(self):
        """Ensure we can verify if product don't exit with a no exist id"""
        response = get_product(product_id=1)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_and_get_order(self):
        """Ensure we can create and retrieve a order"""

        response = self.client.post(
            self.url, self.orderItems, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_get_order(self):
        """Ensure we can get a order with item details"""

        response = self.client.post(self.url, self.orderItems, format='json')

        print('My token: ', self.token)

        url = reverse(views.OrderDetail.name,  None, {response.data['id'], self.token})

        print('URL: ', url)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)

    def test_user_get_orders(self):
        """Ensure we can get a order with item details"""

        response = self.client.post(self.url, self.orderItems, format='json')

        url = reverse(views.UserOrders.name,  None,  {self.token})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)

    def test_user_get_orders_with_invalid_token(self):
        """Ensure we can get a order with item details"""

        response = self.client.post(self.url, self.orderItems, format='json')

        url = reverse(views.UserOrders.name,  None,
                      {'odsihfuieugryifuvshdfgyu'})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_order(self):
        """Ensure we can update order"""

        response = self.client.post(
            self.url, self.orderItems, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        url = reverse(views.OrderDetail.name,  None, { response.data['id'], self.token})
        data = {
            'user': 2,
            'paidAt': datetime.now(),
            'isPaid': True,
            'isDelivered': True,
            'deliveredAt': datetime.now(),
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_partial_update_order(self):
        """Ensure we can update order"""

        response = self.client.post(
            self.url, self.orderItems, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

        url = reverse(views.OrderDetail.name,  None, { response.data['id'], self.token})
        data = {
            'paidAt': datetime.now(),
            'isPaid': True,
        }
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        """Ensure we can delete order"""

        response = self.client.post(self.url, self.orderItems, format='json')

        url = reverse(views.OrderDetail.name,  None, {
                      response.data['id'], self.token})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_login(self):
        """Ensure we can login with credentias"""

        response = get_user_auth(token=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'user@gmail.com')

    def test_login_with_no_credentials_exist(self):
        """Ensure we can login with credentias"""

        response = get_user_auth(token='odaofshfiugr87euyr')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
