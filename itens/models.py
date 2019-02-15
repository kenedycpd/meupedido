from django.db import models

class Produto(models.Model):
	descricao = models.CharField('Descrição', max_length=100,blank=False)
	quantidade = models.IntegerField('Quantidade', default=1,blank=False)
	preco = models.DecimalField('Preço', max_digits=12, decimal_places=2,blank=False)

	class Meta:
		ordering = ('descricao',)
		verbose_name_plural = 'Produtos'
		verbose_name = 'Produto'

	def __str__(self):
		return self.descricao