from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'musicapp/index.html', context=None)


@login_required(login_url='login')
def user_home(request):
    return render(request, 'musicapp/user_home.html', context=None)
