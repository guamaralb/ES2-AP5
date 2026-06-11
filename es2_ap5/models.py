from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass
class Despesa:
    descricao: str
    valor: Decimal
    data: date = field(default_factory=date.today)
