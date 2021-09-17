from django.urls import path
from order import views
from django.contrib.auth import views as auth_views
from order.views import *

app_name = 'order'
urlpatterns = [
    path('', OrderFormView.as_view(), name='orderview'),
    path('list', OrderListView.as_view(), name='list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='detail'),
]