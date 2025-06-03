from urllib import request

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from imovel.models import Imovel
from .forms import ReajustesForm
from .models import Reajustes


def calculaTaxa(request, id):
    print("id: ", id)
    listaImoveis = Imovel.objects.all()
    taxa = Reajustes.objects.get(pk=id)
    for imovel in listaImoveis:
        print(imovel.valor_venda)
        print(imovel.valor_locacao)
        imovel.valor_venda = imovel.valor_venda * (taxa.valor /10 +1)
        imovel.valor_locacao = imovel.valor_locacao * (taxa.valor /10 +1)
        imovel.save()
    return redirect('lista_reajustes')



class TaxasReajuste(ListView):
    model = Reajustes
    template_name = 'taxasReajuste.html'
    context_object_name = 'taxas_r'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de clientes
        context['form'] = ReajustesForm()

        # Campo de busca persistente no template
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_reajustes'] = Reajustes.objects.count()

        # Verifica se o queryset está vazio
        if not context['taxas_r']:
            messages.info(self.request, "Nenhuma taxa encontrada com esse filtro.")

        return context


class IncluirReajusteView(SuccessMessageMixin, CreateView):
    model = Reajustes
    form_class = ReajustesForm
    template_name = 'modalIncluir.html'
    success_url = reverse_lazy('lista_reajustes')
    context_object_name = 'taxas_r'
    success_message = 'Taxa cadastrada com sucesso!'


class EditarReajusteView(SuccessMessageMixin, UpdateView):
    model = Reajustes
    form_class = ReajustesForm
    template_name = 'modaisReajuste.html'
    success_url = reverse_lazy('lista_reajustes')
    context_object_name = 'taxas_r'
    success_message = 'Taxa editada com sucesso!'


class ExcluirReajuste(SuccessMessageMixin, DeleteView):
    model = Reajustes
    success_url = reverse_lazy('lista_reajustes')
    template_name = 'taxasReajuste.html'
    success_message = 'Taxa excluida com sucesso!'

# class CalculaIptu():
#
#     listaImoveis = Imovel.objects.all();
#     taxaIptu = Reajustes.objects.filter(nome='IPTU')

#     for imovel in listaImoveis:
#         imovel.valor_iptu = imovel.valor_iptu * taxa.valor /100


# Class CalculaTaxa():
#   listaImoveis = Imovel.objects.all();
#
#   for imovel in listaImoveis:
#       imovel.valor_venda = imovel.valor_venda * taxa.valor /100
#       imovel.valor_locacao = imovel.valor_locacao * taxa.valor /100
#


# Class CalculaTaxasAll():
#   listaImoveis = Imovel.objects.all();
#
#   for imovel in listaImoveis:
#       imovel.valor_iptu = imovel.valor_iptu * taxa.valor /100
#
