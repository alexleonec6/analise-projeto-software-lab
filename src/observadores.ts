/**
 * Padrão Observer (Observador).
 * Dispara notificações automáticas toda vez que o estado da OS é alterado.
 */

import type { OrdemServico } from "./ordemServico.ts";

export interface IObservadorOS {
  notificar(os: OrdemServico, estadoAnterior: string, estadoNovo: string): void;
}

export class NotificadorLogConsole implements IObservadorOS {
  public notificar(os: OrdemServico, estadoAnterior: string, estadoNovo: string): void {
    console.log(
      `[OBSERVER: LOG] OS #${os.id} | Cliente: ${os.cliente.nome} | Transição: [${estadoAnterior}] -> [${estadoNovo}]`
    );
  }
}

export interface IRegistroAuditoria {
  osId: string;
  cliente: string;
  de: string;
  para: string;
  valorLiquido: number;
}

export class AuditoriaEventos implements IObservadorOS {
  public readonly historico: IRegistroAuditoria[] = [];

  public notificar(os: OrdemServico, estadoAnterior: string, estadoNovo: string): void {
    this.historico.push({
      osId: os.id,
      cliente: os.cliente.nome,
      de: estadoAnterior,
      para: estadoNovo,
      valorLiquido: os.calcularTotal().liquido,
    });
  }
}
