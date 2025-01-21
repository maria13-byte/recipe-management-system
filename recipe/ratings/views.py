from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Rating
from recipes.models import Recipe

@login_required
def rate_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        rating_value = request.POST['rating']
        Rating.objects.update_or_create(recipe=recipe, user=request.user, defaults={'rating': rating_value})
        return redirect('recipe_detail', pk=recipe.pk)
    return render(request, 'ratings/rate_recipe.html', {'recipe': recipe})

