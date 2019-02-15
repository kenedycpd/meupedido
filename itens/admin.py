from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('descricao', 'quantidade', 'preco')
	search_fields = ('descricao',)