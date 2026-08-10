"""
Módulo Principal de Demonstração Interativa.
Executa o ciclo de vida completo de uma OS, demonstrando os conceitos de OOA/OOD.
"""

from src.entidades import Cliente, ItemServico
from src.estrategia_desconto import DescontoPercentual, DescontoValorFixo, SemDesconto
from src.observadores import NotificadorLogConsole, AuditoriaEventos
from src.estados_os import EstadoInvalidoErro
from src.ordem_servico import OrdemServico


def executar_demonstracao():
    print("=" * 70)
    print(" SGOS - SISTEMA DE GESTÃO DE ORDENS DE SERVIÇO")
    print(" Demonstração dos Conceitos de Análise e Projeto de Software (IFRS/MEC)")
    print("=" * 70)

    # 1. Criação do Ator Externo (Cliente)
    cliente = Cliente(id="CLI-001", nome="Alexandre Souza", email="alexleonec6@gmail.com")
    print(f"\n[1] Ator Cliente instanciado: {cliente.nome} ({cliente.email})")

    # 2. Instanciação da Ordem de Serviço com Padrão Strategy
    # Configurando inicialmente com desconto VIP de 15%
    politica_desconto = DescontoPercentual(taxa_percentual=15.0)
    os = OrdemServico(cliente=cliente, politica_desconto=politica_desconto, id_customizado="OS-2026-X1")
    print(f"[2] Ordem de Serviço criada: #{os.id} | Estado Inicial: {os.estado.nome}")

    # 3. Padrão Observer: Inscrição de observadores
    logger = NotificadorLogConsole()
    auditor = AuditoriaEventos()
    os.inscrever_observador(logger)
    os.inscrever_observador(auditor)
    print("[3] Observadores cadastrados: NotificadorLogConsole, AuditoriaEventos")

    # 4. Composição de Itens
    os.adicionar_item(ItemServico(descricao="Análise e Levantamento de Requisitos de Software", preco_unitario=450.0, quantidade=1))
    os.adicionar_item(ItemServico(descricao="Modelagem UML (Casos de Uso, Classes, DTE)", preco_unitario=350.0, quantidade=2))
    os.adicionar_item(ItemServico(descricao="Prototipação Funcional e Arquitetura CASE", preco_unitario=600.0, quantidade=1))

    resumo = os.calcular_total()
    print("\n[4] Itens adicionados à OS:")
    for item in os.itens:
        print(f"    - {item.descricao}: {item.quantidade}x R$ {item.preco_unitario:.2f} = R$ {item.subtotal():.2f}")
    print(f"    -> Total Bruto: R$ {resumo['bruto']:.2f}")
    print(f"    -> Desconto Aplicado (15% Strategy): R$ {resumo['desconto']:.2f}")
    print(f"    -> Total Líquido a Pagar: R$ {resumo['liquido']:.2f}")

    # 5. Padrão State: Transição de Estados
    print("\n[5] Evolução do Ciclo de Vida (Padrão State + Observer):")
    os.iniciar_execucao()
    print(f"    Estado atual da OS: {os.estado.nome}")

    os.concluir()
    print(f"    Estado atual da OS: {os.estado.nome}")

    # 6. Teste de Validação de Regra de Negócio (Transição inválida)
    print("\n[6] Teste de Proteção de Estado (tentando reiniciar uma OS já concluída):")
    try:
        os.iniciar_execucao()
    except EstadoInvalidoErro as err:
        print(f"    [SUCESSO] Exceção esperada interceptada: {err}")

    # 7. Resumo da Auditoria
    print("\n[7] Relatório Final da Auditoria (Observer):")
    for reg in auditor.historico:
        print(f"    Transição: {reg['de']} -> {reg['para']} | Valor Final: R$ {reg['valor_liquido']:.2f}")

    print("\n" + "=" * 70)
    print(" Fim da Execução com Sucesso!")
    print("=" * 70)


if __name__ == "__main__":
    executar_demonstracao()
