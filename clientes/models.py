from django.db import models


class Clientes(models.Model):
	nome = models.CharField('Nome', max_length=100, blank=False)
	
	class Meta:
		verbose_name_plural = 'Clientes'
		verbose_name = 'Cliente'

	def __str__(self):
		return self.nome