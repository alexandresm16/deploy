import re
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Proprietario
import re


class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome', 'fone', 'email']  # Campos a serem exibidos e editados no formulário
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo',
                'minlength': '3'
            }),
            'fone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00)12345-6789',
                'inputmode': 'tel',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com',
                'minlength': '8'
            }),
        }
        error_messages = {
            'nome': {
                'required': 'O nome é obrigatório.',
                'max_length': 'O nome deve ter no máximo 50 caracteres.',
                'minlength': 'O tamanho minimo do nome deve ser de 10 caracteres',
            },
            'fone': {
                'required': 'O telefone é obrigatório.',
                'max_length': 'O telefone deve ter no máximo 14 caracteres.',
                'unique': 'Este número de telefone já está em uso.',
            },
            'email': {
                'required': 'O e-mail é obrigatório.',
                'invalid': 'Digite um endereço de e-mail válido.',
                'max_length': 'O e-mail deve ter no máximo 50 caracteres.',
                'unique': 'Este e-mail já está em uso.',
                'minlength': 'O tamanho minimo do nome deve ser de 8 caracteres',
            },
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not re.match(r'^[A-Za-zÀ-ÿ ]+$', nome):
            raise ValidationError('O nome deve conter apenas letras e espaços.')
        return nome

    def clean_fone(self):
        fone = self.cleaned_data.get('fone')
        if not re.fullmatch(r'\d{10,11}', fone):
            raise ValidationError('Este número de telefone é invalido')

        # Evita duplicidade de telefone
        qs = Proprietario.objects.filter(fone=fone)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError('Este número de telefone já está em uso.')
        return fone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Digite um endereço de e-mail válido.')

        # Evita duplicidade de email
        qs = Proprietario.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError('Este e-mail já está em uso.')
        return email
