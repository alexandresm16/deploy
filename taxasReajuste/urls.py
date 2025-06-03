from django.urls import path
from .views import TaxasReajuste, EditarReajusteView, ExcluirReajuste, IncluirReajusteView, calculaTaxa

urlpatterns = [
    path('', TaxasReajuste.as_view(), name='lista_reajustes'),
    path('incluir/', IncluirReajusteView.as_view(), name='incluir_reajuste'),
    path('editar/<int:pk>/', EditarReajusteView.as_view(), name='editar_reajuste'),
    path('excluir/<int:pk>/', ExcluirReajuste.as_view(), name='excluir_reajuste'),
    path('calcula/taxa/<int:id>/', calculaTaxa, name='calcula_taxa'),
]