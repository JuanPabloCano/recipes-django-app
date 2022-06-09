from django.db import models
from django.db.models import Model
from django_mysql.models import ListTextField


# Create your models here.

class UserModel(Model):
    user_full_name = models.CharField(max_length=255)
    user_age = models.IntegerField()
    user_email = models.CharField(max_length=500)

    def __str__(self):
        return self.user_full_name


class Recipes(Model):
    recipe_name = models.CharField(max_length=255)
    creation_date = models.DateField()
    recipe_ingredients = ListTextField(base_field=models.CharField(max_length=10000000))
    recipe_instructions = models.TextField(null=False, help_text='Por favor escriba a detalle los pasos para la receta')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.recipe_name} - Usuario: {self.user.user_full_name}"
