from rest_framework import serializers

from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'get_image', 'get_thumbnail', 'price', 'get_absolute_url', 'description'
        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'get_absolute_url', 'products'
        ]