from django.urls import path
from . import views

urlpatterns = [
    path('', views.precios_list, name='precios_list')
]