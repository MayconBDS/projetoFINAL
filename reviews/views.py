from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from animes.models import Anime

def criar_review(request):
    animes = Anime.objects.all()

    if request.method == "POST":
        anime_id = request.POST.get("anime")
        mensagem = request.POST.get("mensagem")

        if not anime_id or not mensagem:
            return render(request, 'reviews/reviews_form.html', {
                'erro': 'Todos os campos são obrigatórios.',
                'animes': animes
            })

        anime = get_object_or_404(Anime, id=anime_id)
        Review.objects.create(usuario=request.user, anime=anime, mensagem=mensagem)

        # Redireciona para a página de reviews (ajuste o nome da url)
        return redirect('reviews')  # Certifique-se que 'reviews' está definido no seu urls.py

    return render(request, 'reviews/reviews_form.html', {
        'animes': animes
    })
