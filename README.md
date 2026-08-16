# Análise e Projeto de Software - Na Prática

[![Python Tests](https://img.shields.io/badge/testes-7%20passando-brightgreen.svg)]()
[![Curso](https://img.shields.io/badge/Curso-IFRS%20%2F%20MEC-blue.svg)]()

Este repositório reúne um **resumo fácil de entender** e um **pequeno sistema em Python** mostrando na prática o que foi ensinado no curso de **Análise e Projeto de Software** (Aprenda Mais / MEC / IFRS).

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

## 🛠️ O Projeto de Exemplo: Sistema de Ordens de Serviço (SGOS)

Para mostrar que a teoria funciona na prática, criamos um sistema simples de Ordem de Serviço de oficina/assistência técnica:

- **Cliente e Serviços**: Guarda quem pediu e quais serviços foram feitos.
- **Descontos Flexíveis (Padrão Strategy)**: O sistema calcula descontos facilmente (sem desconto, desconto fixo em dinheiro ou desconto em porcentagem) sem bagunçar a conta.
- **Controle de Fases (Padrão State)**: Uma ordem começa como `CRIADA`, passa para `EM_EXECUCAO` e termina como `CONCLUIDA`. O sistema bloqueia ações sem sentido (como tentar finalizar um serviço que nem começou).
- **Avisos Automáticos (Padrão Observer)**: Toda vez que o status da ordem muda, o sistema avisa automaticamente o painel de log e o histórico de auditoria.

---

## 📁 Estrutura das Pastas

```
analise-projeto-software-lab/
├── docs/
│   └── MODELAGEM.md          # Desenhos do sistema (Casos de uso, classes e etapas)
├── src/
│   ├── entidades.py          # Cliente e Itens do serviço
│   ├── estados_os.py         # As fases da ordem (Criada, Em andamento, Concluída)
│   ├── estrategia_desconto.py# Regras de desconto
│   ├── observadores.py       # Avisos e relatórios de histórico
│   └── ordem_servico.py      # Junta todas as peças em uma ordem de serviço
├── tests.py                  # 7 testes automáticos para provar que tudo funciona
├── main.py                   # Roda uma simulação no terminal
├── RESUMO_CURSO.md           # Resumo do curso em linguagem fácil
└── README.md
```

---

## ▶️ Como Rodar no Computador

Você só precisa ter o **Python instalado** (não precisa instalar nenhuma biblioteca extra).

1. **Ver a simulação funcionando**:
   ```bash
   python main.py
   ```

2. **Rodar os testes automáticos**:
   ```bash
   python -m unittest tests.py
   ```

---

Feito por **Alexandre Souza** ([@alexleonec6](https://github.com/alexleonec6)).
