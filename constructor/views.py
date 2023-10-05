from rest_framework import viewsets
from .models import Ingredient, Cocktail, CocktailIngredient, Review, User, Favorite
from .serializers import IngredientSerializer, CocktailSerializer, CocktailIngredientSerializer, ReviewSerializer, UserSerializer, FavoriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailIngredientViewSet(viewsets.ModelViewSet):
    queryset = CocktailIngredient.objects.all()
    serializer_class = CocktailIngredientSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        'cocktail_id': ['exact'],
    }
    #search_fields = ['comment']
    #ordering_fields = ['pub_date']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
