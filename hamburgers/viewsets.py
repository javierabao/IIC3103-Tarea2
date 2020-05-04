from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.http import Http404

from .serializers import HamburgerSerializer, IngredientSerializer
from .models import Hamburger, Ingredient


class HamburgerViewSet(viewsets.ModelViewSet):
    queryset = Hamburger.objects.all().order_by('name')
    serializer_class = HamburgerSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            hamburgers = instance.hamburger_set.all()
            if not hamburgers:
                self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class IntermediateDetail(APIView):

    def put(self, request, pk, pk2, format=None):
        hamburger = Hamburger.objects.get(pk=pk)
        ingredient = Ingredient.objects.get(pk=pk2)
        if ingredient not in hamburger.ingredients.all():
            hamburger.ingredients.add(ingredient)
            serializer = HamburgerSerializer('json', hamburger)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, pk2, format=None):
        hamburger = Hamburger.objects.get(pk=pk)
        ingredient = Ingredient.objects.get(pk=pk2)
        print(hamburger)
        print(ingredient)
        if ingredient in hamburger.ingredients.all():
            hamburger.ingredients.remove(ingredient)
            serializer = HamburgerSerializer('json', hamburger)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hamburgers': reverse('hamburger-list', request=request, format=format),
        'ingredients': reverse('ingredient-list', request=request, format=format)
    })
