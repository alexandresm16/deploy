from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator
from stdimage import StdImageField

from proprietarioImoveis.models import ProprietarioImovel


class Imovel(models.Model):
    codigo = models.CharField('Código do Imóvel', max_length=20, unique=True)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    uf = models.CharField('UF', max_length=2)
    cep = models.CharField('CEP', max_length=9)
    proprietario = models.ManyToManyField('proprietario.Proprietario', through='proprietarioImoveis.ProprietarioImovel', null=True, blank=True)


    @property
    def proprietarios(self):
        return ProprietarioImovel.objects.filter(proprietario=self)

    valor_venda = models.DecimalField(
        'Valor de Venda',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(100.00)],
        null=False,
        blank=False
    )

    valor_locacao = models.DecimalField(
        'Valor de Locação',
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(100.00)],
        null=False,
        blank=False
    )

    valor_iptu = models.DecimalField(
        'Valor do IPTU',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(100.00)],
        null=False,
        blank=False
    )

    valor_condominio = models.DecimalField(
        'Valor do Condomínio',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    area_total = models.DecimalField('Área Total (m²)', max_digits=10, decimal_places=2, null=True, blank=True)
    area_privada = models.DecimalField('Área Privada (m²)', max_digits=10, decimal_places=2, null=True, blank=True)
    area_util = models.IntegerField('Área Útil (m²)', null=True, blank=True)

    foto = CloudinaryField('Foto', null=True, blank=True)
    descricao = models.TextField('Descrição', null=True, blank=True)

    quartos = models.PositiveIntegerField('Quartos', default=0)
    banheiro = models.PositiveIntegerField('Banheiros', default=0)
    garagem = models.PositiveIntegerField('Vagas de Garagem', default=0)

    TIPO_CHOICES = [
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
        ('loft', 'Loft'),
        ('studio', 'Studio'),
        ('terreno', 'Terreno'),
        ('outro', 'Outro'),
    ]
    tipo = models.CharField('Tipo de Imóvel', max_length=20, choices=TIPO_CHOICES)

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('vendido', 'Vendido'),
        ('alugado', 'Alugado'),
        ('indisponivel', 'Indisponível'),
    ]
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES, default='disponivel')

    caracteristicas = models.TextField('Características', null=True, blank=True)
    comodidades = models.TextField('Comodidades', null=True, blank=True)

    TRANSACAO_CHOICES = [
        ('venda', 'Venda'),
        ('locacao', 'Locação'),
        ('venda_locacao', 'Venda e Locação'),
    ]

    transacao = models.CharField('Transação', max_length=20, choices=TRANSACAO_CHOICES)

    def __str__(self):
        return self.codigo
