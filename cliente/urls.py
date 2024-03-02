from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='indexClientes'),
    path('cadastro', views.cadastro, name='cadastroClientes'),
]
