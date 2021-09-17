from django.db import models
from django.utils import timezone
from django.urls import reverse
from product.models import Product
from django.contrib.auth.models import User
import os


class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField('가격')
    amount = models.IntegerField('수량')
    cartdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
    
    def get_sum(self):
        return self.price * self.amount

