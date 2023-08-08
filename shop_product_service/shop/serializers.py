from rest_framework import serializers

# imprts local apps
from shop.models import Category, Product
from shop import views

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )
    class Meta:
        model = Category
        fields = ('url','pk','name', 'image',  'products')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )
    product_images = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-images-detail'
    )
    class Meta:
        model = Product
        fields = ('url','pk','name','price','category', 'image', 'description', 'is_available', 'product_images')

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Product
        fields = ('url','pk','product','label', 'image', 'description')