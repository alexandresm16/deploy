from django import forms
from .models import Transacao
from imovel.models import Imovel
from corretor.models import Corretor
from clientes.models import Cliente
from taxasImobiliaria.models import TaxasI


class TransacaoVendaForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['imovel', 'corretor', 'cliente']

        # Personalizando os widgets
        widgets = {
            'imovel': forms.Select(attrs={'class': 'form-control'}),
            'corretor': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransacaoVendaForm, self).__init__(*args, **kwargs)

        self.fields['imovel'].error_messages = {
            'required': 'O imóvel é obrigatório.',
        }
        self.fields['corretor'].error_messages = {
            'required': 'O corretor é obrigatório.',
        }
        self.fields['cliente'].error_messages = {
            'required': 'O cliente é obrigatório.',
        }


class TransacaoAluguelForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['imovel', 'corretor', 'cliente']

        # Personalizando os widgets
        widgets = {
            'imovel': forms.Select(attrs={'class': 'form-control'}),
            'corretor': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransacaoAluguelForm, self).__init__(*args, **kwargs)

        self.fields['imovel'].error_messages = {
            'required': 'O imóvel é obrigatório.',
        }
        self.fields['corretor'].error_messages = {
            'required': 'O corretor é obrigatório.',
        }
        self.fields['cliente'].error_messages = {
            'required': 'O cliente é obrigatório.',
        }
