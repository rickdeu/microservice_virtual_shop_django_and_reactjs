from rest_framework import serializers

# imprts local apps
from shop.models import Category, Product
from shop import views

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category-detail'
    )
    class Meta:
        model = Category
        fields = ('url','pk','name', 'image', 'slug', 'products')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )
    class Meta:
        model = Product
        fields = ('url','pk','name','price','category', 'image', 'slug', 'description', 'is_available')