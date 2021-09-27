from django.shortcuts import render,redirect
from django.http import HttpResponse


from .models import Chat
from . import forms

def home(request):
    chats = Chat.objects.all().order_by('id')
    return render(request,'home.html',{'chats':chats})