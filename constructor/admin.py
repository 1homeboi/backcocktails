from django.contrib import admin
from .models import Ingredient, IngredientCategory, Recipe, RecipeIngredient, Review, User, Favorite

# Зарегистрируйте модели в административном интерфейсе
admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Favorite)
