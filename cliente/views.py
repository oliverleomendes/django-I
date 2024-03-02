from django.shortcuts import render
from .models import Clientes

def index(request):
    lista_clientes = Clientes.objects.all()
    return render(request, 'index.html', {'lista': lista_clientes})

def cadastro(request):
    return render(request, 'cadastro.html')