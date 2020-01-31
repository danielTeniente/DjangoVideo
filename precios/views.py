from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import redirect

from .models import Producto, Sandwiches, Precios

# Create your views here.

def precios_list(request):
    lista = Precios.objects.order_by('FechaIngresado')
    return render(request, 'precios/precios_list.html', {'precios': lista})