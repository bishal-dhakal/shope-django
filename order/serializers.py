from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = Order
        fields = ("address", "phone", "items")
        depth = 1

class GetOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = '__all__'


class UpdateOrderSerializer(serializers.Serializer):
    address = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    paid = serializers.BooleanField(required=False)
    status = serializers.CharField(required=False)
