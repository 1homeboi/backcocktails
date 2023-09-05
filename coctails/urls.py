"""
URL configuration for coctails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from constructor.views import *
router = DefaultRouter()

# Регистрируйте представления в маршрутере
router.register(r'ingredients', IngredientViewSet)
router.register(r'ingredientcategories', IngredientCategoryViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipeingredients', RecipeIngredientViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/recipes/', RecipeList.as_view()),
    path(r'api/products/<int:id>/', ProductDetail.as_view())
]