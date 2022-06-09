from django.contrib import admin
from messages_app.models import Message, Room

# Register your models here.

admin.site.register(Message)
admin.site.register(Room)
