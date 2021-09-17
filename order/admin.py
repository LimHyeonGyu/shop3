from django.contrib import admin
from order.models import Order, OrderItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'order_date', 'order_status' ]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

