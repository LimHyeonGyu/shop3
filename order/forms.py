from django import forms

from .models import Order

class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_name', 'order_tel', 'order_addr']
