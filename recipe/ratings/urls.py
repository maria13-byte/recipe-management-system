from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:pk>/', views.rate_recipe, name='rate_recipe'),
]
