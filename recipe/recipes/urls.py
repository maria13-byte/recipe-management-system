from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('filter/<str:tag_name>/', views.filter_recipes_by_tag, name='filter_recipes_by_tag'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]


