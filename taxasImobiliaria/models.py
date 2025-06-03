from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TaxasI(models.Model):
    nome = models.CharField('Taxa', max_length=20)
    valor = models.DecimalField('Valor da Taxa', max_digits=10, decimal_places=2, help_text='Valor da taxa', null=False,
                                blank=False, validators=[
    MinValueValidator(0.01, message='O valor não pode ser menor que 0.01'),
    MaxValueValidator(100.00, message='O valor não pode ser maior que 100.00')
])
    data_alteracao = models.DateTimeField('Data da Ultima alteração', auto_now=True)

    class Meta:
        verbose_name = 'Taxa'
        verbose_name_plural = 'Taxas'

    def __str__(self):
        return self.nome
