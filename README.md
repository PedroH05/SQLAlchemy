# Integração com Banco de Dados usando SQLAlchemy

Projeto desenvolvido com foco em estudo de integração entre aplicações Python e banco de dados utilizando SQLAlchemy, explorando tanto:

- SQLAlchemy Core (queries SQL diretas via Python)

- SQLAlchemy ORM (mapeamento objeto-relacional)

O objetivo foi consolidar conceitos fundamentais para desenvolvimento backend envolvendo persistência de dados, modelagem relacional e manipulação de consultas.

---

# Tecnologias utilizadas

- Python 3

- SQLAlchemy (Core e ORM)

- SQLite (banco em memória)

- PyCharm

---

# 📚 Conceitos trabalhados

Durante o desenvolvimento foram praticados:

- SQLAlchemy Core

- Criação de tabelas via metadata

- Definição de chaves primárias e estrangeiras

- Execução de queries SQL diretamente via Python

- Inserção de dados usando parâmetros

- Execução de SELECT e leitura de resultados

- Inspeção de estrutura do banco

- SQLAlchemy ORM

- Mapeamento objeto-relacional com classes Python

- Relacionamento entre tabelas (relationship)

- Persistência de objetos via Session

- Queries com filtros (WHERE, IN)

- Ordenação crescente e decrescente

- JOIN entre tabelas

- Agregações com funções SQL (COUNT)

- Navegação entre entidades relacionadas

- Estrutura das entidades
- User / UserAccount

# Representa usuários da aplicação:

- ID

- Nome

- Nome completo

- Relacionamento com endereços

# Address

Tabela relacionada a usuários:

- Email

- Chave estrangeira para usuário

# User Preferences (Core)

Tabela adicional utilizada na parte Core para:

- Preferências de usuário

- Configurações associadas
