def format_numeros(numeros):
    """Formata uma lista de números para exibição."""
    return ' - '.join(map(str, sorted(numeros)))

def validate_qtd_jogos(qtd):
    """Valida a quantidade de jogos."""
    try:
        qtd = int(qtd)
        return 1 <= qtd <= 10, qtd
    except ValueError:
        return False, None