# Documento de Engenharia de Software: Sistema de Gestão de Ordens de Serviço (SGOS)

Este documento reflete a aplicação prática dos conceitos teóricos ensinados no curso de **Análise e Projeto de Software** (MEC / Aprenda Mais / IFRS).

---

## 1. Engenharia de Requisitos

### 1.1 Atores Identificados
- **Cliente**: Entidade externa que solicita e acompanha o status de ordens de serviço.
- **Técnico / Operador**: Entidade externa responsável pela execução, transição de estados e faturamento dos serviços prestados.

### 1.2 Requisitos Funcionais (RF)
- `RF01`: O sistema deve permitir a criação de uma nova Ordem de Serviço associada a um Cliente e itens/serviços.
- `RF02`: O sistema deve calcular o valor total com aplicação de políticas de desconto (Padrão Strategy).
- `RF03`: O sistema deve gerenciar a transição estrita de estados da OS (`Criada` -> `EmExecucao` -> `Concluida` ou `Cancelada`).
- `RF04`: O sistema deve emitir eventos/notificações quando o estado de uma OS for alterado (Padrão Observer).
- `RF05`: O sistema deve manter persistência dos dados e rastreabilidade por identificador único.

### 1.3 Requisitos Não Funcionais (RNF)
- `RNF01`: **Desacoplamento**: As classes de negócio não devem depender diretamente de detalhes de persistência ou interface de saída.
- `RNF02`: **Extensibilidade**: Novas regras de desconto ou canais de notificação devem ser adicionáveis sem modificar o código existente (Princípio Aberto/Fechado).

---

## 2. Diagramas de Engenharia de Software

### 2.1 Diagrama de Casos de Uso (UML - Visão do Usuário)

```mermaid
flowchart LR
    Cliente["Ator: Cliente"]
    Tecnico["Ator: Técnico / Operador"]
    
    subgraph SGOS ["Sistema de Gestão de Ordens de Serviço"]
        UC1["Criar Ordem de Serviço"]
        UC2["Consultar Histórico de OS"]
        UC3["Transicionar Estado da OS"]
        UC4["Aplicar Desconto e Faturar"]
        UC5["Receber Alerta de Atualização"]
    end

    Cliente --> UC1
    Cliente --> UC2
    UC5 --> Cliente
    
    Tecnico --> UC3
    Tecnico --> UC4
    Tecnico --> UC2
```

---

### 2.2 Diagrama de Classes (UML - Visão Estrutural)

```mermaid
classDiagram
    class Cliente {
        +str id
        +str nome
        +str email
    }

    class ItemServico {
        +str descricao
        +float preco_unitario
        +int quantidade
        +subtotal() float
    }

    class IPoliticaDesconto {
        <<interface>>
        +calcular_desconto(valor_bruto: float) float
    }

    class DescontoPadrao {
        +calcular_desconto(valor_bruto: float) float
    }

    class DescontoFidelidade {
        +calcular_desconto(valor_bruto: float) float
    }

    class IObservadorOS {
        <<interface>>
        +ao_mudar_estado(os: OrdemServico, estado_anterior: str) void
    }

    class NotificadorConsole {
        +ao_mudar_estado(os: OrdemServico, estado_anterior: str) void
    }

    class IEstadoOS {
        <<interface>>
        +iniciar(os: OrdemServico) void
        +concluir(os: OrdemServico) void
        +cancelar(os: OrdemServico) void
    }

    class EstadoCriada {
        +iniciar(os: OrdemServico) void
        +cancelar(os: OrdemServico) void
    }

    class EstadoEmExecucao {
        +concluir(os: OrdemServico) void
        +cancelar(os: OrdemServico) void
    }

    class EstadoConcluida {
    }

    class EstadoCancelada {
    }

    class OrdemServico {
        +str id
        +Cliente cliente
        +List~ItemServico~ itens
        +IEstadoOS estado
        +IPoliticaDesconto politica_desconto
        +adicionar_item(item: ItemServico) void
        +definir_politica_desconto(politica: IPoliticaDesconto) void
        +inscrever_observador(obs: IObservadorOS) void
        +calcular_total() float
        +iniciar() void
        +concluir() void
        +cancelar() void
    }

    IPoliticaDesconto <|.. DescontoPadrao
    IPoliticaDesconto <|.. DescontoFidelidade
    IObservadorOS <|.. NotificadorConsole
    IEstadoOS <|.. EstadoCriada
    IEstadoOS <|.. EstadoEmExecucao
    IEstadoOS <|.. EstadoConcluida
    IEstadoOS <|.. EstadoCancelada

    OrdemServico o-- Cliente
    OrdemServico *-- ItemServico
    OrdemServico o-- IEstadoOS
    OrdemServico o-- IPoliticaDesconto
    OrdemServico o-- IObservadorOS
```

---

### 2.3 Diagrama de Transição de Estados (DTE / State Machine)

```mermaid
stateDiagram-v2
    [*] --> Criada: Criar OS
    Criada --> EmExecucao: iniciar_execucao()
    Criada --> Cancelada: cancelar()
    EmExecucao --> Concluida: concluir_servico()
    EmExecucao --> Cancelada: cancelar()
    Concluida --> [*]
    Cancelada --> [*]
```

---

### 2.4 Diagrama Entidade-Relacionamento (DER / Dicionário de Dados)

```mermaid
erDiagram
    CLIENTE ||--o{ ORDEM_SERVICO : solicita
    ORDEM_SERVICO ||--|{ ITEM_SERVICO : contem
    ORDEM_SERVICO ||--|| HISTORICO_ESTADO : registra

    CLIENTE {
        string id PK
        string nome
        string email
    }

    ORDEM_SERVICO {
        string id PK
        string cliente_id FK
        string estado_atual
        float valor_bruto
        float valor_desconto
        float valor_liquido
        datetime data_criacao
    }

    ITEM_SERVICO {
        string id PK
        string os_id FK
        string descricao
        float preco_unitario
        int quantidade
    }

    HISTORICO_ESTADO {
        string id PK
        string os_id FK
        string estado_anterior
        string estado_novo
        datetime timestamp
    }
```
