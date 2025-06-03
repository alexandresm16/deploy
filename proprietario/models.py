from core.models import Pessoa

class Proprietario(Pessoa):

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'

    def __str__(self):
        return self.nome
