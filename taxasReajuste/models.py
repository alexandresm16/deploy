from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class ClasseChoices(models.TextChoices):
    LOCAL = 'LC', 'Local'
    FEDERAL = 'FD', 'Federal'
    ESTADUAL = 'ES', 'Estadual'
    MUNICIPAL = 'MN', 'Municipal'

class Reajustes(models.Model):
    nome = models.CharField('nome', max_length=20)
    data_alteracao = models.DateTimeField('Data da Ultima alteração', auto_now=True)
    #data_aplicacao = models.DateTimeField('Data da Ultima Aplicação')
    classe = models.CharField(
        max_length=2,
        choices=ClasseChoices.choices,
        default=ClasseChoices.LOCAL,
    )
    valor = models.DecimalField('Valor da Taxa', max_digits=10, decimal_places=2, help_text='Valor da taxa', null=False,
                                blank=False, validators=[
    MinValueValidator(0.01, message='O valor não pode ser menor que 0.01'),
    MaxValueValidator(100.00, message='O valor não pode ser maior que 100.00')
])

    class Meta:
        verbose_name = 'Reajuste'
        verbose_name_plural = 'Reajustes'

    def __str__(self):
        return self.nome