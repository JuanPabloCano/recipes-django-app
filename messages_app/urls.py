from django.urls import path
from messages_app import views

urlpatterns = [
    path('rooms/', views.home, name='chat_rooms'),
    path('<str:room>/', views.room, name='room'),
    path('rooms/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')
]
