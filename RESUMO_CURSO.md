# Resumo do Curso: Análise e Projeto de Software (IFRS / Aprenda Mais - MEC)

## 1. Módulo 1: Bases Tecnológicas e Prototipação

### 1.1 Histórico e Evolução da Engenharia de Software
- **Origem**: Conceito cunhado por Friedrich Ludwig Bauer na década de 1960 e oficializado na Conferência da OTAN (1968).
- **Definição**: Aplicação prática de princípios científicos e tecnológicos de engenharia para produzir software confiável, eficiente e de fácil manutenção.
- **Engenharia em Camadas**:
  1. **Foco na Qualidade**: Alicerce de todo processo de software.
  2. **Processos**: Estrutura de atividades que conecta métodos e ferramentas.
  3. **Métodos**: Técnicas operacionais para análise de requisitos, projeto, codificação, testes e validação.
  4. **Ferramentas**: Apoio automatizado ou semiautomatizado (CASE - Computer-Aided Software Engineering).

### 1.2 Papel e Características do Software
- **Software como Produto**: Disponibiliza capacidade de computação e manipulação/armazenamento de dados.
- **Software como Veículo**: Plataforma de suporte para execução e criação de outras aplicações (Sistemas Operacionais, redes, ferramentas CASE).
- **Características**: Software é desenvolvido (engenharia lógica), não manufaturado fisicamente; não se desgasta com atrito mecânico, mas deteriora conforme requisitos e ambientes evoluem sem refatoração adequada.

### 1.3 Ciclos de Vida e Modelos de Processo
- **Modelo Tradicional (Cascata)**: Abordagem sequencial rígida (Comunicação -> Planejamento -> Modelagem -> Construção -> Implantação). Cada fase precisa estar concluída e validada antes da próxima.
- **Modelo Prototipação**: Foco em atender o cliente de forma gradual quando requisitos são incertos.
  - *Tipos*: Ilustrativo (telas), Simulado (fluxo de persistência mockado), Funcional (subconjunto real), Evolucionário (base que cresce iterativamente).
  - *Desafios*: Expectativas irreais do usuário (confundir protótipo com produto final), código de arquitetura frágil e falta de visibilidade do progresso real.
- **Modelo Incremental**: Combina a linearidade do tradicional com a entrega modular de software utilizável em cada versão ("core" funcional entregue primeiro).

### 1.4 Engenharia de Requisitos
- **5 Passos Fundamentais (Sommerville)**:
  1. Elicitação/Obtenção de requisitos (técnicas como FAST - Facilitated Application Specification Techniques e QFD).
  2. Análise e Negociação.
  3. Especificação (documentação dos requisitos).
  4. Modelagem do Sistema.
  5. Validação de Requisitos.

---

## 2. Módulo 2: Análise, Análise Orientada e Projeto

### 2.1 Análise Estruturada
- **Dicionário de Dados**: Catálogo central de todas as definições de fluxo e dados.
- **DFD (Diagrama de Fluxo de Dados)**: Representação de processos funcionais, depósitos de dados e entidades externas.
- **DER (Diagrama Entidade-Relacionamento)**: Mapeamento de objetos de dados, atributos descritivos e relacionamentos (com cardinalidade e modalidade).
- **DTE (Diagrama de Transição de Estados)**: Modela o comportamento temporal e reativo sob gatilhos/eventos.

### 2.2 Análise e Projeto Orientado a Objetos (OOA / OOD)
- **Princípios Nucleares**:
  - *Encapsulamento*: Agrupamento de dados e operações, com ocultação de dados internos via interfaces limpas.
  - *Herança*: Criação de tipos especializados preservando contratos da classe base.
  - *Polimorfismo*: Tratamento uniforme de diferentes implementações sob uma mesma assinatura de método.
  - *Desacoplamento*: Minimização de dependências entre módulos para evitar efeitos colaterais na manutenção.
- **Modelagem UML (Unified Modeling Language)**:
  - *Visão do Usuário*: Casos de Uso e Atores (quem interage externa e diretamente com o sistema).
  - *Visão Estrutural*: Diagramas de Classes e Objetos.
  - *Visão Comportamental*: Diagramas de Sequência e Atividades (interações dinâmicas entre elementos).
  - *Visão de Implementação e Ambiente*: Componentes físicos e nós de implantação.
- **Design Patterns (Padrões de Projeto)**:
  - Soluções comprovadas para problemas arquiteturais recorrentes na OOD.
  - Foco central na reutilização de decisões de projeto estruturadas, e não apenas código bruto.
