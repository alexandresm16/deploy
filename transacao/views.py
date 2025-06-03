from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from imovel.models import Imovel
from .models import Transacao
from .forms import TransacaoVendaForm, TransacaoAluguelForm


class ListarTransacaoView(ListView):
    model = Transacao
    template_name = 'transacoes.html'
    success_url = reverse_lazy('home')
    context_object_name = 'transacoes'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super().get_queryset()

        if buscar:
            qs = qs.filter(
                Q(transacao__cliente__nome__icontains=buscar) |
                Q(transacao__corretor__nome__icontains=buscar) |
                Q(transacao__imovel__codigo__icontains=buscar) |
                Q(transacao__imovel__tipo__icontains=buscar)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de corretores
        context['form'] = TransacaoVendaForm()

        # Mantém o termo de busca no formulário/input
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_transacoes'] = Transacao.objects.count()

        # Mensagem se a lista estiver vazia
        if not context['transacoes']:
            messages.info(self.request, "Nenhuma transação encontrada com esse filtro.")

        return context


class IncluirTransacaoVendaView(SuccessMessageMixin, CreateView):
    model = Transacao
    form_class = TransacaoVendaForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('listar_transacoes')
    success_message = 'Venda efetuada com sucesso!'

    def get_form(self, form_class=None):
        form_class = form_class or self.get_form_class()
        form = super().get_form(form_class)

        form.fields['imovel'].queryset = Imovel.objects.filter(status='disponivel').exclude(transacao='locacao')
        return form

    def form_valid(self, form):
        transacao = form.save(commit=False)
        transacao.tipo = 'Venda'
        transacao.valor = transacao.imovel.valor_venda
        transacao.imovel.status = 'vendido'
        transacao.imovel.save()
        if not transacao.imovel.valor_venda:
            form.add_error('imovel', 'Este imóvel não tem um valor de venda definido.')
            return self.form_invalid(form)
        transacao.save()
        return super().form_valid(form)


class IncluirTransacaoAluguelView(SuccessMessageMixin, CreateView):
    model = Transacao
    form_class = TransacaoAluguelForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('listar_transacoes')
    success_message = 'Aluguel efetuado com sucesso!'

    def get_form(self, form_class=None):
        form_class = form_class or self.get_form_class()
        form = super().get_form(form_class)

        form.fields['imovel'].queryset = Imovel.objects.filter(status='disponivel').exclude(transacao='venda')
        return form

    def form_valid(self, form):
        transacao = form.save(commit=False)
        transacao.tipo = 'Locacao'
        transacao.imovel.status = 'alugado'
        transacao.imovel.save()
        transacao.valor = transacao.imovel.valor_locacao
        transacao.save()
        if not transacao.imovel.valor_locacao:
            form.add_error('imovel', 'Este imóvel não tem um valor de Aluguel definido.')
            return self.form_invalid(form)
        return super().form_valid(form)


class EditarTransacaoVendaView(SuccessMessageMixin, UpdateView):
    model = Transacao
    form_class = TransacaoVendaForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('listar_transacoes')
    context_object_name = 'transacao'
    success_message = 'Transação Editada com sucesso!'


class EditarTransacaoAluguelView(SuccessMessageMixin, UpdateView):
    model = Transacao
    form_class = TransacaoVendaForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('listar_transacoes')
    context_object_name = 'transacao'
    success_message = 'Transação Editada com sucesso!'


class ExcluirTransacaoView(SuccessMessageMixin, DeleteView):
    model = Transacao
    template_name = 'detalhes_transacao.html'
    context_object_name = 'transacao'
    success_url = reverse_lazy('listar_transacoes')
    success_message = 'Transação excluida com sucesso!'


class DetailtransacaoView(DetailView):
    model = Transacao
    template_name = 'detalhes_transacao.html'
    context_object_name = 'transacao'
