"""
Padrão de Projeto: Strategy (Comportamental).
Permite variar o algoritmo de cálculo de desconto independentemente dos clientes que o utilizam.
"""

from abc import ABC, abstractmethod


class IPoliticaDesconto(ABC):
    """Interface abstrata para definição de estratégias de desconto."""

    @abstractmethod
    def calcular_desconto(self, valor_bruto: float) -> float:
        """Calcula o valor nominal do desconto a partir do valor bruto."""
        pass


class SemDesconto(IPoliticaDesconto):
    """Estratégia padrão: nenhum desconto aplicado."""

    def calcular_desconto(self, valor_bruto: float) -> float:
        return 0.0


class DescontoValorFixo(IPoliticaDesconto):
    """Estratégia de desconto com abatimento fixo em reais."""

    def __init__(self, valor_fixo: float):
        if valor_fixo < 0:
            raise ValueError("Valor de desconto não pode ser negativo.")
        self._valor_fixo = valor_fixo

    def calcular_desconto(self, valor_bruto: float) -> float:
        return round(min(valor_bruto, self._valor_fixo), 2)


class DescontoPercentual(IPoliticaDesconto):
    """Estratégia de desconto percentual (ex: clientes VIP, convênios)."""

    def __init__(self, taxa_percentual: float):
        if not (0.0 <= taxa_percentual <= 100.0):
            raise ValueError("Percentual de desconto deve estar entre 0 e 100.")
        self._taxa = taxa_percentual / 100.0

    def calcular_desconto(self, valor_bruto: float) -> float:
        return round(valor_bruto * self._taxa, 2)
