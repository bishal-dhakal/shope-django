from django.http import JsonResponse
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import traceback
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from django.db import transaction

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class= RegisterSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            user = CustomUser.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                phonenumber =serializer.validated_data['phonenumber']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()

            #do something if not done or completed execute code in if sent block
            sent = None
            if sent:
                user.delete()
                return Response({"message": "failed to create user"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "User created successfully."})
    
class CustomTokenPairView(TokenObtainPairView):
    serializer_class= CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = request.user
            print(user)
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token, verify=True)
            token.blacklist()
            user.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(traceback.format_exc())
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t,_ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)