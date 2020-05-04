from django.urls import path
from .viewsets import (
    HamburgerViewSet,
    HamburgerDetail,
    IngredientDetail,
    IngredientViewSet,
    IntermediateDetail,
    api_root
)


hamburger_list = HamburgerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

hamburger_detail = HamburgerDetail.as_view()

ingredient_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredient_detail = IngredientDetail.as_view()

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
