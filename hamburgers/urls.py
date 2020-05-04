from django.urls import path
from .viewsets import (
    HamburgerViewSet,
    IngredientViewSet,
    IntermediateDetail,
    api_root
)


hamburger_list = HamburgerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

hamburger_detail = HamburgerViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

ingredient_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredient_detail = IngredientViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

intermediate_detail = IntermediateDetail.as_view()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', api_root),
    path('hamburguesa/', hamburger_list, name='hamburger-list'),
    path('hamburguesa/<int:pk>/', hamburger_detail, name='hamburger-detail'),
    path('ingrediente/', ingredient_list, name='ingredient-list'),
    path('ingrediente/<int:pk>/', ingredient_detail, name='ingredient-detail'),
    path(
        'hamburguesa/<int:pk>/ingrediente/<int:pk2>/',
        intermediate_detail,
        name='intermediate-detail'
    ),
]
