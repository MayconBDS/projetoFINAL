from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    generos = models.ManyToManyField(Genero)
    imagem_url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
