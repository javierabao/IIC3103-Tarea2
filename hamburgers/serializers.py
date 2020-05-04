# rest
from rest_framework import serializers

# models
from .models import Hamburger, Ingredient


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'nombre', 'descripcion')


class HamburgerSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Hamburger
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes')
