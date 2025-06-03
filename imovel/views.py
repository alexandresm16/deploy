from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin

from proprietario.models import Proprietario
from .models import Imovel
from .forms import ImovelForm, ProprietariosImoveis


class ListarImoveisView(ListView):
    model = Imovel
    template_name = 'imoveis.html'
    context_object_name = 'imoveis'
    paginate_by = 4

    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        status = self.request.GET.get('status', '')

        queryset = Imovel.objects.all().order_by('id')

        if buscar:
            queryset = queryset.filter(
                Q(codigo__icontains=buscar) |
                Q(cidade__icontains=buscar) |
                Q(uf__icontains=buscar) |
                Q(proprietario__nome__icontains=buscar) |
                Q(status__icontains=buscar) |
                Q(tipo__icontains=buscar)
            )

        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        buscar = self.request.GET.get('buscar', '')
        status = self.request.GET.get('status', '')

        context['buscar'] = buscar
        context['status'] = status
        context['qtd_imoveis'] = Imovel.objects.count()

        if not context['imoveis']:
            messages.info(self.request, "Não existem imóveis encontrados com esse filtro.")

        return context


class IncluirImovelView(SuccessMessageMixin, CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('listar_imoveis')
    context_object_name = 'imovel'
    success_message = 'Imovel cadastrado com sucesso!'


class EditarImovelView(SuccessMessageMixin, UpdateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('listar_imoveis')
    context_object_name = 'imovel'
    success_message = 'Imovel editado com sucesso!'


class ExcluirImovelView(SuccessMessageMixin, DeleteView):
    model = Imovel
    template_name = 'excluirImovel.html'
    success_url = reverse_lazy('listar_imoveis')
    context_object_name = 'imovel'
    success_message = 'Imovel excluido com sucesso!'


class DetailImovelView(DetailView):
    model = Imovel
    template_name = 'detalhes_Imovel.html'
    context_object_name = 'imovel'


class ImovelInLineEditView(TemplateResponseMixin, View):
    template_name = 'imovel_inline_edit.html'

    def get_formset(self, data=None):
        return ProprietariosImoveis(instance=self.imovel, data=data)

    def dispatch(self, request, pk):
        self.imovel = get_object_or_404(Imovel, id=pk)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'imovel': self.imovel, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('listar_imoveis')
        return self.render_to_response({'imovel': self.imovel, 'formset': formset})
