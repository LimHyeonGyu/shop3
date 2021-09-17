from django.db import models
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    order_name = models.CharField('받는사람',max_length=200)
    order_tel = models.CharField('연락처', max_length=200)
    order_addr = models.CharField('주소', max_length=200)
    order_status_choice = [
        ('주문완료','주문완료'),
        ('결재완료','결재완료'),
        ('배송중','배송중'),
        ('배송완료','배송완료'),
        ('주문취소','주문취소'),
        ]
    order_status = models.CharField(max_length=20, choices=order_status_choice, default='주문완료')
    order_date = models.DateField('주문일', default=timezone.now)
    delivery = models.CharField('택배사', max_length=200, null=True, default='')
    delivery_no = models.CharField('송장번호', max_length=200, null=True, default='')
    
    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return self.order_id

    def get_total_product(self):
        return sum(item.get_item_price() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    price = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_item_price(self):
        return self.price * self.amount
