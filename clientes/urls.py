from django.urls import path
from .views import ListarClientesView, IncluirClienteView, EditarClienteView, ExcluirClienteView, verificar_cliente_existente

urlpatterns = [
    path('', ListarClientesView.as_view(), name='listar_clientes'),
    path('incluir/', IncluirClienteView.as_view(), name='incluir_cliente'),
    path('editar/<int:pk>/', EditarClienteView.as_view(), name='editar_cliente'),
    path('verificar_cliente_existente/', verificar_cliente_existente, name='verificar_cliente_existente'),
    path('excluir/<int:pk>/', ExcluirClienteView.as_view(), name='excluir_cliente')
]
