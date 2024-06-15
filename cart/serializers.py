from rest_framework import serializers
from .models import CartItem

class CartSerializer(serializers.Serializer):
    class Meta:
        model = CartItem
        fields = '__all__'