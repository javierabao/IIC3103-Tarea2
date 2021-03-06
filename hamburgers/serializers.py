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


class IngredientPathSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedIdentityField(view_name='ingredient-detail')

    class Meta:
        model = Ingredient
        fields = ('path',)


class HamburgerListSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = IngredientPathSerializer(many=True, read_only=True)

    class Meta:
        model = Hamburger
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes')
