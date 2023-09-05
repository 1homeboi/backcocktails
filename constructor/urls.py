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
router.register(r'ingredients', IngredientViewSet)
router.register(r'ingredientcategories', IngredientCategoryViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipeingredients', RecipeIngredientViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'favorites', FavoriteViewSet)

# Определите маршруты
urlpatterns = [
    path('api/', include(router.urls)),
]
