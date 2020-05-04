from django.db import models

# Create your models here.


class Ingredient(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Hamburger(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.BigIntegerField(default=0)
    descripcion = models.TextField()
    imagen = models.TextField()
    ingredientes = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.nombre
