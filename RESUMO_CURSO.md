# Resumo Descomplicado do Curso: Análise e Projeto de Software

Um guia direto ao ponto, sem enrolação e em linguagem simples, sobre o que foi ensinado no curso da plataforma Aprenda Mais (MEC / IFRS).

---

## 🧭 Módulo 1: O Que É Engenharia de Software e Como Começar?

### 1. O que é Engenharia de Software?
Não é apenas sentar e sair digitando código no computador. É planejar, construir e cuidar do programa usando métodos organizados para que ele não quebre nem vire uma dor de cabeça no futuro.
- **A base é a qualidade**: Tudo é feito pensando em entregar algo que funcione direito para o cliente.
- **Ferramentas CASE**: São programas que ajudam os programadores a desenhar telas, bancos de dados e planejar o sistema antes de programar.

### 2. O software não quebra como uma máquina física
Uma peça de carro quebra por desgaste e ferrugem. O software não gasta com o tempo, mas ele fica ruim e defasado se as necessidades mudarem e ninguém atualizar o código com cuidado.

### 3. As formas de tocar um projeto (Ciclos de Vida)
- **Modelo Tradicional (Cascata)**: Você só começa a próxima etapa quando a anterior estiver 100% pronta e aprovada (Levanta o que o cliente quer -> Desenha -> Programa -> Testa -> Entrega). É rígido e difícil de mudar no meio do caminho.
- **Modelo de Prototipagem**: Faz telas de rascunho (protótipos) para mostrar ao cliente antes de fazer o sistema real. Ajuda o cliente a ver o que quer, mas tem o perigo dele achar que o rascunho já é o sistema final.
- **Modelo Incremental**: Entrega o sistema aos poucos em pedaços úteis. Primeiro entrega o básico que já funciona e vai adicionando novas funções a cada versão.

### 4. Engenharia de Requisitos: Ouvindo o que o cliente precisa
É a fase de conversa e entendimento. Se você entender errado o que o cliente quer, vai programar a coisa errada:
1. **Perguntar e ouvir** o que ele precisa (usando reuniões guiadas).
2. **Organizar e negociar** o que dá para fazer.
3. **Anotar tudo** em um documento claro.
4. **Validar** com o cliente para ter certeza de que é aquilo mesmo.

---

## 🧱 Módulo 2: Desenhando e Estruturando o Software

### 1. Análise Estruturada: Os Diagramas Clássicos
Antes de programar, usamos desenhos simples para entender o fluxo:
- **DFD (Fluxo de Dados)**: Mostra para onde as informações vão (ex: cliente digita os dados -> sistema processa -> salva no banco).
- **DER (Entidade-Relacionamento)**: Mostra como as tabelas do banco conversam entre si (ex: um Cliente tem vários Pedidos).
- **DTE (Transição de Estados)**: Mostra as fases de algo no sistema (ex: Pedido Criado -> Em Andamento -> Entregue ou Cancelado).

### 2. Orientação a Objetos: Pensando no Mundo Real
Em vez de deixar variáveis e funções soltas, nós criamos "Objetos" que representam coisas do mundo real (como um Cliente ou uma Ordem de Serviço):
- **Encapsulamento**: Esconder os detalhes internos e só deixar mexer pelo jeito certo (como o painel de um carro: você pisa no acelerador e não precisa saber como o motor injeta gasolina).
- **Desacoplamento**: Fazer as partes do sistema funcionarem de forma independente. Se você mudar a tela de pagamento, isso não deve quebrar a tela de cadastro.
- **Polimorfismo**: Tratar coisas parecidas com a mesma regra básica (ex: tanto desconto em dinheiro quanto desconto em porcentagem são tipos de "Desconto").

### 3. Padrões de Projeto (Design Patterns): Soluções Prontas para Problemas Comuns
São receitas de bolo consagradas criadas por programadores experientes:
- **Strategy (Estratégia)**: Permite trocar a fórmula de cálculo sem mexer no resto do programa (usamos no projeto para escolher entre não dar desconto, dar desconto em reais ou desconto em %).
- **State (Estado)**: Controla em qual situação algo está sem encher o código de `if/else` confusos (garante que uma ordem concluída não possa ser cancelada do nada).
- **Observer (Observador)**: Faz o sistema avisar automaticamente outras partes quando algo importante acontece (ex: a ordem mudou de status -> o sistema avisa a auditoria e manda uma mensagem no terminal).
