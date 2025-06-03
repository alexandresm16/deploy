from django.urls import path
from .views import ListarImoveisView

urlpatterns = [
    path('', ListarImoveisView.as_view(), name='index'),
]