from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Song


# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {'songs':songs}
    return render(request, 'musicapp/index.html', context=context)

