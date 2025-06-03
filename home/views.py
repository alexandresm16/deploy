from imovel.models import Imovel
from django.views.generic import ListView

class ListarImoveisView(ListView):
    model = Imovel
    template_name = 'index.html'
    context_object_name = 'imoveis'

    def get_queryset(self):
        return Imovel.objects.filter(status='disponivel')