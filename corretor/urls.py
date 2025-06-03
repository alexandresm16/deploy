from django.urls import path
from .views import ListarCorretoresView, IncluirCorretorView, EditarCorretorView, ExcluirCorretorView, verificar_corretor_existente

urlpatterns = [
    path('', ListarCorretoresView.as_view(), name='listar_corretores'),
    path('incluir/', IncluirCorretorView.as_view(), name='incluir_corretor'),
    path('editar/<int:pk>/', EditarCorretorView.as_view(), name='editar_corretor'),
    path('verificar_corretor_existente/', verificar_corretor_existente, name='verificar_corretor_existente'),
    path('excluir/<int:pk>/', ExcluirCorretorView.as_view(), name='excluir_corretor')
]