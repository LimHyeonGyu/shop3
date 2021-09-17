from django.urls import path
from product import views
from product.views import *

app_name = 'product'
urlpatterns = [
    path('', ProdListView.as_view(), name='list'),
    path('<int:pk>/', ProdDetailView.as_view(), name='detail'),
    path('like/',views.like, name='like'),
    #path('<int:product_id>', views.detail, name='detail'),
]