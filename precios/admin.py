from django.contrib import admin
from .models import Producto, Sandwiches, Precios

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Producto admin."""

    list_display = ('id', 'nombre', 'costo', 'cantidad', 'user')

@admin.register(Sandwiches)
class SandwichesAdmin(admin.ModelAdmin):
    """Sandwiches admin."""

    list_display = ('id', 'nombre', 'get_productos','user')

@admin.register(Precios)
class PreciosAdmin(admin.ModelAdmin):
    """Precios admin."""

    list_display = ('id', 'sandwich', 'precio', 'ganancia', 'user')