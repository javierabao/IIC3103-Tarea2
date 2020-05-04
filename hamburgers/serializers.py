# rest
from rest_framework import serializers

# models
from .models import Hamburger, Ingredient


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description')


class HamburgerSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Hamburger
        fields = ('id', 'name', 'price', 'description', 'image', 'ingredients')
