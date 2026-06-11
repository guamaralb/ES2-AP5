from decimal import Decimal

import pytest

from es2_ap5.budget import adicionar, total
from es2_ap5.models import Despesa


def test_adicionar_retorna_lista_com_nova_despesa():
    resultado = adicionar([], 'Café', Decimal('5.00'))
    assert len(resultado) == 1
    assert resultado[0].descricao == 'Café'
    assert resultado[0].valor == Decimal('5.00')


def test_adicionar_nao_muta_lista_original():
    original = [Despesa(descricao='Almoço', valor=Decimal('20.00'))]
    adicionar(original, 'Jantar', Decimal('30.00'))
    assert len(original) == 1


def test_adicionar_valor_negativo_levanta_valor_error():
    with pytest.raises(ValueError, match='positivo'):
        adicionar([], 'Erro', Decimal('-1.00'))


def test_adicionar_valor_zero_levanta_valor_error():
    with pytest.raises(ValueError, match='positivo'):
        adicionar([], 'Erro', Decimal('0'))


def test_total_soma_todos_os_valores():
    despesas = [
        Despesa(descricao='Café', valor=Decimal('5.00')),
        Despesa(descricao='Almoço', valor=Decimal('20.50')),
        Despesa(descricao='Lanche', valor=Decimal('4.50')),
    ]
    assert total(despesas) == Decimal('30.00')
