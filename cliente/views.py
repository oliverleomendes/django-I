from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        lista_clientes = Clientes.objects.all()
        return render(request, 'index.html', {'lista': lista_clientes})
    else:
        return redirect('index_usuario')

def cadastro(request):
    if request.user.is_authenticated:
        return render(request, 'cadastro.html')
    else:
        return redirect('index_usuario')

def criar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']
    cliente = Clientes.objects.create(primeiro_nome=nome, sobrenome=sobrenome,
                                        email=email, status=1)
    cliente.save()
    return redirect('index_cliente')

def editar(request, id_cliente):
    if request.user.is_authenticated:
        cliente = get_object_or_404(Clientes, pk=id_cliente)
        return render(request, 'editar_cliente.html', {'dados_cliente': cliente})
    else:
        return redirect('index_usuario')

def atualizar_cliente(request):
    id_cliente = request.POST["id"]
    cliente = Clientes.objects.get(pk=id_cliente)
    cliente.primeiro_nome = request.POST["nome"]
    cliente.sobrenome = request.POST["sobrenome"]
    cliente.email = request.POST["email"]
    cliente.save()
    return redirect('index_cliente')

def deletar_cliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, pk=id_cliente)
    cliente.delete()
    return redirect('index_cliente')