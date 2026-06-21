# Sistema-de-Cadastro-de-Produtos---Python-MySQL
Sistema de cadastro e gerenciamento de produtos desenvolvido em Python com integração ao banco de dados MySQL. O projeto permite inserir, visualizar, atualizar e remover produtos utilizando operações CRUD, além de demonstrar conexão entre aplicação e banco de dados relacional



# Sistema de Cadastro de Produtos - Python + MySQL

Sistema de gerenciamento de produtos desenvolvido em Python com integração ao banco de dados MySQL.

O projeto tem como objetivo praticar conexão com banco de dados, comandos SQL e operações CRUD (Create, Read, Update e Delete).

## Funcionalidades

- Cadastrar produtos
- Listar produtos cadastrados
- Atualizar informações dos produtos
- Remover produtos
- Armazenar dados em banco MySQL

## Tecnologias utilizadas

- Python
- MySQL
- mysql-connector-python

## Estrutura do projeto

├── sistema_cadastro_produtos.py
├── database.sql
├── config_exemplo.py
└── README.md


## Banco de dados

Banco utilizado:
portfolio_db


Tabela criada:

database.sql:

é responsável por criar o banco de dados e a tabela utilizada pelo sistema.

Exemplo da estrutura criada:

-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS portfolio_db;

-- Usar banco criado
USE portfolio_db;


-- Criar tabela de produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Inserir alguns dados de teste
INSERT INTO produtos (nome, categoria, preco, quantidade)
VALUES
('Teclado Mecânico', 'Periféricos', 250.90, 10),
('Mouse Gamer', 'Periféricos', 120.50, 15),
('Monitor 24 Polegadas', 'Monitores', 899.99, 5);

## Produtos

Campos:

- id
- nome
- categoria
- preco
- quantidade
- data_cadastro

## Como executar

Execute o arquivo:
database.sql
no MySQL para criar o banco e a tabela.

Configurar conexão
No arquivo: sistema_cadastro_produtos.py

configure os dados do seu MySQL:
user="root"
password="SUA_SENHA"
database="portfolio_db"

## Executar o projeto

python sistema_cadastro_produtos.py

## Conceitos aplicados
Programação em Python
Integração Python com MySQL
Operações CRUD
Manipulação de dados
Comandos SQL
Banco de dados relacionais
Entrada e saída de informações
Objetivo

Projeto desenvolvido para praticar desenvolvimento em Python, SQL e criação de sistemas conectados a bancos de dados relacionais.
