/**
 * Padrão Strategy (Estratégia).
 * Permite trocar a regra de cálculo de desconto sem mexer no restante do código.
 */

export interface IPoliticaDesconto {
  calcularDesconto(valorBruto: number): number;
}

export class SemDesconto implements IPoliticaDesconto {
  calcularDesconto(_valorBruto: number): number {
    return 0.0;
  }
}

export class DescontoValorFixo implements IPoliticaDesconto {
  private readonly valorFixo: number;

  constructor(valorFixo: number) {
    if (valorFixo < 0) {
      throw new Error("Valor de desconto não pode ser negativo.");
    }
    this.valorFixo = valorFixo;
  }

  calcularDesconto(valorBruto: number): number {
    const desconto = Math.min(valorBruto, this.valorFixo);
    return Number(desconto.toFixed(2));
  }
}

export class DescontoPercentual implements IPoliticaDesconto {
  private readonly taxa: number;

  constructor(taxaPercentual: number) {
    if (taxaPercentual < 0 || taxaPercentual > 100) {
      throw new Error("Percentual de desconto deve estar entre 0 e 100.");
    }
    this.taxa = taxaPercentual / 100.0;
  }

  calcularDesconto(valorBruto: number): number {
    return Number((valorBruto * this.taxa).toFixed(2));
  }
}
