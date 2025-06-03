from django import forms
from .models import TaxasI

class TaxaForm(forms.ModelForm):
    class Meta:
        model = TaxasI
        fields = ['valor']
        labels = {
            'valor': 'Valor da Taxa em %',
        }
        error_messages = {
            'valor': {
                'required': 'Informe um valor!',
            },
        }

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor is not None and valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")
        return valor

