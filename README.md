# Análise e Projeto de Software - Laboratório & Implementação

[![Python Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen.svg)]()
[![Course](https://img.shields.io/badge/Course-IFRS%20%2F%20MEC-blue.svg)]()
[![Architecture](https://img.shields.io/badge/Pattern-State%20%7C%20Strategy%20%7C%20Observer-orange.svg)]()

Repositório prático contendo o **resumo conceitual completo** e uma **implementação de referência** cobrindo todos os módulos da formação **Análise e Projeto de Software** (Turma 2026B — Rede e-Tec Brasil / IFRS / Aprenda Mais - MEC).

---

## 📚 Conteúdo do Curso

O curso é estruturado em dois eixos fundamentais:

1. **Módulo 1: Bases Tecnológicas e Prototipação**
   - Evolução histórica da Engenharia de Software (F. L. Bauer, 1968, Conferência da OTAN).
   - Engenharia em camadas (Foco na qualidade, Processos, Métodos, Ferramentas CASE).
   - Ciclos de Vida (Tradicional / Cascata, Prototipação, Incremental / Evolucionário).
   - Engenharia de Requisitos (FAST, QFD, Elicitação, Modelagem e Validação).
2. **Módulo 2: Análise, Análise Orientada e Projeto**
   - Análise Estruturada (Dicionário de Dados, DFD, DER, Diagrama de Transição de Estados).
   - Análise Orientada a Objetos (OOA) e Projeto (OOD) com UML (Casos de Uso, Diagrama de Classes).
   - Padrões de Projeto (*Design Patterns*) e desacoplamento de software.

👉 O resumo teórico detalhado está disponível em: [`RESUMO_CURSO.md`](./RESUMO_CURSO.md).  
👉 A documentação de requisitos e diagramas UML/DER/DTE está em: [`docs/MODELAGEM.md`](./docs/MODELAGEM.md).

---

## 🛠️ O Projeto de Referência: SGOS (Sistema de Gestão de Ordens de Serviço)

O projeto implementa um sistema enxuto e desacoplado que sintetiza os tópicos de modelagem e design patterns estudados:

- **Domínio & Encapsulamento**: `Cliente` e `ItemServico` com invariantes de negócio.
- **Padrão Strategy**: Cálculo de descontos flexíveis (`SemDesconto`, `DescontoValorFixo`, `DescontoPercentual`) sem acoplar a classe de pedido.
- **Padrão State**: Ciclo de vida com máquina de estados finita (`CRIADA` -> `EM_EXECUCAO` -> `CONCLUIDA` / `CANCELADA`), prevenindo transições ilegais.
- **Padrão Observer**: Disparo desacoplado de eventos de mudança de estado para logs de console e trilha de auditoria.

### 📐 Arquitetura

```
analise-projeto-software-lab/
├── docs/
│   └── MODELAGEM.md          # Especificação de Requisitos, Casos de Uso, Diagrama de Classes e DTE
├── src/
│   ├── __init__.py
│   ├── entidades.py          # Entidades do Domínio (Cliente, ItemServico)
│   ├── estados_os.py         # Padrão State (Ciclo de Vida da OS)
│   ├── estrategia_desconto.py# Padrão Strategy (Políticas de Desconto)
│   ├── observadores.py       # Padrão Observer (Logs e Auditoria)
│   └── ordem_servico.py      # Agregador Central da Ordem de Serviço
├── tests.py                  # Bateria de Testes Unitários Automatizados (7 testes)
├── main.py                   # Execução interativa demonstrativa
├── RESUMO_CURSO.md           # Resumo completo dos tópicos do curso MEC/IFRS
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10+ (sem dependências externas; utiliza a biblioteca padrão).

### Executar a Demonstração
```bash
python main.py
```

### Executar os Testes Unitários
```bash
python -m unittest tests.py
```

---

## 📝 Licença
Desenvolvido por **Alexandre Souza** ([@alexleonec6](https://github.com/alexleonec6)).  
Distribuído sob a licença MIT.
