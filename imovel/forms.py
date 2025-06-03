from django import forms
from django.forms import inlineformset_factory

from proprietarioImoveis.models import ProprietarioImovel
from .models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        labels = {
            'codigo': 'Código do Imóvel',
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'uf': 'UF',
            'cep': 'CEP',
            'valor_venda': 'Valor de Venda',
            'valor_locacao': 'Valor de Locação',
            'valor_iptu': 'Valor do IPTU',
            'valor_condominio': 'Valor do Condomínio',
            'area_total': 'Área Total (m²)',
            'area_privada': 'Área Privada (m²)',
            'area_util': 'Área Útil (m²)',
            'foto': 'Foto Principal',
            'descricao': 'Descrição',
            'quartos': 'Quartos',
            'banheiro': 'Banheiros',
            'garagem': 'Garagem',
            'tipo': 'Tipo de Imóvel',
            'status': 'Status',
            'caracteristicas': 'Características',
            'comodidades': 'Comodidades',
            'transacao': 'Transação',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: APT1024'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'valor_venda': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'valor_locacao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'valor_iptu': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'valor_condominio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'area_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'area_privada': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'area_util': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'quartos': forms.NumberInput(attrs={'class': 'form-control'}),
            'banheiro': forms.NumberInput(attrs={'class': 'form-control'}),
            'garagem': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'caracteristicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'comodidades': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'transacao': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'codigo': {
                'required': 'O código do imóvel é obrigatório.',
                'unique': 'Já existe um imóvel com esse código.',
            },
            'logradouro': {
                'required': 'O logradouro é obrigatório.',
            },
            'numero': {
                'required': 'O número é obrigatório.',
            },
            'valor_venda': {
                'required': 'O valor de venda é obrigatório.',
                'min_value': 'O valor de venda deve ser de no mínimo R$ 100,00.',
            },
            'valor_locacao': {
                'required': 'O valor de locação é obrigatório.',
                'min_value': 'O valor de locação deve ser de no mínimo R$ 100,00.',
            },
            'valor_iptu': {
                'required': 'O valor do IPTU é obrigatório.',
                'min_value': 'O valor do IPTU deve ser de no mínimo R$ 100,00.',
            },
            'area_util': {
                'invalid': 'Digite um número inteiro válido.',
            },
        }


ProprietariosImoveis = inlineformset_factory(Imovel, ProprietarioImovel, fk_name='imovel', fields=('proprietario',),
                                             extra=1, can_delete=True,
                                             widgets={'proprietario': forms.Select(attrs={'class': 'input'})})
