from django.contrib import admin
from .models import Ingredient, IngredientCategory, Cocktail, CocktailIngredient, Review, User, Favorite

# Зарегистрируйте модели в административном интерфейсе
admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(Cocktail)
admin.site.register(CocktailIngredient)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Favorite)
