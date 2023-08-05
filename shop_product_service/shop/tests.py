from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from shop.models import Category
from shop import views



class CategotyAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(views.CategoryList.name)
        
    def _create_test_image(self):
        image = Image.new('RGB', (100, 100))
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)
        return SimpleUploadedFile('test.png', image_file.read(), content_type='image/png')

    def post_category(self, name, image):
        data = {'name': name, 'image': image}
        response = self.client.post(self.url, data, format='multipart')
        return response
    
    def test_post_and_get_category_product(self):
        new_category_name = 'Water'
        new_category_image = self._create_test_image()
        response = self.post_category(new_category_name, new_category_image)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get()
        self.assertEqual(category.name, new_category_name)
        # check if url image has expected
        self.assertTrue(category.image.url.startswith('/media/'))
        category.image.delete()

