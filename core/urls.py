from django.urls import include, path
from . import views

urlpatterns = [
  path('clientes/', views.clientes, name='clientes'),
  path('produtos/', views.produtos, name='produtos'),
  path('pedido/', views.pedido, name='pedido'),
  path('lista/', views.lista, name='lista'),
  path('delete_pedido/<int:id_pedido>/', views.delete_pedido, name='delete_pedido'),
  path('edite_pedido/<int:id_pedido>/', views.edite_pedido, name='edite_pedido'),
]