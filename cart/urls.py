from django.urls import path
from cart import views
from django.contrib.auth import views as auth_views
from cart.views import *

app_name = 'cart'
urlpatterns = [
    path('', CartListView.as_view(), name='list'),
    path('remove/<int:pk>/', CartDeleteView.as_view(), name='remove'),
]