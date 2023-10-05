from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    cocktail_id = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Review(models.Model):
    cocktail_id = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cocktail_id = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
