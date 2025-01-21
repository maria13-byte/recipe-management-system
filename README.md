# Recipe Management System

## Overview

The Recipe Management System is a Django-based web application that allows users to create, update, delete, and view recipes. Users can also rate recipes and filter them by tags. The application includes user authentication, ensuring that only authenticated users can perform CRUD operations on recipes.

## Features

- User registration and login
- Create, update, and delete recipes
- View a list of all recipes
- View detailed information about a single recipe
- Rate recipes
- Search and filter recipes by tags

## Prerequisites

- Python 3.x
- Django 5.1.5
- Virtual environment (optional but recommended)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/maria13-byte/recipe-management-system
   cd recipe

 python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

python manage.py migrate
python manage.py runserver
Register: Go to http://127.0.0.1:8000/users/register/ to create a new user account.
Login: Go to http://127.0.0.1:8000/users/login/ to log in with your credentials.
Logout: Go to http://127.0.0.1:8000/users/logout/ to log out.



#in progress

Create Recipe: Go to http://127.0.0.1:8000/recipes/create/ to create a new recipe.
Update Recipe: Go to http://127.0.0.1:8000/recipes/update/<recipe_id>/ to update an existing recipe.
Delete Recipe: Go to http://127.0.0.1:8000/recipes/delete/<recipe_id>/ to delete a recipe.
View Recipes: Go to http://127.0.0.1:8000/recipes/ to view a list of all recipes.
View Recipe Details: Click on a recipe title in the list to view detailed information about the recipe.
Rate Recipe: Go to http://127.0.0.1:8000/ratings/rate/<recipe_id>/ to rate a recipe.
Search Recipes: Use the search form on the recipe list page to search for recipes by title or ingredients.
Filter Recipes by Tag: Use the filter links on the recipe list page to filter recipes by tag.
