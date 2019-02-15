from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Clientes, Pedido
from .forms import PedidoForm
from datetime import *
from django.contrib import messages
def home(request):
	return render(request, 'index.html',{})

def clientes(request):
	cliente = Clientes.objects.all()
	return render(request, 'core/tabela_cliente.html',{'cliente':cliente})


def produtos(request):
	prod = Produto.objects.all()
	return render(request, 'core/tabela_produtos.html',{'prod':prod})

def pedido(request):
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Produto Adicionado com Sucesso!')
			return redirect('pedido')
	else:
		form = PedidoForm()
	return render(request, 'core/pedido.html',{'form':form})

def lista(request):
	data = datetime.now()
	venda = Pedido.objects.all()
	return render(request, 'core/lista.html',{'venda':venda,'data':data})

def delete_pedido(request, id_pedido):
	pedido = Pedido.objects.get(id=id_pedido).delete()
	return redirect('lista')

def edite_pedido(request, id_pedido):
	edite = get_object_or_404(Pedido, id=id_pedido)
	if request.method == 'POST':
		form = PedidoForm(request.POST, instance=edite)
		if form.is_valid():
			form.save()
			return redirect('pedido')
	else:
		form = PedidoForm(instance=edite)
	return render(request, 'core/pedido.html',{'form':form})