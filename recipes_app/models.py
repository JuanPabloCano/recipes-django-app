from django.db import models
from django.db.models import Model


# Create your models here.

class User(Model):
    user_full_name = models.CharField(max_length=255)
    user_age = models.IntegerField()
    user_email = models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre: {self.user_full_name}"


class Recipes(Model):
    recipe_name = models.CharField(max_length=255)
    creation_date = models.DateField()
    recipe_ingredients = models.JSONField(null=True)
    recipe_instructions = models.TextField(null=False, help_text='Por favor escriba a detalle los pasos para la receta')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.recipe_name} - Usuario: {self.user.user_full_name}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
