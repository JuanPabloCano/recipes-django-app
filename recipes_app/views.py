from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipes_app.models import *
from .forms import *


# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')


# Recipes

class RecipesList(ListView):
    model = Recipes
    template_name = 'recipeForms/recipes_list.html'


class RecipesDetail(DetailView):
    model = Recipes
    template_name = 'recipeForms/recipes_detail.html'


class RecipesCreate(CreateView):
    model = Recipes
    success_url = reverse_lazy('recipes_list')
    template_name = 'recipeForms/recipes_form.html'
    form_class = RecipesForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class RecipesUpdate(UpdateView):
    model = Recipes
    success_url = reverse_lazy('recipes_list')
    template_name = 'recipeForms/recipes_form.html'
    fields = ['recipe_name', 'creation_date', 'recipe_ingredients', 'recipe_instructions', 'user']


class RecipesDelete(DeleteView):
    model = Recipes
    template_name = 'recipeForms/recipes_confirm_delete.html'
    success_url = reverse_lazy('recipes_list')
    fields = ['recipe_name', 'creation_date', 'recipe_ingredients', 'recipe_instructions', 'user']


def recipe_search_result(request):
    return render(request, 'recipeForms/recipes_list.html')


def search_recipes(request):
    if request.GET['name']:
        name = request.GET['name']
        recipes = Recipes.objects.filter(recipe_name__contains=name)
        ctx = {'recipes': recipes,
               'name': name}
        return render(request, 'recipeForms/recipes_search_results.html', ctx)
    else:
        response = 'No se encontraron datos'
        ctx = {'response': response}
        return render(request, 'recipeForms/recipes_search_results.html', ctx)


# Users

class UsersList(ListView):
    model = User
    template_name = 'userForms/users_list.html'


class UserDetail(DetailView):
    model = User
    template_name = 'userForms/user_detail.html'


class UserCreate(CreateView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'userForms/user_form.html'
    form_class = UsersForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'userForms/user_form.html'
    fields = ['user_full_name', 'user_age', 'user_email']


class UserDelete(DeleteView):
    model = User
    template_name = 'userForms/users_confirm_delete.html'
    success_url = reverse_lazy('users_list')
    fields = ['user_full_name', 'user_age', 'user_email']


def user_search_result(request):
    return render(request, 'userForms/users_list.html')


def search_users(request):
    if request.GET['name']:
        name = request.GET['name']
        users = User.objects.filter(user_full_name__contains=name)
        ctx = {'users': users,
               'name': name}
        return render(request, 'userForms/users_search_results.html', ctx)
    else:
        response = 'No se encontraron datos'
        ctx = {'response': response}
        return render(request, 'userForms/users_search_results.html', ctx)