from django import forms
from .models import *


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['recipe_name', 'creation_date', 'recipe_ingredients', 'recipe_instructions', 'user']
        labels = {
            'recipe_name': 'Nombre de la receta',
            'creation_date': 'Fecha de creación',
            'recipe_ingredients': 'Ingredientes',
            'recipe_instructions': 'Instrucciones',
            'user': 'Chef'
        }


class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_full_name', 'user_age', 'user_email']
        labels = {
            'user_full_name': 'Nombre completo',
            'user_age': 'Edad',
            'user_email': 'Email'
        }
