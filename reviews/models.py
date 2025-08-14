from django.db import models
from django.contrib.auth.models import User
from animes.models import Anime  # ou onde estiver seu model de Anime

class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.anime.nome}"
