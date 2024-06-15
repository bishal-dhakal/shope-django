from django.db import models
from product.models import Products
from user.models import CustomUser

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} * {self.product.name}'