/**
 * Entidades do Domínio de Negócio.
 * Representam os dados essenciais da aplicação de forma tipada e segura.
 */

export interface ICliente {
  readonly id: string;
  readonly nome: string;
  readonly email: string;
}

export class Cliente implements ICliente {
  readonly id: string;
  readonly nome: string;
  readonly email: string;

  constructor(id: string, nome: string, email: string) {
    this.id = id;
    this.nome = nome;
    this.email = email;
  }
}

export interface IItemServico {
  readonly id: string;
  readonly descricao: string;
  readonly precoUnitario: number;
  readonly quantidade: number;
  subtotal(): number;
}

export class ItemServico implements IItemServico {
  readonly id: string;
  readonly descricao: string;
  readonly precoUnitario: number;
  readonly quantidade: number;

  constructor(descricao: string, precoUnitario: number, quantidade: number = 1, idCustomizado?: string) {
    if (precoUnitario < 0 || quantidade < 1) {
      throw new Error("Preço unitário ou quantidade inválida.");
    }
    this.descricao = descricao;
    this.precoUnitario = precoUnitario;
    this.quantidade = quantidade;
    this.id = idCustomizado || Math.random().toString(36).substring(2, 9);
  }

  subtotal(): number {
    return Number((this.precoUnitario * this.quantidade).toFixed(2));
  }
}
