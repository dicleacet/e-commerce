from django.shortcuts import render
from product.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Product

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)