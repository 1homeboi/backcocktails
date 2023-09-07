from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientViewSet,
    IngredientCategoryViewSet,
    RecipeViewSet,
    RecipeIngredientViewSet,
    ReviewViewSet,
    UserViewSet,
    FavoriteViewSet,
)

# Создайте объект DefaultRouter
router = DefaultRouter()

# Регистрируйте представления в маршрутере
router.register('ingredients', IngredientViewSet)
router.register('ingredientcategories', IngredientCategoryViewSet)
router.register('recipes', RecipeViewSet)
router.register('recipeingredients', RecipeIngredientViewSet)
router.register('reviews', ReviewViewSet)
router.register('users', UserViewSet)
router.register('favorites', FavoriteViewSet)

# Определите маршруты
urlpatterns = [
    path('api/', include(router.urls)),
]
