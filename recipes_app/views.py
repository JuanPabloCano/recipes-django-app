from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import *


# Create your views here.

# Recipes

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        ctx = {'title': 'Prueba'}
        return render(request, self.template_name, ctx)


class AboutMePage(TemplateView):
    template_name = 'about_me.html'

    def get(self, request, *args, **kwargs):
        ctx = {'title': 'Prueba'}
        return render(request, self.template_name, ctx)


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


class RecipeSearchResult(TemplateView):
    template_name = 'recipeForms/recipes_list.html'

    def get(self, request, *args, **kwargs):
        ctx = {'title': 'Prueba'}
        return render(request, self.template_name, ctx)


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
    model = UserModel
    template_name = 'userForms/users_list.html'


class UserDetail(DetailView):
    model = UserModel
    template_name = 'userForms/user_detail.html'


class UserCreate(CreateView):
    model = UserModel
    success_url = reverse_lazy('users_list')
    template_name = 'userForms/user_form.html'
    form_class = UsersForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = UserModel
    success_url = reverse_lazy('users_list')
    template_name = 'userForms/user_form.html'
    fields = ['user_full_name', 'user_age', 'user_email']


class UserDelete(DeleteView):
    model = UserModel
    template_name = 'userForms/users_confirm_delete.html'
    success_url = reverse_lazy('users_list')
    fields = ['user_full_name', 'user_age', 'user_email']


class UserSearchResult(TemplateView):
    template_name = 'userForms/users_list.html'

    def get(self, request, *args, **kwargs):
        ctx = {'title': 'Prueba'}
        return render(request, self.template_name, ctx)


def search_users(request):
    if request.GET['name']:
        name = request.GET['name']
        users = UserModel.objects.filter(user_full_name__contains=name)
        ctx = {'users': users,
               'name': name}
        return render(request, 'userForms/users_search_results.html', ctx)
    else:
        response = 'No se encontraron datos'
        ctx = {'response': response}
        return render(request, 'userForms/users_search_results.html', ctx)


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes_list')
    else:
        form = UserSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
