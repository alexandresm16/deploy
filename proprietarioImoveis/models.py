from django.db import models

class ProprietarioImovel(models.Model):
    imovel = models.ForeignKey(
        'imovel.Imovel',
        on_delete=models.CASCADE,
        related_name='pi_imoveis',
        verbose_name="Imóvel"
    )
    proprietario = models.ForeignKey(
        'proprietario.Proprietario',
        on_delete=models.CASCADE,
        related_name='pi_proprietarios',
        verbose_name="Proprietário"
    )

    class Meta:
        verbose_name = "Proprietário de Imovel"
        verbose_name_plural = "Proprietários de Imovel"


    def __str__(self):
        return self.imovel.nome