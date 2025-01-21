from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} rated {self.recipe.title} with {self.rating}'
