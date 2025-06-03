from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView
from .models import TaxasI
from .forms import TaxaForm


class TaxasImobiliaria(ListView):
    model = TaxasI
    template_name = 'taxasImobiliaria.html'
    context_object_name = 'taxas_i'


class EditarTaxaView(UpdateView):
    model = TaxasI
    form_class = TaxaForm
    template_name = 'taxasImobiliaria.html'
    success_url = reverse_lazy('lista_taxas')
    context_object_name = 'taxas_i'