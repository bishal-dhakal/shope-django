from django.shortcuts import render
from rest_framework.views import APIView
from .models import Products,Category
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .serializers import ProductsSerializer,UpdateProductSerializer,CategorySerializer

# Create your views here.
class CreateProductView(APIView):
    serializer_class = ProductsSerializer

    def post(self,request):
        category_name = request.data.pop('category_name', None)
        
        if category_name:
            try:
                category = Category.objects.get(name=category_name)
                request.data['category'] = category.id
            except Category.DoesNotExist:
                raise ValidationError({"category_name": "Category does not exist."})

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListVIew(APIView):
    serializer_class = ProductsSerializer

    def get(self,request):
        products = Products.get_all_products()
        serializer = self.serializer_class(products,many=True)
        all_product = serializer.data
        return Response(all_product,status=status.HTTP_200_OK)
    
class ProductByIDView(APIView):
    serializer_class = ProductsSerializer

    def get(self,request,id):
        try:
            product = Products.get_product_by_id([id]).first()
            if product:
                serializer = self.serializer_class(product)
                data = serializer.data
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response('Product not found', status=status.HTTP_404_NOT_FOUND)
        except Products.DoesNotExist:
            return Response('Product not found',status=status.HTTP_404_NOT_FOUND)
        
class UpdateProductView(APIView):
    serializer_class = UpdateProductSerializer,ProductsSerializer

    def put(self,request,id):
        try:
            product = Products.objects.get(pk=id)
        except Products.DoesNotExist:
            return Response({'error':"product not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductByID(APIView):
    def delete(self,request,id):
        product = Products.objects.filter(id=id).delete()
        return Response(f"Succesfully Deleted product {id}",status=status.HTTP_200_OK)
    

class CreateCategoryView(APIView):
    serializer_class = CategorySerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class GetCategoryByIDView(APIView):
    serializer_class = CategorySerializer

    def get(self,request,id):
        try:
            category = Category.objects.filter(id=id)
            serializer = self.serializer_class(category,many=True)
            data = serializer.data
            return Response(data,status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            return Response('Product not found',status=status.HTTP_404_NOT_FOUND)


class CategoryListView(APIView):
    serializer_class = CategorySerializer

    def get(self,request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category,many=True)
            category_list = serializer.data
            return Response(category_list,status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error':"Categories not found"},status=status.HTTP_404_NOT_FOUND)

class DeleteCategoryByID(APIView):
    def delete(self,request,id):
        category = Category.objects.filter(id=id).delete()
        return Response(f"Succesfully Deleted Category {id}",status=status.HTTP_200_OK)
    
class UpdateCategoryView(APIView):
    serializer_class = CategorySerializer

    def put(self,request,id):
        try:    
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response({'error':"Categories not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
