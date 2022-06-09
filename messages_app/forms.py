from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message', 'user']
        labels = {
            'message': 'Mensaje',
            'user': 'Usuario',
        }
