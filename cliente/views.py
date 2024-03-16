from django.shortcuts import render, redirect
from .models import Clientes
from datetime import datetime

def index(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'index.html', {'lista': lista_clientes})

def cadastro(request):
    return render(request, 'cadastro.html')

def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    cliente = Clientes.objects.create(primeiro_nome=nome, sobrenome=sobrenome,
                                        email=email, status=1)
    cliente.save()
    return redirect('index')
    