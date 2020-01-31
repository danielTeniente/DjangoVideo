from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Tabla de productos
class Producto(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# Tabla de sanwiches
class Sandwiches(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    producto = models.ManyToManyField(Producto)

    class Meta:
        ordering = ['nombre']

    def get_productos(self):
        return "\n".join([p.nombre for p in self.producto.all()])

    def __str__(self):
        return self.nombre

# Tabla de sanwiches con precios
class Precios(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sandwich = models.ForeignKey(Sandwiches, on_delete=models.CASCADE) 
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null = True)
    ganancia = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null = True)
    FechaIngresado = models.DateField(auto_now_add=True)

    def calculate(self):
        total = 0
        imp = 1/2 #porcentaje asigando por la empresa
        productos = self.sandwich.producto.all()
        for producto in productos:
            costo = producto.costo
            total += costo
        totalFloat = float(total)
        ganaciaP = totalFloat * imp  
        self.ganancia = ganaciaP
        self.precio = totalFloat + ganaciaP
        self.save()
        return ":"

    def __str__(self):
        return self.sandwich.nombre