from django import template

register = template.Library()

@register.filter
def formatar_moeda(value):
    try:
        # Formata o valor como R$ 1.234,56
        return f'R$ {value:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value  # Retorna o valor original em caso de erro