# Sistema de Gestão de Farmácia

[Link para o documento no Google Docs](https://docs.google.com/document/d/1j21Q1iR5Terk88ZYbzLt6Zancwbagf5PdOamMc9NCHM/edit?tab=t.0)

## Descrição

Este sistema foi desenvolvido para gerenciar informações de uma farmácia, incluindo o controle de fornecedores, estoque e cadastro de remédios. O objetivo é otimizar o fluxo de trabalho e assegurar a organização dos dados.

## Funcionalidades

- **Gerenciamento de Fornecedores**: Cadastro e consulta de informações dos fornecedores que abastecem a farmácia.
- **Controle de Estoque**: Registro de entradas, saídas e monitoramento das validades dos produtos.  
- **Cadastro de Remédios**: Registro de remédios com informações detalhadas, como tarja e validade.  

## Estrutura de Dados

### Entidades e Atributos

#### Fornecedor
- `ID_Fornecedor`: Identificador único do fornecedor. 
- `nome_fornecedor`: Nome do fornecedor.
- `contato`: Informações de contato do fornecedor.  
- `endereço`: Localização do fornecedor.  
- `Tipo_Produto`: Tipo de produto fornecido (ex.: remédios, equipamentos médicos, etc.).

#### Estoque
- `id_do_remedio`: Informações adicionais de cuidado com o produto.
- `Quantidade`: Quantidade de itens no estoque.  
- `Data_Validade`: Data de validade do produto.  
- `Data_Entrada_Estoque`: Data de entrada do produto no estoque.  
- `Unidade_Medida`: Unidade de medida do produto.  
  

#### Remédio
- `Nome`: Nome do remédio.  
- `Tarja`: Tipo de tarja do remédio (ex: vermelha, preta, etc.).  
- `Preço`: Preço do remédio.  
- `Validade`: Data de validade do remédio.  
- `ID_Remédio`: Identificador único do remédio.

---

# API de Controle de Estoque de Remédios

Este projeto é uma API simples desenvolvida com FastAPI para gerenciar o estoque de remédios. A API permite adicionar, listar, atualizar e deletar remédios, utilizando um arquivo CSV como base de dados.

## Inicialização do Servidor

1. Certifique-se de que você tem o Python e o FastAPI instalados.
2. No terminal, execute o seguinte comando para iniciar o servidor:

    ```bash
    uvicorn main:app --reload
    ```

3. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Endpoints Disponíveis

### Base URL

`http://127.0.0.1:8000`

### **1. Inserir Remédio (`POST /remedios`)**

Adiciona um novo remédio ao estoque.

- **URL:** `POST /remedios`
- **Body (raw, JSON):**

    ```json
    {
        "id_remedio": "001",
        "nome": "Paracetamol",
        "tarja": "Branca",
        "preco": 10.5,
        "validade": "2025-12-31"
    }
    ```

### **2. Listar Todos os Remédios (`GET /remedios`)**

Retorna todos os remédios cadastrados.

- **URL:** `GET /remedios`

### **3. Atualizar um Remédio (`PUT /remedios/{id_remedio}`)**

Atualiza as informações de um remédio existente.

- **URL:** `PUT /remedios/{id_remedio}`

- **Body (raw, JSON):**

    ```json
    {
        "id_": "001",
        "nome": "Paracetamol",
        "tarja": "Vermelha",
        "preco": 12.0,
        "validade": "2026-01-01"
    }
    ```

### **4. Deletar um Remédio (`DELETE /remedios/{id_remedio}`)**

Remove um remédio do estoque.

- **URL:** `DELETE /remedios/{id_remedio}`

---

## Ferramentas Recomendadas

### Postman

Para testar os endpoints, recomendamos o uso do [Postman](https://www.postman.com/), que facilita a realização de requisições HTTP.
