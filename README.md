# Sistema de Gestão de Farmácia

[Link para o documento no Google Docs](https://docs.google.com/document/d/1j21Q1iR5Terk88ZYbzLt6Zancwbagf5PdOamMc9NCHM/edit?tab=t.0)

## Descrição

Este sistema foi desenvolvido para gerenciar informações de uma farmácia, incluindo a administração de funcionários, controle de estoque e cadastro de remédios. O objetivo é otimizar o fluxo de trabalho e assegurar a organização dos dados.

## Funcionalidades

- **Gerenciamento de Funcionários**: Cadastro e consulta de informações dos funcionários, incluindo cargo e salário.  
- **Controle de Estoque**: Registro de entradas, saídas e monitoramento das validades dos produtos.  
- **Cadastro de Remédios**: Registro de remédios com informações detalhadas, como tarja e validade.  

## Estrutura de Dados

### Entidades e Atributos

#### Funcionário
- `ID_Funcionário`: Identificador único do funcionário.  
- `Nome`: Nome completo do funcionário.  
- `Cargo`: Cargo ocupado na farmácia.  
- `Salário`: Salário do funcionário.  
- `Data_Salário`: Data de pagamento do salário.  

#### Estoque
- `Quantidade`: Quantidade de itens no estoque.  
- `Data_Validade`: Data de validade do produto.  
- `Data_Entrada_Estoque`: Data de entrada do produto no estoque.  
- `Unidade_Medida`: Unidade de medida do produto.  
- `Observações_Cuidado`: Informações adicionais de cuidado com o produto.  

#### Remédio
- `Nome`: Nome do remédio.  
- `Tarja`: Tipo de tarja do remédio (ex: vermelha, preta, etc.).  
- `Preço`: Preço do remédio.  
- `Validade`: Data de validade do remédio.  
- `ID_Remédio`: Identificador único do remédio.  
