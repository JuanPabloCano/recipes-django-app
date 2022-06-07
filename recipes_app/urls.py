from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('recipes/list/', RecipesList.as_view(), name='recipes_list'),
    path('recipes/<pk>', RecipesDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', RecipesCreate.as_view(), name='recipes_create'),
    path('recipes/update/<pk>', RecipesUpdate.as_view(), name='recipes_update'),
    path('recipes/delete/<pk>', RecipesDelete.as_view(), name='recipes_delete'),
    path('recipes/search/', search_recipes, name='search_recipes'),
    path('recipes/search/results/', recipe_search_result, name='recipes_search_results'),



    path('users/list/', UsersList.as_view(), name='users_list'),
    path('users/<pk>', UserDetail.as_view(), name='users_detail'),
    path('users/create/', UserCreate.as_view(), name='users_create'),
    path('users/update/<pk>', UserUpdate.as_view(), name='users_update'),
    path('users/delete/<pk>', UserDelete.as_view(), name='users_delete'),
    path('users/search/', search_users, name='search_users'),
    path('users/search/results/', user_search_result, name='users_search_results'),

]
