import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Corretor
from .forms import CorretorForm


class ListarCorretoresView(ListView):
    model = Corretor
    template_name = 'Corretores.html'
    context_object_name = 'corretores'
    paginate_by = 4

    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        qs = super().get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de corretores
        context['form'] = CorretorForm()

        # Mantém o termo de busca no formulário/input
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_corretores'] = Corretor.objects.count()

        # Mensagem se a lista estiver vazia
        if not context['corretores']:
            messages.info(self.request, "Nenhum corretor encontrado com esse filtro.")

        return context


@csrf_protect
@require_POST
def verificar_corretor_existente(request):
    data = json.loads(request.body)
    fone = data.get('fone')
    email = data.get('email')
    corretor_id = data.get('corretor_id')  # pode ser None

    fone_existe = Corretor.objects.filter(fone=fone).exclude(id=corretor_id).exists()
    email_existe = Corretor.objects.filter(email=email).exclude(id=corretor_id).exists()

    return JsonResponse({
        'fone_existe': fone_existe,
        'email_existe': email_existe
    })


class IncluirCorretorView(SuccessMessageMixin, CreateView):
    model = Corretor
    form_class = CorretorForm
    template_name = 'incluirCorretor.html'
    success_url = reverse_lazy('listar_corretores')
    context_object_name = 'corretores'
    success_message = 'Corretor cadastrado com sucesso!'


class EditarCorretorView(SuccessMessageMixin, UpdateView):
    model = Corretor
    form_class = CorretorForm
    template_name = 'editarCorretor.html'
    success_url = reverse_lazy('listar_corretores')
    context_object_name = 'corretores'
    success_message = 'Corretor editado com sucesso!'


class ExcluirCorretorView(SuccessMessageMixin, DeleteView):
    model = Corretor
    template_name = 'excluirCorretor.html'
    success_url = reverse_lazy('listar_corretores')
    context_object_name = 'corretores'
    success_message = 'Corretor excluido com sucesso!'
