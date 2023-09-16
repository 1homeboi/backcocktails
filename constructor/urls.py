from django.urls import path, include
from rest_framework import routers
from .views import (
    IngredientViewSet,
    IngredientCategoryViewSet,
    CocktailViewSet,
    CocktailIngredientViewSet,
    ReviewViewSet,
    UserViewSet,
    FavoriteViewSet,
)

# Создайте объект DefaultRouter
router = routers.DefaultRouter()

# Регистрируйте представления в маршрутере
router.register(r'ingredients', IngredientViewSet)
router.register(r'ingredientcategories', IngredientCategoryViewSet)
router.register(r'cocktails', CocktailViewSet)
router.register(r'cocktailingredients', CocktailIngredientViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'favorites', FavoriteViewSet)

# Определите маршруты
urlpatterns = [
    path('', include(router.urls)),
]
