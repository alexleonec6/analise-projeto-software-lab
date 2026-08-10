"""
Padrão de Projeto: State (Comportamental).
Modela os estados possíveis de uma Ordem de Serviço e encapsula o comportamento
de transição de cada estado, eliminando estruturas condicionais aninhadas (if/else).
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ordem_servico import OrdemServico


class EstadoInvalidoErro(Exception):
    """Exceção levantada quando uma transição de estado não é permitida pelo domínio."""
    pass


class IEstadoOS(ABC):
    """Interface abstrata base para estados da Ordem de Serviço."""

    @property
    @abstractmethod
    def nome(self) -> str:
        """Nome legível do estado atual."""
        pass

    def iniciar(self, os: "OrdemServico") -> None:
        raise EstadoInvalidoErro(f"Transição inválida: Não é possível iniciar a partir do estado '{self.nome}'.")

    def concluir(self, os: "OrdemServico") -> None:
        raise EstadoInvalidoErro(f"Transição inválida: Não é possível concluir a partir do estado '{self.nome}'.")

    def cancelar(self, os: "OrdemServico") -> None:
        raise EstadoInvalidoErro(f"Transição inválida: Não é possível cancelar a partir do estado '{self.nome}'.")


class EstadoCriada(IEstadoOS):
    """Estado inicial da OS."""

    @property
    def nome(self) -> str:
        return "CRIADA"

    def iniciar(self, os: "OrdemServico") -> None:
        os._mudar_estado(EstadoEmExecucao())

    def cancelar(self, os: "OrdemServico") -> None:
        os._mudar_estado(EstadoCancelada())


class EstadoEmExecucao(IEstadoOS):
    """Estado em que o serviço está sendo realizado."""

    @property
    def nome(self) -> str:
        return "EM_EXECUCAO"

    def concluir(self, os: "OrdemServico") -> None:
        os._mudar_estado(EstadoConcluida())

    def cancelar(self, os: "OrdemServico") -> None:
        os._mudar_estado(EstadoCancelada())


class EstadoConcluida(IEstadoOS):
    """Estado terminal de sucesso da OS."""

    @property
    def nome(self) -> str:
        return "CONCLUIDA"


class EstadoCancelada(IEstadoOS):
    """Estado terminal de cancelamento da OS."""

    @property
    def nome(self) -> str:
        return "CANCELADA"
