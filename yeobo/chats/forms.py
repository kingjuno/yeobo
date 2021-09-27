from django import forms
from . import models

class ChatForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ['chat']