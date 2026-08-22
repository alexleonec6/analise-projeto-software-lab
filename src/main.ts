/**
 * Demonstração Prática Interativa em TypeScript.
 * Roda de ponta a ponta simulando uma Ordem de Serviço real.
 */

import { Cliente, ItemServico } from "./entidades.ts";
import { DescontoPercentual } from "./estrategiaDesconto.ts";
import { NotificadorLogConsole, AuditoriaEventos } from "./observadores.ts";
import { EstadoInvalidoErro } from "./estadosOS.ts";
import { OrdemServico } from "./ordemServico.ts";

function executarDemonstracao(): void {
  console.log("=".repeat(70));
  console.log(" SGOS - SISTEMA DE GESTÃO DE ORDENS DE SERVIÇO (TypeScript)");
  console.log(" Demonstração dos Conceitos de Análise e Projeto de Software (IFRS/MEC)");
  console.log("=".repeat(70));

  // 1. Instanciando Ator Cliente
  const cliente = new Cliente("CLI-001", "Alexandre Souza", "alexleonec6@gmail.com");
  console.log(`\n[1] Ator Cliente: ${cliente.nome} (${cliente.email})`);

  // 2. Ordem de Serviço com Desconto (Strategy)
  const descontoVip = new DescontoPercentual(15);
  const os = new OrdemServico(cliente, descontoVip, "OS-2026-TS1");
  console.log(`[2] Ordem de Serviço criada: #${os.id} | Estado: ${os.estado.nome}`);

  // 3. Cadastrando Observadores (Observer)
  const logger = new NotificadorLogConsole();
  const auditor = new AuditoriaEventos();
  os.inscreverObservador(logger);
  os.inscreverObservador(auditor);
  console.log("[3] Observadores cadastrados: NotificadorLogConsole, AuditoriaEventos");

  // 4. Adicionando Itens de Serviço
  os.adicionarItem(new ItemServico("Análise e Levantamento de Requisitos", 450.0, 1));
  os.adicionarItem(new ItemServico("Modelagem UML e Arquitetura", 350.0, 2));
  os.adicionarItem(new ItemServico("Prototipação e Validação", 600.0, 1));

  const total = os.calcularTotal();
  console.log("\n[4] Itens da Ordem de Serviço:");
  for (const item of os.itens) {
    console.log(`    - ${item.descricao}: ${item.quantidade}x R$ ${item.precoUnitario.toFixed(2)} = R$ ${item.subtotal().toFixed(2)}`);
  }
  console.log(`    -> Total Bruto: R$ ${total.bruto.toFixed(2)}`);
  console.log(`    -> Desconto Aplicado (15% Strategy): R$ ${total.desconto.toFixed(2)}`);
  console.log(`    -> Total Líquido a Pagar: R$ ${total.liquido.toFixed(2)}`);

  // 5. Transições de Estado (State)
  console.log("\n[5] Evolução do Ciclo de Vida:");
  os.iniciarExecucao();
  console.log(`    Estado atual: ${os.estado.nome}`);

  os.concluir();
  console.log(`    Estado atual: ${os.estado.nome}`);

  // 6. Teste de Regra Bloqueante
  console.log("\n[6] Teste de Proteção de Regra (tentando reiniciar uma OS concluída):");
  try {
    os.iniciarExecucao();
  } catch (erro) {
    if (erro instanceof EstadoInvalidoErro) {
      console.log(`    [SUCESSO] Bloqueio confirmado: ${erro.message}`);
    }
  }

  // 7. Relatório da Auditoria
  console.log("\n[7] Relatório Final do Observer (Auditoria):");
  for (const reg of auditor.historico) {
    console.log(`    Transição: ${reg.de} -> ${reg.para} | Valor Final: R$ ${reg.valorLiquido.toFixed(2)}`);
  }

  console.log("\n" + "=".repeat(70));
  console.log(" Fim da Execução em TypeScript com Sucesso!");
  console.log("=".repeat(70));
}

executarDemonstracao();
