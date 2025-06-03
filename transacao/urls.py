from django.urls import path
from .views import ListarTransacaoView, ExcluirTransacaoView, \
    DetailtransacaoView, IncluirTransacaoVendaView, IncluirTransacaoAluguelView, EditarTransacaoVendaView, \
    EditarTransacaoAluguelView

urlpatterns = [
    path('', ListarTransacaoView.as_view(), name='listar_transacoes'),
    path('venda/incluir/', IncluirTransacaoVendaView.as_view(), name='incluir_venda'),
    path('aluguel/incluir/', IncluirTransacaoAluguelView.as_view(), name='incluir_aluguel'),
    path('venda/editar/<int:pk>/', EditarTransacaoVendaView.as_view(), name='editar_venda'),
    path('aluguel/editar/<int:pk>/', EditarTransacaoAluguelView.as_view(), name='editar_aluguel'),
    path('excluir/<int:pk>/', ExcluirTransacaoView.as_view(), name='excluir_transacao'),
    path('visita/<int:pk>/', DetailtransacaoView.as_view(), name='visualizar_transacao'),
]
