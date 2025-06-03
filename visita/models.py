from django.db import models

class Visita(models.Model):
    AGENDADO = 'Agendado'
    CONCLUIDO = 'Concluido'
    CANCELADO = 'Cancelado'
    STATUS_CHOICES = [
        (AGENDADO, 'Agendado'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]

    data_hora = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name='Data e Hora'
    )
    corretor = models.ForeignKey(
        'corretor.Corretor',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Corretor'
    )
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Cliente'
    )
    imovel = models.ForeignKey(
        'imovel.Imovel',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Imóvel'
    )
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default=AGENDADO,
        null=False,
        blank=False,
        verbose_name='Status'
    )
    descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Descrição'
    )

    def __str__(self):
        return f"Visita de {self.cliente} a {self.imovel} em {self.data_hora}"