"""
Bateria de Testes Unitários Automatizados (Engenharia de Qualidade).
Valida contratos, transições de estado (State), cálculo de descontos (Strategy) e eventos (Observer).
"""

import unittest
from src.entidades import Cliente, ItemServico
from src.estrategia_desconto import SemDesconto, DescontoValorFixo, DescontoPercentual
from src.estados_os import EstadoInvalidoErro
from src.observadores import AuditoriaEventos
from src.ordem_servico import OrdemServico


class TestAnaliseProjetoSoftware(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(id="CLI-1", nome="Teste Unitario", email="test@domain.com")

    def test_item_servico_subtotal(self):
        item = ItemServico(descricao="Item Teste", preco_unitario=150.0, quantidade=3)
        self.assertEqual(item.subtotal(), 450.0)

    def test_desconto_strategy_sem_desconto(self):
        os = OrdemServico(cliente=self.cliente, politica_desconto=SemDesconto())
        os.adicionar_item(ItemServico(descricao="Serviço A", preco_unitario=200.0, quantidade=1))
        resumo = os.calcular_total()
        self.assertEqual(resumo["bruto"], 200.0)
        self.assertEqual(resumo["desconto"], 0.0)
        self.assertEqual(resumo["liquido"], 200.0)

    def test_desconto_strategy_percentual(self):
        os = OrdemServico(cliente=self.cliente, politica_desconto=DescontoPercentual(10.0))
        os.adicionar_item(ItemServico(descricao="Serviço B", preco_unitario=500.0, quantidade=1))
        resumo = os.calcular_total()
        self.assertEqual(resumo["bruto"], 500.0)
        self.assertEqual(resumo["desconto"], 50.0)
        self.assertEqual(resumo["liquido"], 450.0)

    def test_desconto_strategy_fixo(self):
        os = OrdemServico(cliente=self.cliente, politica_desconto=DescontoValorFixo(75.0))
        os.adicionar_item(ItemServico(descricao="Serviço C", preco_unitario=300.0, quantidade=1))
        resumo = os.calcular_total()
        self.assertEqual(resumo["desconto"], 75.0)
        self.assertEqual(resumo["liquido"], 225.0)

    def test_ciclo_vida_sucesso(self):
        os = OrdemServico(cliente=self.cliente)
        self.assertEqual(os.estado.nome, "CRIADA")

        os.iniciar_execucao()
        self.assertEqual(os.estado.nome, "EM_EXECUCAO")

        os.concluir()
        self.assertEqual(os.estado.nome, "CONCLUIDA")

    def test_transicao_invalida_lanca_excecao(self):
        os = OrdemServico(cliente=self.cliente)
        # Não pode ir direto de CRIADA para CONCLUIDA
        with self.assertRaises(EstadoInvalidoErro):
            os.concluir()

    def test_observer_recebe_notificacoes(self):
        os = OrdemServico(cliente=self.cliente)
        auditor = AuditoriaEventos()
        os.inscrever_observador(auditor)

        os.adicionar_item(ItemServico(descricao="Item 1", preco_unitario=100.0, quantidade=1))
        os.iniciar_execucao()
        os.concluir()

        self.assertEqual(len(auditor.historico), 2)
        self.assertEqual(auditor.historico[0]["de"], "CRIADA")
        self.assertEqual(auditor.historico[0]["para"], "EM_EXECUCAO")
        self.assertEqual(auditor.historico[1]["de"], "EM_EXECUCAO")
        self.assertEqual(auditor.historico[1]["para"], "CONCLUIDA")


if __name__ == "__main__":
    unittest.main()
