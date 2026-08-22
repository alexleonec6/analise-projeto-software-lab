# Análise e Projeto de Software - Na Prática (TypeScript)

[![TypeScript Tests](https://img.shields.io/badge/testes-7%20passando-brightgreen.svg)]()
[![Runtime](https://img.shields.io/badge/Node.js-v24%20(TS%20Nativo)-blue.svg)]()
[![Curso](https://img.shields.io/badge/Curso-IFRS%20%2F%20MEC-blue.svg)]()

Este repositório reúne um **resumo fácil de entender** e um **sistema completo em TypeScript** demonstrando na prática o que foi ensinado no curso de **Análise e Projeto de Software** (Aprenda Mais / MEC / IFRS).

---

## 💡 O Que Aprendemos no Curso? (Em Palavras Simples)

1. **Antes de codificar, planeje**:
   - Engenharia de software serve para não criar programas bagunçados que quebram facilmente.
   - Ouvir bem o cliente (Requisitos) evita fazer o sistema errado.
2. **Ciclos de vida**:
   - Podemos fazer tudo em fila reta (Cascata), desenhar rascunhos para mostrar rápido (Prototipação) ou entregar pequenas partes úteis aos poucos (Incremental).
3. **Orientação a Objetos e Padrões de Projeto**:
   - Dividir o código em peças independentes (peças de Lego). Se precisar mexer em uma peça, as outras continuam funcionando sem quebrar.

👉 **Quer ler o resumo completo e descomplicado?** Veja o arquivo [`RESUMO_CURSO.md`](./RESUMO_CURSO.md).  
👉 **Quer ver os desenhos da arquitetura?** Veja o arquivo [`docs/MODELAGEM.md`](./docs/MODELAGEM.md).

---

## 🛠️ O Projeto de Exemplo: Sistema de Ordens de Serviço (SGOS em TypeScript)

Para mostrar que a teoria funciona na prática, criamos um sistema simples e tipado de Ordem de Serviço de oficina/assistência técnica:

- **Cliente e Serviços (`src/entidades.ts`)**: Interfaces e classes tipadas com invariantes de domínio.
- **Descontos Flexíveis (`src/estrategiaDesconto.ts` - Padrão Strategy)**: O sistema calcula descontos facilmente (`SemDesconto`, `DescontoValorFixo`, `DescontoPercentual`) sem bagunçar a classe principal.
- **Controle de Fases (`src/estadosOS.ts` - Padrão State)**: Uma ordem começa como `CRIADA`, passa para `EM_EXECUCAO` e termina como `CONCLUIDA`. O sistema bloqueia ações ilegais (como tentar finalizar um serviço que nem começou).
- **Avisos Automáticos (`src/observadores.ts` - Padrão Observer)**: Toda vez que o status da ordem muda, o sistema avisa automaticamente o painel de log e o histórico de auditoria.

---

## 📁 Estrutura das Pastas

```
analise-projeto-software-lab/
├── docs/
│   └── MODELAGEM.md          # Desenhos do sistema (Casos de uso, classes e etapas)
├── src/
│   ├── index.ts              # Ponto de exportação dos módulos
│   ├── entidades.ts          # Cliente e Itens do serviço
│   ├── estadosOS.ts          # As fases da ordem (Criada, Em andamento, Concluída)
│   ├── estrategiaDesconto.ts # Regras de desconto (Strategy)
│   ├── observadores.ts       # Avisos e relatórios de histórico (Observer)
│   ├── ordemServico.ts       # Junta todas as peças em uma ordem de serviço
│   └── main.ts               # Demonstração interativa de execução
├── tests.ts                  # 7 testes automáticos usando o runner nativo do Node.js
├── package.json              # Configurações e scripts npm
├── RESUMO_CURSO.md           # Resumo do curso em linguagem fácil
└── README.md
```

---

## ▶️ Como Rodar no Computador

Você só precisa ter o **Node.js 22+ instalado** (ele roda os arquivos TypeScript diretamente, sem precisar de compilação manual nem instalar pacotes pesados).

1. **Ver a simulação funcionando**:
   ```bash
   npm start
   # ou: node --experimental-strip-types src/main.ts
   ```

2. **Rodar os testes automáticos**:
   ```bash
   npm test
   # ou: node --experimental-strip-types --test tests.ts
   ```

---

Feito por **Alexandre Souza** ([@alexleonec6](https://github.com/alexleonec6)).
