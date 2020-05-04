from django.contrib import admin
from .models import Hamburger, Ingredient
# Register your models here.

admin.site.register(Hamburger)
admin.site.register(Ingredient)
