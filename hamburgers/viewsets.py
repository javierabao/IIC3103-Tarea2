from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .serializers import HamburgerSerializer, IngredientSerializer
from .models import Hamburger, Ingredient


class HamburgerViewSet(viewsets.ModelViewSet):
    queryset = Hamburger.objects.all().order_by('nombre')
    serializer_class = HamburgerSerializer


class HamburgerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        if not isinstance(pk, int):
            return 'not instance'
        try:
            return Hamburger.objects.get(pk=pk)
        except Hamburger.DoesNotExist:
            return 'not instance'

    def get(self, request, pk, format=None):
        hamburger = self.get_object(pk)
        if hamburger == 'not instance':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if hamburger == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HamburgerSerializer(hamburger)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        hamburger = self.get_object(pk)
        if hamburger == 'not instance' or hamburger == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)

        poss_variables = ['nombre', 'precio' 'descripcion', 'imagen']
        for param in request.data:
            print(param)
            if param not in poss_variables:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = HamburgerSerializer(
            hamburger,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hamburger = self.get_object(pk)
        if hamburger == 'not instance' or hamburger == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)

        hamburger.delete()
        return Response(status=status.HTTP_200_OK)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('nombre')
    serializer_class = IngredientSerializer


class IngredientDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        if not isinstance(pk, int):
            return 'not instance'
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return 'doesnt exist'

    def get(self, request, pk, format=None):
        ingredient = self.get_object(pk)

        if ingredient == 'not instance':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if ingredient == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        if ingredient == 'not instance' or ingredient == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)
        hamburgers = ingredient.hamburger_set.all()
        if not hamburgers:
            ingredient.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)


class IntermediateDetail(APIView):

    def get_hamburger(self, pk):
        if not isinstance(pk, int):
            return 'not instance'
        try:
            return Hamburger.objects.get(pk=pk)
        except Hamburger.DoesNotExist:
            return 'not instance'

    def get_ingredient(self, pk):
        if not isinstance(pk, int):
            return 'doesnt exist'
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return 'doesnt exist'

    def put(self, request, pk, pk2, format=None):
        hamburger = self.get_hamburger(pk=pk)
        ingredient = self.get_ingredient(pk=pk2)

        if hamburger == 'not instance':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if ingredient == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)

        if ingredient not in hamburger.ingredientes.all():
            hamburger.ingredientes.add(ingredient)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, pk2, format=None):
        hamburger = self.get_hamburger(pk=pk)
        ingredient = self.get_ingredient(pk=pk2)

        if hamburger == 'not instance':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if ingredient == 'doesnt exist':
            return Response(status=status.HTTP_404_NOT_FOUND)

        if ingredient in hamburger.ingredientes.all():
            hamburger.ingredientes.remove(ingredient)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hamburgers': reverse(
            'hamburger-list',
            request=request,
            format=format
        ),
        'ingredients': reverse(
            'ingredient-list',
            request=request,
            format=format
        )
    })
