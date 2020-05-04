from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Hamburger(models.Model):
    name = models.CharField(max_length=100)
    price = models.BigIntegerField(default=0)
    description = models.TextField()
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
