from django.urls import path
from . import views

urlpatterns = [
    path ('', views.listar_clientes, name = 'listar_clientes'),
    path ('Adicionar', views.adicionar_clientes, name= 'adicionar_clientes'),
    path ('Atualizar/<int:pk>', views.atualizar_clientes, name='atualizar_clientes'),
    path ('Deletar/?<int:pk', views.deletar_cliente, name='deletar_cliente')
]
