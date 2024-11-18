# Sistema de Gestão de Farmácia

[Link para o documento no Google Docs](https://docs.google.com/document/d/1j21Q1iR5Terk88ZYbzLt6Zancwbagf5PdOamMc9NCHM/edit?tab=t.0)

## Descrição

Este sistema foi desenvolvido para gerenciar informações de uma farmácia, incluindo o controle de fornecedores, estoque e cadastro de remédios. O objetivo é otimizar o fluxo de trabalho e assegurar a organização dos dados.

## Funcionalidades

- **Gerenciamento de Fornecedores**: Cadastro e consulta de informações dos fornecedores que abastecem a farmácia.
- **Controle de Estoque**: Registro de entradas, saídas e monitoramento das validades dos produtos.  
- **Cadastro de Remédios**: Registro de remédios com informações detalhadas, como tarja e validade.

## Detalhamento e modularização dos arquivos

### `remedio.py`

Este arquivo contém toda a lógica para manipular os dados do estoque de remédios. Ele inclui funções para carregar, salvar, adicionar, atualizar e deletar remédios.

#### Principais Funções

- **`load_remedios()`**  
  Carrega os dados do arquivo `estoque_remedios.csv` em um DataFrame. Se o arquivo não existir, cria um DataFrame vazio.

- **`save_remedios(df)`**  
  Salva o DataFrame atualizado no arquivo CSV.

- **`add_remedio(remedio: RemedioRequest)`**  
  Adiciona um novo remédio ao estoque, verificando se o `id` ou os dados já existem.

- **`update_remedio(id: str, remedio: RemedioRequest)`**  
  Atualiza as informações de um remédio existente com base no `id`.

- **`delete_remedio(id: str)`**  
  Remove um remédio do estoque com base no `id`.

- **Outras Funções**  
  Funções para obter a quantidade de remédios, compactar os dados em um arquivo zip e calcular o hash do arquivo CSV.

### `main.py`

Este arquivo define os endpoints da API. Ele utiliza as funções de `remedio.py` para realizar as operações de CRUD e outras funcionalidades.

#### Principais Endpoints

- **`POST /remedios`**  
  Adiciona um novo remédio ao estoque.

- **`GET /remedios`**  
  Retorna todos os remédios cadastrados.

- **`PUT /remedios/{id}`**  
  Atualiza as informações de um remédio existente.

- **`DELETE /remedios/{id}`**  
  Remove um remédio do estoque.

- **`GET /remedios/quantidade`**  
  Retorna a quantidade total de remédios cadastrados.

- **`GET /remedios/compactar`**  
  Gera e retorna um arquivo zip contendo o arquivo CSV do estoque.

- **`GET /remedios/hash`**  
  Retorna o hash SHA256 do arquivo CSV para verificação de integridade.

- **`GET /`**  
  Endpoint raiz que retorna uma mensagem de funcionamento da API.

## Criando o ambiente e testando a aplicação

1. Certifique-se de ter Python instalado:
   ```bash
   python --version
   
2. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   

3. Crie o ambiente virtual: No terminal, navegue até o diretório onde você deseja criar o ambiente virtual e execute:
   ```bash
   python -m venv nome_do_ambiente

4. Ativando o ambiente virtual (Windows):
   ```bash
   nome_do_ambiente\Scripts\activate

5. Ativando o ambiente virtual (Linux/Mac):
   ```bash
   source nome_do_ambiente/bin/activate

6. Instalar as depencias:
   ```bash
   pip install -r requirements.txt

7. Execultar a aplicação:
   ```bash
   uvicorn main:app --reload

## Estrutura de Dados

### Entidades e Atributos

#### Remédio
- `id`: Identificador único do remédio.
- `nome`: Nome do remédio.  
- `tarja`: Tipo de tarja do remédio (ex: vermelha, preta, etc.).  
- `preço`: Preço do remédio.  
- `validade`: Data de validade do remédio.  
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
        "id": "1",
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
        "id": "1",
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
### Python
Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
### Postman

Para testar os endpoints, recomendamos o uso do [Postman](https://www.postman.com/), que facilita a realização de requisições HTTP.
