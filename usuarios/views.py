from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import FormCriarUsuario
from django.contrib.auth.models import User
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormCriarUsuario(request.POST)
        username = request.POST.get('username')
        senha = request.POST.get('password1')
        confirmar = request.POST.get('password2')

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/registrar.html', {'form': form})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
            return render(request, 'usuarios/registrar.html', {'form': form})

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('custom_login')  

    else:
        form = FormCriarUsuario()

    return render(request, 'usuarios/registrar.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('custom_login')  