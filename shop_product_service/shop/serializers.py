from rest_framework import serializers

# imprts local apps
from shop.models import Category, Product, ProductImage
from shop import views

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url','pk','name', 'image',  'products')



class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('url','pk','product','label', 'image', 'description')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('url','pk','name','price','category', 'image', 'description', 'is_available', 'product_images')


