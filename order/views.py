from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product
from django.db.models import Q
from .forms import OrderAddForm
from cart.models import Cart
from order.models import Order, OrderItem
from datetime import datetime

class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/member/login'
    template_name = 'order/list.html'

    def get_queryset(self):
        return Order.objects.filter(author=self.request.user)

class OrderDetailView(LoginRequiredMixin, DetailView):
    login_url = '/member/login'
    model = Order
    template_name = 'order/detail.html'

    #def get_queryset(self):
        #return self.queryset.filter(pk=self.kwargs['pk'])

class OrderFormView(FormView):
    form_class = OrderAddForm
    template_name = 'order/order.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        cart_list = Cart.objects.filter(author=self.request.user)
        context = super(OrderFormView, self).get_context_data(**kwargs)
        context['cart_list'] = cart_list
        context['cart_total'] = sum(item.get_sum() for item in cart_list)

        return context 

    def form_valid(self, form):
        form_order = form.cleaned_data
        cart_list = Cart.objects.filter(author=self.request.user)
        today = datetime.now()
        order_id = today.strftime('%Y%m%d%H%M%S')

        order = Order(order_id=order_id, author=self.request.user, \
                        order_name=form_order['order_name'],\
                        order_tel=form_order['order_tel'],\
                        order_addr=form_order['order_addr'],\
                        delivery='로젠택배',\
                        delivery_no=today.strftime('%Y%m%d%H%M%S')+'78')
        order.save()

        for item in cart_list:
            OrderItem(order_id=order.id, product_id=item.product_id, price=item.price, \
                        amount=item.amount).save()
            ## 상품 테이블에 있는 재고수량을 감소
            decrement_stk = Product.objects.get(pk=item.product_id)
            decrement_stk.pro_stock -= item.amount
            decrement_stk.save()

        Cart.objects.filter(author=self.request.user).delete()

        return super(OrderFormView, self).form_valid(form)