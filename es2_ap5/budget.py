from decimal import Decimal

from es2_ap5.models import Despesa


def adicionar(
    despesas: list[Despesa],
    descricao: str,
    valor: Decimal,
) -> list[Despesa]:
    if valor <= 0:
        raise ValueError('O valor deve ser positivo.')
    return [*despesas, Despesa(descricao=descricao, valor=valor)]


def total(despesas: list[Despesa]) -> Decimal:
    return sum((d.valor for d in despesas), Decimal('0'))
