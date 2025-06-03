from django import forms
from .models import Reajustes, ClasseChoices


class ReajustesForm(forms.ModelForm):
    class Meta:
        model = Reajustes
        fields = ['nome', 'classe', 'valor']
        labels = {
            'nome': 'Nome do Reajuste',
            'classe': 'Classe do Reajuste',
            'valor': 'Valor da Taxa em %',
        }
        error_messages = {
            'nome': {
                'required': 'O nome do reajuste é obrigatório.',
                'max_length': 'O nome deve conter no máximo 20 caracteres.',
            },
            'classe': {
                'required': 'A classe do reajuste é obrigatória.',
                'invalid_choice': 'Selecione uma classe válida.',
            },
            'valor': {
                'required': 'O valor da taxa é obrigatório.',
                'invalid': 'Digite um número válido para o valor da taxa.',
            },
        }
        help_texts = {
            'valor': 'Informe um valor entre 0.01 e 100.00',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Reajuste Anual',
            }),
            'classe': forms.Select(choices=ClasseChoices.choices),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 3.5',
                'step': '0.01',
                'min': '0'
            }),

        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome
