from django.db import models

# Create your models here.
class Project(models.Model):
    precio = models.PositiveIntegerField(default=0)
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    códigodeproducto = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
