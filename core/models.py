from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    fone = models.CharField('Telefone', max_length=14, null=False, blank=False, unique=True)
    email = models.EmailField('E-mail', max_length=50, null=False, blank=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
