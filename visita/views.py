from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import Visita
from .forms import VisitaForm
from django.urls import reverse_lazy


class ListarVisitasView(ListView):
    model = Visita
    template_name = 'visitas.html'
    context_object_name = 'visitas'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super().get_queryset()

        if buscar:  # Só filtra se buscar tiver valor
            qs = qs.filter(
                Q(imovel__codigo__icontains=buscar) |
                Q(cliente__nome__icontains=buscar) |
                Q(corretor__nome__icontains=buscar)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de corretores
        context['form'] = VisitaForm()

        # Mantém o termo de busca no formulário/input
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_visitas'] = Visita.objects.count()

        # Mensagem se a lista estiver vazia
        if not context['visitas']:
            messages.info(self.request, "Nenhuma visita encontrada com esse filtro.")

        return context


class IncluirVisitasView(SuccessMessageMixin, CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita_form.html'
    success_url = reverse_lazy('listar_visitas')
    context_object_name = 'visitas'
    success_message = 'Visita agendada com sucesso!'


class EditarVisitasView(SuccessMessageMixin, UpdateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita_form.html'
    success_url = reverse_lazy('listar_visitas')
    context_object_name = 'visitas'
    success_message = 'Visita editada com sucesso!'


class ExcluirVisitasView(SuccessMessageMixin, DeleteView):
    model = Visita
    template_name = 'visitas.html'
    context_object_name = 'visitas'
    success_url = reverse_lazy('listar_visitas')
    success_message = 'Visita excluida com sucesso!'


class DetailVisitaView(DetailView):
    model = Visita
    template_name = 'detalhesVisita.html'
    context_object_name = 'visita'
