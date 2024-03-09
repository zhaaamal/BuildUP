from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        field = '__all__'


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = '__all__'
