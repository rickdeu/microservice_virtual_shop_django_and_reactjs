from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

from shop.models import Category, Product, ProductImage
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

    def test_post_with_same_name_category_product(self):
        new_category_name = 'Water'
        new_category_image = self._create_test_image()

        response = self.post_category(new_category_name, new_category_image)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.post_category(new_category_name, new_category_image)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_category_by_name(self):
        """
        Ensure we can filter category by name
        """
        new_category_name = 'Water'
        new_category_image = self._create_test_image()
        self.post_category(new_category_name, new_category_image)
        filter_by_name = {'name': new_category_name}
        url = f'{reverse(views.CategoryList.name)}?{urlencode(filter_by_name)}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], new_category_name)

    def test_filter_category_by_id(self):
        """
        Ensure we can filter category by id
        """
        new_category_name = 'Water'
        new_category_image = self._create_test_image()

        self.post_category(new_category_name, new_category_image)
        filter_by_id = {'pk': Category.objects.get().pk}

        url = f'{reverse(views.CategoryList.name)}?{urlencode(filter_by_id)}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], new_category_name)

    def test_get_category_collections(self):
        """
        Ensure we can retrieve the category collections
        """
        new_category_name = 'Water'
        new_category_image = self._create_test_image()
        self.post_category(new_category_name, new_category_image)
        url = reverse(views.CategoryList.name)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], new_category_name)

    def test_update_category(self):
        """
        Ensure we can retrieve the category collections
        """
        new_category_name = 'Water'
        new_category_image = self._create_test_image()

        # create category
        reponse = self.post_category(new_category_name, new_category_image)
        url = reverse(views.CategoryDetail.name, None, {reponse.data['pk']})
        self.assertEqual(reponse.status_code, status.HTTP_201_CREATED)
        self.assertEqual(reponse.data['name'], new_category_name)

        # update category
        new_category_name = 'Category updated'
        data = {'name': new_category_name}
        reponse = self.client.patch(url, data, format='json')
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertEqual(reponse.data['name'], new_category_name)

    def test_get_category(self):
        """
        Ensure we can get a single category by id
        """
        new_category_name = 'Water'
        new_category_image = self._create_test_image()

        # create category
        response = self.post_category(new_category_name, new_category_image)
        url = reverse(views.CategoryDetail.name, None, {response.data['pk']})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get category after create
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_category_name)


class ProductAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_category = reverse(views.CategoryList.name)
        self.url_product = reverse(views.ProductList.name)

    def _create_test_image(self):
        image = Image.new('RGB', (100, 100))
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)
        return SimpleUploadedFile('test.png', image_file.read(), content_type='image/png')


    def test_post_and_get_product(self):
        """
        Ensure we can create and get product with foreign key category
        """

        # test category
        new_category_image = self._create_test_image()
        data = {'name': 'Water', 'image': new_category_image}
        response = self.client.post(
            self.url_category, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get()
        
        self.assertEqual(category.name, data['name'])

        # check if url image has expected
        self.assertTrue(category.image.url.startswith('/media/'))
        category.image.delete()

        # test product
        data = {
            'category': category, 'name': 'name',
            'image': self._create_test_image(), 'description': 'description',
            'price': 199, 'is_available': True
        }
        response = self.client.post(self.url_product, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get()

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, data['name'])

class ProductImageAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url_category = reverse(views.CategoryList.name)
        self.url_product = reverse(views.ProductList.name)
        self.url_productimage = reverse(views.ProductImageList.name)


    def _create_test_image(self):
        image = Image.new('RGB', (100, 100))
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)
        return SimpleUploadedFile('test.png', image_file.read(), content_type='image/png')
  
    def test_post_and_get_product_image(self):
        # test category
        data = {'name': 'Water', 'image': self._create_test_image()}
        response = self.client.post(
            self.url_category, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get()
        
        self.assertEqual(category.name, data['name'])

        # check if url image has expected
        self.assertTrue(category.image.url.startswith('/media/'))
        category.image.delete()

        # test product
        data1 = {
            'category': category, 'name': 'name',
            'image': self._create_test_image(), 'description': 'description',
            'price': 199, 'is_available': True
        }
        response1 = self.client.post(self.url_product, data1, format='multipart')

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        product = Product.objects.get()

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, data1['name'])
         # check if url image has expected
        self.assertTrue(product.image.url.startswith('/media/'))
        #product.image.delete()


        # test product image
        data2 = {
            'product': product, 'label': 'label',
            'image': self._create_test_image(), 'description': 'description',
        }
        response2 = self.client.post(self.url_productimage, data2, format='multipart')
        print(f'response: {response2.data}')


        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductImage.objects.count(), 1)

        
        product_image = ProductImage.objects.get()

        # check if url image has expected
        self.assertTrue(product.image.url.startswith('/media/'))
        product.image.delete()


        self.assertEqual(product_image.label, data2['label'])
        # check if url image has expected
        self.assertTrue(product_image.image.url.startswith('/media/'))
        product_image.image.delete()