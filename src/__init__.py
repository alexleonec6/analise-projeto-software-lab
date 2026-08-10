"""
Pacote src - Sistema de Gestão de Ordens de Serviço (SGOS).
Demonstrador prático de conceitos de Análise e Projeto de Software.
"""

from .entidades import Cliente, ItemServico
from .estados_os import IEstadoOS, EstadoCriada, EstadoEmExecucao, EstadoConcluida, EstadoCancelada, EstadoInvalidoErro
from .estrategia_desconto import IPoliticaDesconto, SemDesconto, DescontoValorFixo, DescontoPercentual
from .observadores import IObservadorOS, NotificadorLogConsole, AuditoriaEventos
from .ordem_servico import OrdemServico

__all__ = [
    "Cliente",
    "ItemServico",
    "IEstadoOS",
    "EstadoCriada",
    "EstadoEmExecucao",
    "EstadoConcluida",
    "EstadoCancelada",
    "EstadoInvalidoErro",
    "IPoliticaDesconto",
    "SemDesconto",
    "DescontoValorFixo",
    "DescontoPercentual",
    "IObservadorOS",
    "NotificadorLogConsole",
    "AuditoriaEventos",
    "OrdemServico",
]
