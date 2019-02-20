from django.db import models
from itens.models import Produto
from clientes.models import Clientes

class Pedido(models.Model):
	criado = models.DateTimeField(auto_now_add=True)
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=False)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, blank=False)
	preco = models.DecimalField('Preço', max_digits=12, decimal_places=2, blank=False)
	quantidade = models.IntegerField('Quantidade', default=1, blank=False)

	def otima(self):
		if self.preco > 100:
			return 'otima'
		if self.preco >=90:
			return 'boa'
		if self.preco <=89.99:
			return 'ruim'
	o = property(otima)

	
	
	def __str__(self):
		return "%s" % self.criado