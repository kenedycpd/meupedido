from django.shortcuts import render
from .models import Produto
from .forms import ProdutoForm

def produto(request):
	if request.method == 'POST':
		form = ProdutoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('pedido')
	else:
		form = ProdutoForm()
	return render(request, 'core/pedido.html',{'form':form})