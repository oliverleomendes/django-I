from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_usuario'),
    path('criar', views.criar, name='criar_usuario'),
    path('login', views.login, name='login_usuario')
]