from django.urls import path
from .views import TaxasImobiliaria, EditarTaxaView

urlpatterns = [
    path('', TaxasImobiliaria.as_view(), name='lista_taxas'),
    path('editar/<int:pk>/', EditarTaxaView.as_view(), name='editar_taxa'),
]