/**
 * Padrão State (Estado).
 * Controla os estados de uma Ordem de Serviço e impede transições inválidas.
 */

import type { OrdemServico } from "./ordemServico.ts";

export class EstadoInvalidoErro extends Error {
  constructor(mensagem: string) {
    super(mensagem);
    this.name = "EstadoInvalidoErro";
  }
}

export interface IEstadoOS {
  readonly nome: string;
  iniciar(os: OrdemServico): void;
  concluir(os: OrdemServico): void;
  cancelar(os: OrdemServico): void;
}

export abstract class EstadoBase implements IEstadoOS {
  public abstract readonly nome: string;

  public iniciar(_os: OrdemServico): void {
    throw new EstadoInvalidoErro(`Transição inválida: Não é possível iniciar a partir de '${this.nome}'.`);
  }

  public concluir(_os: OrdemServico): void {
    throw new EstadoInvalidoErro(`Transição inválida: Não é possível concluir a partir de '${this.nome}'.`);
  }

  public cancelar(_os: OrdemServico): void {
    throw new EstadoInvalidoErro(`Transição inválida: Não é possível cancelar a partir de '${this.nome}'.`);
  }
}

export class EstadoCriada extends EstadoBase {
  public readonly nome = "CRIADA";

  public override iniciar(os: OrdemServico): void {
    os.mudarEstado(new EstadoEmExecucao());
  }

  public override cancelar(os: OrdemServico): void {
    os.mudarEstado(new EstadoCancelada());
  }
}

export class EstadoEmExecucao extends EstadoBase {
  public readonly nome = "EM_EXECUCAO";

  public override concluir(os: OrdemServico): void {
    os.mudarEstado(new EstadoConcluida());
  }

  public override cancelar(os: OrdemServico): void {
    os.mudarEstado(new EstadoCancelada());
  }
}

export class EstadoConcluida extends EstadoBase {
  public readonly nome = "CONCLUIDA";
}

export class EstadoCancelada extends EstadoBase {
  public readonly nome = "CANCELADA";
}
