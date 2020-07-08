from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Song
from django.db.models import Q


# Create your views here.
def index(request):
    songs = Song.objects.all()
    query = request.GET.get('q')

    if query:
        songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'songs':songs}
        return render(request, 'musicapp/index.html', context)

    context = {'songs':songs}
    print(context)
    return render(request, 'musicapp/index.html', context=context)


def detail(request, song_id):
    print(song_id)
    songs = Song.objects.filter(id=song_id).first()
    context = {'songs':songs}
    print(context)
    return render(request, 'musicapp/detail.html', context=context)