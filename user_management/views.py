from django.http import JsonResponse
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class= RegisterSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse('hello',safe=False)
    
class LoginView(generics.CreateAPIView):
    serializer_class= LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            print(f'{serializer.errors}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        return Response({'token': '10'})
