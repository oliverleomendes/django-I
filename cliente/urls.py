from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_cliente'),
    path('cadastro', views.cadastro, name='cadastro_cliente'),
    path('criar/cliente', views.criar, name='criar_cliente')
]