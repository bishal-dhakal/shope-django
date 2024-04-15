from django.db import models
from product.models import Products
from user.models import CustomUser
from datetime import datetime

# Create your models here.
class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED,'ordered'),
        (SHIPPED,'shipped')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0) 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.today) 
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=ORDERED) 

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    # def __str__(self) -> str:
    #     return self.product
