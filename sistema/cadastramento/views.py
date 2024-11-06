#6. Criar as Views para o CRUD
from django.shortcuts import render, get_list_or_404, redirect
from .models import Cliente
from .forms import clienteForm

def listar_clientes (request):
    clientes = Cliente.objects.all()
    return render (request, 'cadastramento/listar_clientes.html', {'clientes':clientes})

#____________________________________________________________________________________________________________________

def adicionar_clientes (request):
    if request.method == 'POST':
        form = clienteForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('listar_clientes')
        else:
            form =clienteForm()
        return render ('cadastramento/adicionar_clientes.html', {'form' :form})

#____________________________________________________________________________________________________________________

def atualizar_clientes (request, pk):
    cliente = get_list_or_404 (cliente, pk=pk)
    if request.method == 'POST':
         form = clienteForm (request.POST, instance=cliente)
         if form.is_valid():
             form.save()
             return redirect ('listar_clientes')
         else:
             form = clienteForm (instance=cliente)
    return render (request, 'cadastramento/atualizar_clientes.html', {'form' :form})
            
def deletar_cliente(request, pk):
    cliente = get_list_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'cadastros/deletar_cliente.html', {'cliente': cliente})


# Create your views here.
