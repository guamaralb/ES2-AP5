import shlex
from decimal import (
    Decimal,
    InvalidOperation,
)

from es2_ap5 import budget, storage

_ADICIONAR_NARGS = 2


def _cmd_adicionar(despesas, parts):
    if len(parts) != _ADICIONAR_NARGS:
        print('Uso: adicionar <descricao> <valor>')
        return despesas
    descricao, valor_str = parts
    try:
        valor = Decimal(valor_str)
    except InvalidOperation:
        print(f'Valor inválido: {valor_str}')
        return despesas
    try:
        despesas = budget.adicionar(despesas, descricao, valor)
    except ValueError as e:
        print(f'Erro: {e}')
        return despesas
    storage.salvar(despesas)
    print(f'Despesa adicionada: {descricao} — R$ {valor:.2f}')
    return despesas


def _cmd_resumo(despesas):
    if not despesas:
        print('Nenhuma despesa registrada.')
        return
    width_desc = max(len(d.descricao) for d in despesas)
    width_desc = max(width_desc, 10)
    for d in despesas:
        print(f'{d.data}  {d.descricao:<{width_desc}}  R$ {d.valor:>8.2f}')
    sep = '─' * (12 + width_desc + 16)
    print(sep)
    print(f'{"Total":<{width_desc + 12}}  R$ {budget.total(despesas):>8.2f}')


def main():
    despesas = storage.carregar()
    print('Rastreador de despesas. Digite "exit" para sair.')
    while True:
        try:
            line = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line == 'exit':
            break
        try:
            parts = shlex.split(line)
        except ValueError as e:
            print(f'Erro de sintaxe: {e}')
            continue
        cmd, *args = parts
        if cmd == 'adicionar':
            despesas = _cmd_adicionar(despesas, args)
        elif cmd == 'resumo':
            _cmd_resumo(despesas)
        else:
            print(
                f'Comando desconhecido: {cmd}.'
                ' Comandos: adicionar, resumo, exit'
            )


if __name__ == '__main__':
    main()
