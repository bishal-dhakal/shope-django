from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Products
from .serializers import CartSerializer

class CreateCartItem(APIView):
    serializer_class =  CartSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllCartItem(APIView):

    def get(self,request):
        pass

class GetCartItemByID(APIView):

    def get(self,request):
        pass

class DeleteCartItemById(APIView):

    def delete(self.request):
        pass

class DeleteCart(APIView):
    
    def delete(self,request):
        pass 