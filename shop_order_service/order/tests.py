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

from datetime import datetime


class OrderAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('order_create')
        self.product_id = 2
        self.orderItems = [
            {
                'product_id': 2,
                'product_name': 'goiba',
                'image': 'data.image',
                'price': 2,
                'qty': 100,
            },
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
            },
        ]

    def test_get_product(self):
        """Ensure we can retrieve a product"""
        response = views.get_product(product_id=self.product_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Alto Falante')

    def test_get_product_no_exists(self):
        """Ensure we can verify if product don't exit with a no exist id"""
        response = views.get_product(product_id=1)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_and_get_order(self):
        """Ensure we can create and retrieve a order"""

        response = self.client.post(
            self.url, self.orderItems, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)

    def test_get_order(self):
        """Ensure we can get a order with item details"""

        response = self.client.post(self.url, self.orderItems, format='json')
        print(response.data['data']['id'])

        url = reverse( 'order_detail',  None,{response.data['data']['id']})

        response = self.client.get(url, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)


    def test_update_order(self):
        """Ensure we can update order"""

        response = self.client.post(
            self.url, self.orderItems, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)

        url = reverse( 'order_detail',  None,{response.data['data']['id']})
        data = {
            'user': 2,
            'paidAt': datetime.now(),
            'isPaid': True,
            'isDelivered': True,
            'deliveredAt':datetime.now(),
        }
        response = self.client.put(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_delete_order(self):
        """Ensure we can delete order"""

        response = self.client.post(self.url, self.orderItems, format='json')

        url = reverse( 'order_detail',  None,{response.data['data']['id']})

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


