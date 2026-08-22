/**
 * Testes Unitários Automatizados em TypeScript.
 * Roda nativamente no test runner do Node.js (node:test e node:assert).
 */

import test from "node:test";
import assert from "node:assert/strict";

import { Cliente, ItemServico } from "./src/entidades.ts";
import { SemDesconto, DescontoValorFixo, DescontoPercentual } from "./src/estrategiaDesconto.ts";
import { EstadoInvalidoErro } from "./src/estadosOS.ts";
import { AuditoriaEventos } from "./src/observadores.ts";
import { OrdemServico } from "./src/ordemServico.ts";

const clienteTeste = new Cliente("CLI-T1", "Cliente Teste", "teste@lab.com");

test("ItemServico: deve calcular subtotal corretamente", () => {
  const item = new ItemServico("Serviço Teste", 150.0, 3);
  assert.equal(item.subtotal(), 450.0);
});

test("Strategy: SemDesconto não deve abater valor", () => {
  const os = new OrdemServico(clienteTeste, new SemDesconto());
  os.adicionarItem(new ItemServico("Serviço A", 200.0, 1));
  const total = os.calcularTotal();

  assert.equal(total.bruto, 200.0);
  assert.equal(total.desconto, 0.0);
  assert.equal(total.liquido, 200.0);
});

test("Strategy: DescontoPercentual deve abater porcentagem exata", () => {
  const os = new OrdemServico(clienteTeste, new DescontoPercentual(10));
  os.adicionarItem(new ItemServico("Serviço B", 500.0, 1));
  const total = os.calcularTotal();

  assert.equal(total.bruto, 500.0);
  assert.equal(total.desconto, 50.0);
  assert.equal(total.liquido, 450.0);
});

test("Strategy: DescontoValorFixo deve abater valor monetário", () => {
  const os = new OrdemServico(clienteTeste, new DescontoValorFixo(75));
  os.adicionarItem(new ItemServico("Serviço C", 300.0, 1));
  const total = os.calcularTotal();

  assert.equal(total.desconto, 75.0);
  assert.equal(total.liquido, 225.0);
});

test("State: deve seguir o fluxo CRIADA -> EM_EXECUCAO -> CONCLUIDA", () => {
  const os = new OrdemServico(clienteTeste);
  assert.equal(os.estado.nome, "CRIADA");

  os.iniciarExecucao();
  assert.equal(os.estado.nome, "EM_EXECUCAO");

  os.concluir();
  assert.equal(os.estado.nome, "CONCLUIDA");
});

test("State: transição ilegal deve disparar EstadoInvalidoErro", () => {
  const os = new OrdemServico(clienteTeste);
  // Não pode concluir sem iniciar
  assert.throws(() => os.concluir(), EstadoInvalidoErro);
});

test("Observer: deve ser notificado e registrar histórico", () => {
  const os = new OrdemServico(clienteTeste);
  const auditor = new AuditoriaEventos();
  os.inscreverObservador(auditor);

  os.adicionarItem(new ItemServico("Serviço X", 100.0, 1));
  os.iniciarExecucao();
  os.concluir();

  assert.equal(auditor.historico.length, 2);
  assert.equal(auditor.historico[0].de, "CRIADA");
  assert.equal(auditor.historico[0].para, "EM_EXECUCAO");
  assert.equal(auditor.historico[1].de, "EM_EXECUCAO");
  assert.equal(auditor.historico[1].para, "CONCLUIDA");
});
