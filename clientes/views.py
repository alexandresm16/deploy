import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm


class ListarClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    context_object_name = 'clientes'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClienteForm()
        return context

    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        qs = super(ListarClientesView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formulário para criação ou edição de clientes
        context['form'] = ClienteForm()

        # Campo de busca persistente no template
        context['buscar'] = self.request.GET.get('buscar', '')

        context['qtd_clientes'] = Cliente.objects.count()

        # Verifica se o queryset está vazio
        if not context['clientes']:
            messages.info(self.request, "Nenhum cliente encontrado com esse filtro.")

        return context


@csrf_protect
@require_POST
def verificar_cliente_existente(request):
    data = json.loads(request.body)
    fone = data.get('fone')
    email = data.get('email')
    cliente_id = data.get('cliente_id')  # pode ser None

    fone_existe = Cliente.objects.filter(fone=fone).exclude(id=cliente_id).exists()
    email_existe = Cliente.objects.filter(email=email).exclude(id=cliente_id).exists()

    return JsonResponse({
        'fone_existe': fone_existe,
        'email_existe': email_existe
    })


class IncluirClienteView(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'incluirCliente.html'
    success_url = reverse_lazy('listar_clientes')
    context_object_name = 'clientes'
    success_message = 'Cliente cadastrado com sucesso!'


class EditarClienteView(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'editarClientes.html'
    success_url = reverse_lazy('listar_clientes')
    context_object_name = 'clientes'
    success_message = 'Cliente editado com sucesso!'


class ExcluirClienteView(SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'excluirClientes.html'
    success_url = reverse_lazy('listar_clientes')
    context_object_name = 'clientes'
    success_message = 'Cliente excluido com sucesso!'
