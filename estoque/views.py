from django.shortcuts import render, redirect
from .models import Estoque

def indexEstoque(request):
    if request.user.is_authenticated:
        lista_estoque = Estoque.objects.all()
        return render(request, 'listaEstoque.html', {'lista': lista_estoque})
    else:
        return redirect('index_usuario')

def cadastroEstoque(request):
    if request.user.is_authenticated:
        return render(request, 'cadastroEstoque.html')
    else:
        return redirect('index_usuario')

def criarProduto(request):
    nome_produto = request.POST['nome']
    descricao = request.POST['descricao']
    preco = request.POST['preco']
    min_estoque = request.POST['min_estoque']
    max_estoque = request.POST['max_estoque']
    produto = Estoque.objects.create(nome_produto=nome_produto, descricao=descricao, preco=preco, min_estoque=min_estoque, max_estoque=max_estoque)
    produto.save()
    return redirect('index_estoque')