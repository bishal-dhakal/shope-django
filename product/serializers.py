from rest_framework import serializers
from .models import Products,Category

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        depth = 1

class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Products
        fields = ('name','images','category','description')
        extra_kwargs={
            'name':{'required':False},
            'images':{'required':False},
            'category':{'required':False},
            'description':{'required':False},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'