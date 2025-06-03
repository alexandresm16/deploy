from django.urls import path
from .views import ListarProprietariosView, EditarProprietarioView, ExcluirProprietarioView, IncluirProprietarioView

urlpatterns = [
    path('', ListarProprietariosView.as_view(), name='listar_proprietarios'),
    path('incluir/', IncluirProprietarioView.as_view(), name='incluir_proprietario'),
    path('editar/<int:pk>/', EditarProprietarioView.as_view(), name='editar_proprietario'),
    path('excluir/<int:pk>/', ExcluirProprietarioView.as_view(), name='excluir_proprietario')
]