from django.urls import path
from .views import ListarVisitasView, IncluirVisitasView, EditarVisitasView, ExcluirVisitasView, DetailVisitaView

urlpatterns = [
    path('', ListarVisitasView.as_view(), name='listar_visitas'),
    path('incluir/', IncluirVisitasView.as_view(), name='incluir_visita'),
    path('editar/<int:pk>/', EditarVisitasView.as_view(), name='editar_visita'),
    path('excluir/<int:pk>/', ExcluirVisitasView.as_view(), name='excluir_visita'),
    path('visita/<int:pk>/', DetailVisitaView.as_view(), name='visualizar_visita')
]