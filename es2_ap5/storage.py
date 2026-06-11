import json
from datetime import date
from decimal import Decimal
from pathlib import Path

from es2_ap5.models import Despesa

_DATA_FILE = Path.home() / '.despesas' / 'despesas.json'


def carregar(path: Path | None = None) -> list[Despesa]:
    p = path or _DATA_FILE
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding='utf-8'))
    return [
        Despesa(
            descricao=d['descricao'],
            valor=Decimal(d['valor']),
            data=date.fromisoformat(d['data']),
        )
        for d in data
    ]


def salvar(despesas: list[Despesa], path: Path | None = None) -> None:
    p = path or _DATA_FILE
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps(
            [
                {
                    'descricao': d.descricao,
                    'valor': str(d.valor),
                    'data': d.data.isoformat(),
                }
                for d in despesas
            ],
            indent=2,
            ensure_ascii=False,
        ),
        encoding='utf-8',
    )
