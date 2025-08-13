from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anime/<int:anime_id>/', views.anime_detalhes, name='anime_detalhes'),

]

