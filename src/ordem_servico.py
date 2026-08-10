"""
Entidade Agregadora Central: OrdemServico.
Integra o padrão State (ciclo de vida), Strategy (faturamento/desconto) e Observer (eventos).
"""

from typing import List, Dict
import uuid

from .entidades import Cliente, ItemServico
from .estados_os import IEstadoOS, EstadoCriada
from .estrategia_desconto import IPoliticaDesconto, SemDesconto
from .observadores import IObservadorOS


class OrdemServico:
    """Classe agregadora que encapsula a lógica de negócio e ciclo de vida da OS."""

    def __init__(
        self,
        cliente: Cliente,
        politica_desconto: IPoliticaDesconto = None,
        id_customizado: str = None
    ):
        self._id = id_customizado or str(uuid.uuid4())[:8]
        self._cliente = cliente
        self._itens: List[ItemServico] = []
        self._estado: IEstadoOS = EstadoCriada()
        self._politica_desconto: IPoliticaDesconto = politica_desconto or SemDesconto()
        self._observadores: List[IObservadorOS] = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def estado(self) -> IEstadoOS:
        return self._estado

    @property
    def itens(self) -> List[ItemServico]:
        return list(self._itens)

    def adicionar_item(self, item: ItemServico) -> None:
        if self._estado.nome != "CRIADA":
            raise ValueError(f"Não é permitido modificar itens no estado atual: {self._estado.nome}")
        self._itens.append(item)

    def definir_politica_desconto(self, politica: IPoliticaDesconto) -> None:
        self._politica_desconto = politica

    def inscrever_observador(self, observador: IObservadorOS) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador: IObservadorOS) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def _mudar_estado(self, novo_estado: IEstadoOS) -> None:
        estado_antigo = self._estado.nome
        self._estado = novo_estado
        self._notificar_observadores(estado_antigo, novo_estado.nome)

    def _notificar_observadores(self, anterior: str, novo: str) -> None:
        for obs in self._observadores:
            obs.notificar(self, anterior, novo)

    # Métodos delegados ao padrão State
    def iniciar_execucao(self) -> None:
        self._estado.iniciar(self)

    def concluir(self) -> None:
        self._estado.concluir(self)

    def cancelar(self) -> None:
        self._estado.cancelar(self)

    def calcular_total(self) -> Dict[str, float]:
        """Calcula resumo financeiro aplicando o padrão Strategy configurado."""
        bruto = sum(item.subtotal() for item in self._itens)
        desconto = self._politica_desconto.calcular_desconto(bruto)
        liquido = max(0.0, round(bruto - desconto, 2))
        return {
            "bruto": round(bruto, 2),
            "desconto": round(desconto, 2),
            "liquido": liquido
        }
