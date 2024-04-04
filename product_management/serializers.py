from rest_framework import serializers
from .models import Products,Category

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Products
        fields = ('name','images','Category','description')
        extra_kwargs={
            'name':{'required':False},
            'images':{'required':False},
            'Category':{'required':False},
            'description':{'required':False},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'