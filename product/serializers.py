from rest_framework import serializers

from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'get_image', 'get_thumbnail', 'price', 'get_absolute_url', 'description'
        ]
        