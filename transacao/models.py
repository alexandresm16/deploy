from datetime import timezone

from django.db import models

from clientes.models import Cliente
from corretor.models import Corretor
from imovel.models import Imovel
from taxasImobiliaria.models import TaxasI


class Transacao(models.Model):

    tipo = models.CharField(
        max_length=10,
        verbose_name="Tipo da Transação",
    )
    imovel = models.ForeignKey(
        Imovel,
        on_delete=models.CASCADE,
        related_name='transacoes',
        verbose_name="Imóvel"
    )
    corretor = models.ForeignKey(
        Corretor,
        on_delete=models.CASCADE,
        related_name='transacoes',
        verbose_name="Corretor"
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='transacoes',
        verbose_name="Cliente"
    )
    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Valor da Transação",
        editable=False
    )
    competencia = models.DateField(
        auto_now=True,
        verbose_name="Competência (Mês/Ano)",
    )
    valortaxa = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Valor da Taxa",
        editable=False
    )
    valortaxado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Valor faturado com a Transação",
        editable=False,
        null=True,
    )

    def save(self, *args, **kwargs):
        # Atribuir a taxa com base no tipo


        taxa = TaxasI.objects.filter(nome=self.tipo).first()

        if taxa:
            self.valortaxa = taxa.valor
        else:
            # Se não encontrar taxa para o tipo, atribua valor 0
            self.valortaxa = 0

        i = self.valortaxa / 100
        self.valortaxado = self.valor * i

        # Chama o metodo save da classe pai
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.imovel} - {self.cliente}"

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
        ordering = ['-competencia']
