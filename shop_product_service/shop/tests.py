from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from shop.models import Category
from shop import views

class CategoryTest(APITestCase):
    def post_category(self, name, image):
        url = reverse(views.CategoryList.name)
        data = {'name': name, 'image': image}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_category_product(self):
        """
        Ensure we can create a new Category and then get it
        """
        new_category_name = 'Water'
        new_category_image = ''
        response = self.post_category(new_category_name, new_category_image)
        print('PK {0}'.format(Category.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.count() == 1
        assert Category.objects.get().name == new_category_name
