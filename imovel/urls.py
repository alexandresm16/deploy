from django.urls import path
from .views import DetailImovelView, ListarImoveisView, EditarImovelView, IncluirImovelView, ImovelInLineEditView

urlpatterns = [
    path('', ListarImoveisView.as_view(), name='listar_imoveis'),
    path('incluir/', IncluirImovelView.as_view(), name='incluir_imovel'),
    path('editar/<int:pk>/', EditarImovelView.as_view(), name='editar_imovel'),
    path('excluir/<int:pk>/', DetailImovelView.as_view(), name='excluir_imovel'),
    path('imovel/<int:pk>/', DetailImovelView.as_view(), name='visualizar_imovel'),
    path('proprietario/inline/<int:pk>/', ImovelInLineEditView.as_view(), name='proprietario_imovel'),
]