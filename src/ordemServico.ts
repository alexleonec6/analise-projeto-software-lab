/**
 * Entidade Agregadora: OrdemServico.
 * Une os dados do pedido aos padrões State, Strategy e Observer.
 */

import { Cliente, ItemServico } from "./entidades.ts";
import { EstadoCriada, type IEstadoOS } from "./estadosOS.ts";
import { SemDesconto, type IPoliticaDesconto } from "./estrategiaDesconto.ts";
import type { IObservadorOS } from "./observadores.ts";

export interface IResumoFinanceiro {
  bruto: number;
  desconto: number;
  liquido: number;
}

export class OrdemServico {
  private readonly _id: string;
  private readonly _cliente: Cliente;
  private readonly _itens: ItemServico[] = [];
  private _estado: IEstadoOS;
  private _politicaDesconto: IPoliticaDesconto;
  private readonly _observadores: IObservadorOS[] = [];

  constructor(
    cliente: Cliente,
    politicaDesconto?: IPoliticaDesconto,
    idCustomizado?: string
  ) {
    this._id = idCustomizado || Math.random().toString(36).substring(2, 9).toUpperCase();
    this._cliente = cliente;
    this._estado = new EstadoCriada();
    this._politicaDesconto = politicaDesconto || new SemDesconto();
  }

  public get id(): string {
    return this._id;
  }

  public get cliente(): Cliente {
    return this._cliente;
  }

  public get estado(): IEstadoOS {
    return this._estado;
  }

  public get itens(): ReadonlyArray<ItemServico> {
    return this._itens;
  }

  public adicionarItem(item: ItemServico): void {
    if (this._estado.nome !== "CRIADA") {
      throw new Error(`Não é permitido alterar itens no estado: ${this._estado.nome}`);
    }
    this._itens.push(item);
  }

  public definirPoliticaDesconto(politica: IPoliticaDesconto): void {
    this._politicaDesconto = politica;
  }

  public inscreverObservador(observador: IObservadorOS): void {
    if (!this._observadores.includes(observador)) {
      this._observadores.push(observador);
    }
  }

  public mudarEstado(novoEstado: IEstadoOS): void {
    const anterior = this._estado.nome;
    this._estado = novoEstado;
    this.notificarObservadores(anterior, novoEstado.nome);
  }

  private notificarObservadores(anterior: string, novo: string): void {
    for (const obs of this._observadores) {
      obs.notificar(this, anterior, novo);
    }
  }

  public iniciarExecucao(): void {
    this._estado.iniciar(this);
  }

  public concluir(): void {
    this._estado.concluir(this);
  }

  public cancelar(): void {
    this._estado.cancelar(this);
  }

  public calcularTotal(): IResumoFinanceiro {
    const bruto = this._itens.reduce((acc, item) => acc + item.subtotal(), 0);
    const desconto = this._politicaDesconto.calcularDesconto(bruto);
    const liquido = Math.max(0, bruto - desconto);

    return {
      bruto: Number(bruto.toFixed(2)),
      desconto: Number(desconto.toFixed(2)),
      liquido: Number(liquido.toFixed(2)),
    };
  }
}
