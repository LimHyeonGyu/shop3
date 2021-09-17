from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from product.models import Product
from cart.models import Cart
from .forms import AddProForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
try:
    from django.utils import simplejson as json

except ImportError:
    import json


class ProdListView(ListView):
    model = Product
    template_name = 'product/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProdListView, self).get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context

    def get_queryset(self, *args, **kwargs):
        product_qs = super(ProdListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('search')

        if query :
            product_qs = self.model.objects.filter(Q(pro_name__contains=query))
        return product_qs


class ProdDetailView(LoginRequiredMixin, DetailView):
    login_url = '/member/login'
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = AddProForm()
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        form_amount = AddProForm(request.POST)
        if form_amount.is_valid():
            cd = form_amount.cleaned_data
            try:
                cart = Cart.objects.get(Q(product_id=product.id) & Q(author=request.user))
            except (KeyError, Cart.DoesNotExist):
                qry = Cart(product_id=product.id, author=request.user, amount=cd['amount'], price=product.pro_price)
                qry.save()
            else:
                cart.price = product.pro_price
                cart.amount += cd['amount']
                cart.save()

            return HttpResponseRedirect(reverse('cart:list'))


def like(request):
    if request.method == 'POST':
        product_id = request.POST['pk']
        product = Product.objects.get(pk = product_id)
        product.pro_like +=1
        product.save()
        message = 'You liked this'

    context = {'likes_count' : product.pro_like, 'message' : message}

    return HttpResponse(json.dumps(context), content_type='application/json')
