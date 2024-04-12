from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index_usuario.html')

def cadastro(request):
    return render(request, 'cadastro_usuario.html')

def criar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('index_usuario')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('index_usuario')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('index_usuario')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso')

        return redirect('index_usuario')
    else:
        return render(request, 'index_usuario.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('index_usuario')
        
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index_estoque')
    
    return render(request, 'index_usuario.html')