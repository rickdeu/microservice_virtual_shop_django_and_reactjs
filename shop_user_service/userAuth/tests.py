from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


class CategotyAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_register = reverse('rest_register')
        self.url_login = reverse('rest_login')
        self.url_logout = reverse('rest_logout')

        self.user = {
            'username': 'rickdeu',
            'email': 'andre@gmail.com',
            'password1': 'Andh*8987979878',
            'password2': 'Andh*8987979878',
        }

    def _create_test_image(self):
        image = Image.new('RGB', (100, 100))
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)
        return SimpleUploadedFile('test.png', image_file.read(), content_type='image/png')

    def test_post_and_get_registration(self):
        """Ensure we can create and retrieve a user"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_login(self):
        """Ensure we can create a login"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        credentials = {
            #'username': 'rickdeu',
            'email': 'andre@gmail.com',
            'password': 'Andh*8987979878',
        }

        response = self.client.post(self.url_login, credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_logout(self):
        """Ensure we can logout"""
        response = self.client.post(
            self.url_register, self.user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.url_logout, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
