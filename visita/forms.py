from django import forms
from .models import Visita


class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['data_hora', 'corretor', 'cliente', 'imovel', 'status', 'descricao']

        labels = {
            'data_hora': 'Data e Hora da Visita',
            'corretor': 'Corretor Responsável',
            'cliente': 'Cliente Interessado',
            'imovel': 'Imóvel',
            'status': 'Status da Visita',
            'descricao': 'Descrição',
        }

        widgets = {
            'data_hora': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Selecione data e hora',
            }),
            'corretor': forms.Select(attrs={'class': 'form-select'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'imovel': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adicione uma descrição da visita',
            }),
        }

        error_messages = {
            'data_hora': {
                'required': 'A data e hora da visita são obrigatórias.',
                'invalid': 'Digite uma data e hora válidas.',
            },
            'corretor': {
                'required': 'Selecione um corretor.',
            },
            'cliente': {
                'required': 'Selecione um cliente.',
            },
            'imovel': {
                'required': 'Selecione um imóvel.',
            },
            'status': {
                'required': 'Escolha o status da visita.',
            },
            'descricao': {
                'required': 'A descrição é obrigatória.',
                'max_length': 'A descrição deve ter no máximo 255 caracteres.',
            },
        }
