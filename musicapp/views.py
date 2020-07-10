from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    songs = Song.objects.all()
    query = request.GET.get('q')

    if query:
        songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'songs':songs}
        return render(request, 'musicapp/index.html', context)

    context = {'songs':songs}
    return render(request, 'musicapp/index.html', context=context)


def detail(request, song_id):
    songs = Song.objects.filter(id=song_id).first()
    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    
    if request.method == "POST":
        
        if 'playlist' in request.POST:
            playlist_name = request.POST["playlist"]
            q=Playlist(user=request.user,song=songs,playlist_name=playlist_name)
            q.save()
            messages.success(request, "Song added to playlist!")

    context = {'songs':songs,'playlists':playlists}
    return render(request, 'musicapp/detail.html', context=context)


def mymusic(request):
    return render(request, 'musicapp/mymusic.html')


def playlist(request):
    playlists = Playlist.objects.filter(user=request.user).values('playlist_name').distinct
    context = {'playlists':playlists}
    return render(request, 'musicapp/playlist.html', context=context)


def playlist_songs(request, playlist_name):
    songs = Song.objects.filter(playlist__playlist_name=playlist_name).distinct()

    if request.method == "POST":
        song_id = list(request.POST.keys())[1]
        playlist_song = Playlist.objects.filter(playlist_name=playlist_name, song__id=song_id)
        playlist_song.delete()
        messages.success(request, "Song removed from playlist!")

    context = {'playlist_name':playlist_name,'songs':songs}

    return render(request, 'musicapp/playlist_songs.html', context=context)


def favourite(request):
    return render(request, 'musicapp/favourite.html')


def all_songs(request):
    songs = Song.objects.all()
    query = request.GET.get('q')

    if query:
        songs = Song.objects.filter(Q(name__icontains=query)).distinct()
        context = {'songs':songs}
        return render(request, 'musicapp/all_songs.html', context)

    context = {'songs':songs}
    return render(request, 'musicapp/all_songs.html',context=context)