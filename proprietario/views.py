from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Proprietario
from .forms import ProprietarioForm


class ListarProprietariosView(ListView):
    model = Proprietario
    template_name = 'proprietarios.html'
    context_object_name = 'proprietarios'
    paginate_by = 4

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ListarProprietariosView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de clientes
        context['form'] = ProprietarioForm()

        # Campo de busca persistente no template
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_proprietarios'] = Proprietario.objects.count()

        # Verifica se o queryset está vazio
        if not context['proprietarios']:
            messages.info(self.request, "Nenhum proprietario encontrado com esse filtro.")

        return context


class IncluirProprietarioView(SuccessMessageMixin, CreateView):
    model = Proprietario
    form_class = ProprietarioForm
    template_name = 'proprietarios.html'
    success_url = reverse_lazy('listar_proprietarios')
    context_object_name = 'proprietarios'
    success_message = 'Proprietario cadastrado com sucesso!'

    def form_invalid(self, form):
        print("teste", form.errors)
        # Pega a lista atualizada para o contexto
        proprietarios = Proprietario.objects.all()
        context = {
            'form': form,
            self.context_object_name: proprietarios,
            "abrir_modal": True,  # para você controlar no template que abre o modal
        }
        return render(self.request, self.template_name, context)


class EditarProprietarioView(SuccessMessageMixin, UpdateView):
    model = Proprietario
    form_class = ProprietarioForm
    template_name = 'editarProprietario.html'
    success_url = reverse_lazy('listar_proprietarios')
    context_object_name = 'proprietarios'
    success_message = 'Proprietario editado com sucesso!'


class ExcluirProprietarioView(SuccessMessageMixin, DeleteView):
    model = Proprietario
    template_name = 'proprietarios.html'
    context_object_name = 'proprietario'
    success_url = reverse_lazy('listar_proprietarios')
    success_message = 'Proprietario excluido com sucesso!'
