"""
Módulo de Domínio e Entidades de Negócio.
Aplica princípios de OOD: Encapsulamento, Tipagem Forte e Imutabilidade onde pertinente.
"""

from dataclasses import dataclass, field
from typing import List
import uuid


@dataclass(frozen=True)
class Cliente:
    """Entidade que representa o ator externo Cliente."""
    id: str
    nome: str
    email: str


@dataclass
class ItemServico:
    """Entidade que compõe a Ordem de Serviço."""
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    descricao: str = ""
    preco_unitario: float = 0.0
    quantidade: int = 1

    def subtotal(self) -> float:
        """Calcula o valor parcial do item (preço * quantidade)."""
        if self.preco_unitario < 0 or self.quantidade < 1:
            raise ValueError("Preço unitário ou quantidade inválida.")
        return round(self.preco_unitario * self.quantidade, 2)
