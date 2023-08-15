from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from order.models import Order, OrderItem
from order import views 


class OrderAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('order_create')

    def test_get_product(self):
        product_id = 2
        response = views.get_product(product_id=product_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Alto Falante')

    def test_get_product_no_exists(self):
        product_id = 1
        response = views.get_product(product_id=product_id)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_and_get_order(self):
        
        orderItems = [
            {
                'product': 2,
            'name': 'goiba',
            'image': 'data.image',
            'price': 2,
            'qty': 100,
            },
            {
                'product': 2,
            'name': 'pera',
            'image': 'data.image',
            'price': 2,
            'qty': 38,
            },
            {
                'product': 3,
            'name': 'maca',
            'image': 'data.image',
            'price': 2,
            'qty': 8,
            },
        ]
        response = self.client.post(
            self.url, orderItems, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)

