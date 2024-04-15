from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Order, OrderItem
from product.models import Products
from django.db import transaction
from .serializers import OrderSerializer,UpdateOrderSerializer,GetOrderSerializer
from rest_framework.exceptions import ValidationError


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            items_data = data.pop('items', [])
            if not items_data:
                raise ValidationError("Orders must have at least one item.")

            total_amount = 0

            with transaction.atomic():
                order = Order.objects.create(user=user, **data)
                for item_data in items_data:
                    product = item_data.get('product')
                    quantity = item_data.get('quantity')
                    unit_price = product.price

                    if quantity <= 0:
                        raise ValidationError("Invalid item data: quantity and unit price must be positive")

                    total_amount += quantity * unit_price

                    OrderItem.objects.create(order=order,**item_data)
                order.total_amount = total_amount
                order.save()
            return Response(f"Order  has been successfully placed. Thank you for your purchase.",
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrderView(APIView):
    serializer_class = UpdateOrderSerializer

    def post(self,request,id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            print(data)
            try:
                order = Order.objects.get(id=id)
                Order.objects.filter(id=id).update(**data)
                if data['status']:
                    order_status = data['status']
                    if order_status in dict(Order.STATUS_CHOICES):
                        order.status = order_status
                        order.save()
                    else:
                        return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)
            except Order.DoesNotExist:
                return Response(f"order doe snot exist!",status=status.HTTP_404_NOT_FOUND)
        return Response('hello world',status=status.HTTP_200_OK)

class OrdersView(APIView):
    serializer_class = GetOrderSerializer

    def get(self,request):
        orders = Order.objects.all()
        serializer = self.serializer_class(orders, many=True)
        data =  serializer.data
        return Response(data)
    
class OrdersByIdView(APIView):
    serializer_class = GetOrderSerializer

    def get(self,request,id):
        orders = Order.objects.filter(id=id).first()
        serializer = self.serializer_class(orders)
        data =  serializer.data
        return Response(data)
    
class DeleteOrder(APIView):
    def delete(self,request,id):
        delete = Order.objects.filter(id=id).delete()
        return Response(f"Order {id} removed.")
    
class OrdersByUser(APIView):
    serializer_class = GetOrderSerializer

    def get(self,request):
        user = request.user
        orders = Order.objects.filter(user=user).first()
        serializer = self.serializer_class(orders)
        data =  serializer.data
        return Response(data)
