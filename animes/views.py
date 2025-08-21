from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Anime 

@login_required
def home(request):
    animes = Anime.objects.all()[:10]
    return render(request, 'animes/home.html', {'animes': animes})

def anime_detalhes(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'animes/detalhes.html', {'anime': anime})

@login_required
def profile_view(request):
    
    return render(request, 'usuarios/profile.html')
