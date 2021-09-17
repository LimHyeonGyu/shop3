from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from product.models import Product
from cart.models import Cart
from product.forms import AddProForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# 장바구니 목록
class CartListView(LoginRequiredMixin, ListView):
    login_url = '/member/login'
    template_name = 'cart/detail.html'

    def get_queryset(self):
        return Cart.objects.filter(author=self.request.user)

# 장바구니 삭제
class CartDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/member/login'
    model = Cart
    success_url = reverse_lazy('cart:list')

