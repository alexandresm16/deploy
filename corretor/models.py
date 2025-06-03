from core.models import Pessoa


class Corretor(Pessoa):

    class Meta:
        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'

    def __str__(self):
        return self.nome
