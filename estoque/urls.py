from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexEstoque, name='index_estoque'),
    path('cadastro', views.cadastroEstoque, name='cadastro_estoque'),
    path('criar/produto', views.criarProduto, name='criar_produto'),
]