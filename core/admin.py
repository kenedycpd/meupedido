from django.contrib import admin
from .models import Pedido
from django.utils.timezone import now

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ('criado', 'cliente', 'produto','quantidade','preco', 'total')
	search_fields = ('cliente', 'produto')
	date_hierarchy = ('criado')

