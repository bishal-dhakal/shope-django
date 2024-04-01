from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value


    class Meta:
        model = CustomUser
        fields=('username','password','password2','email','phonenumber')
        extra_kwargs ={
            'phonenumber':{'required':True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            phonenumber=validated_data['phonenumber']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255,read_only=True)
    password = serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','password']

    def validate(self,data):
        email = data.get('email',None)
        password = data.get('password',None)

        if email is None:
            raise serializers.ValidationError('Email is required.')
        
        if password is None:
            raise serializers.ValidationError('password is required.')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('This user is not currently activated.')

        return user
