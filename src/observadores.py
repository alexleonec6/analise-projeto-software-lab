"""
Padrão de Projeto: Observer (Comportamental).
Define uma dependência um-para-muitos entre objetos para que, quando um objeto
muda de estado, todos os seus dependentes sejam notificados e atualizados automaticamente.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .ordem_servico import OrdemServico


class IObservadorOS(ABC):
    """Interface abstrata para assinantes de eventos de Ordem de Serviço."""

    @abstractmethod
    def notificar(self, os: "OrdemServico", estado_anterior: str, estado_novo: str) -> None:
        pass


class NotificadorLogConsole(IObservadorOS):
    """Observador concreto que emite mensagens formatadas no console/stdout."""

    def notificar(self, os: "OrdemServico", estado_anterior: str, estado_novo: str) -> None:
        print(
            f"[OBSERVER: LOG] OS #{os.id} | Cliente: {os.cliente.nome} | "
            f"Transição: [{estado_anterior}] -> [{estado_novo}]"
        )


class AuditoriaEventos(IObservadorOS):
    """Observador concreto que registra o histórico de eventos para compliance e relatórios."""

    def __init__(self):
        self.historico: List[dict] = []

    def notificar(self, os: "OrdemServico", estado_anterior: str, estado_novo: str) -> None:
        registro = {
            "os_id": os.id,
            "cliente": os.cliente.nome,
            "de": estado_anterior,
            "para": estado_novo,
            "valor_liquido": os.calcular_total()["liquido"]
        }
        self.historico.append(registro)
