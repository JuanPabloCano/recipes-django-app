from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePage.as_view(), name='inicio'),
    path('about/', AboutMePage.as_view(), name='about'),
    path('recipes/list/', RecipesList.as_view(), name='recipes_list'),
    path('recipes/<pk>', RecipesDetail.as_view(), name='recipes_detail'),
    path('recipes/create/', RecipesCreate.as_view(), name='recipes_create'),
    path('recipes/update/<pk>', RecipesUpdate.as_view(), name='recipes_update'),
    path('recipes/delete/<pk>', RecipesDelete.as_view(), name='recipes_delete'),
    path('recipes/search/', search_recipes, name='search_recipes'),
    path('recipes/search/results/', RecipeSearchResult.as_view(), name='recipes_search_results'),

    path('users/list/', UsersList.as_view(), name='users_list'),
    path('users/<pk>', UserDetail.as_view(), name='users_detail'),
    path('users/create/', UserCreate.as_view(), name='users_create'),
    path('users/update/<pk>', UserUpdate.as_view(), name='users_update'),
    path('users/delete/<pk>', UserDelete.as_view(), name='users_delete'),
    path('users/search/', search_users, name='search_users'),
    path('users/search/results/', UserSearchResult.as_view(), name='users_search_results'),

    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login')
]
