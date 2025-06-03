from django.contrib import admin
from .models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'imovel', 'cliente', 'valor', 'competencia', 'valortaxa')
    list_filter = ('tipo', 'competencia')
    search_fields = ('imovel__descricao', 'cliente__nome')