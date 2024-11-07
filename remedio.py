from fastapi import FastAPI
from pydantic import BaseModel
import csv
import os

# Definindo a classe do Remédio
class Remedio:
    def __init__(self, nome, tarja, preco, validade, id_remedio):
        self.nome = nome
        self.tarja = tarja
        self.preco = preco
        self.validade = validade
        self.id_remedio = id_remedio

    def to_dict(self):
        return {
            "nome": self.nome,
            "tarja": self.tarja,
            "preco": self.preco,
            "validade": self.validade,
            "id_remedio": self.id_remedio
        }

    @staticmethod
    def from_dict(data):
        return Remedio(
            nome=data['nome'],
            tarja=data['tarja'],
            preco=data['preco'],
            validade=data['validade'],
            id_remedio=data['id_remedio']
        )

# Inicializando o FastAPI
app = FastAPI()

# Função auxiliar para salvar os dados no arquivo CSV
def save_to_csv(remedios):
    with open('estoque_remedios.csv', mode='w', newline='') as file:
        fieldnames = remedios[0].to_dict().keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for remedio in remedios:
            writer.writerow(remedio.to_dict())

# Função auxiliar para carregar os dados do CSV
def load_from_csv():
    remedios = []
    if os.path.exists('estoque_remedios.csv'):
        with open('estoque_remedios.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                remedios.append(Remedio.from_dict(row))
    return remedios

# Classe para definir o modelo da requisição para criar o Remédio
class RemedioRequest(BaseModel):
    nome: str
    tarja: str
    preco: float
    validade: str
    id_remedio: str

# Endpoint para adicionar um remédio
@app.post("/remedio")
def add_remedio(remedio: RemedioRequest):
    remedio_obj = Remedio(remedio.nome, remedio.tarja, remedio.preco, remedio.validade, remedio.id_remedio)
    remedios = load_from_csv()
    remedios.append(remedio_obj)
    save_to_csv(remedios)
    return {"message": "Remédio inserido com sucesso"}

# Endpoint para listar todos os remédios
@app.get("/remedios")
def get_remedios():
    remedios = load_from_csv()
    return [remedio.to_dict() for remedio in remedios]

# Endpoint para atualizar um remédio
@app.put("/remedio/{id_remedio}")
def update_remedio(id_remedio: str, remedio: RemedioRequest):
    remedios = load_from_csv()
    for r in remedios:
        if r.id_remedio == id_remedio:
            r.nome = remedio.nome
            r.tarja = remedio.tarja
            r.preco = remedio.preco
            r.validade = remedio.validade
            save_to_csv(remedios)  # Reescrever o CSV
            return {"message": "Remédio atualizado com sucesso"}
    return {"message": "Remédio não encontrado"}

# Endpoint para deletar um remédio
@app.delete("/remedio/{id_remedio}")
def delete_remedio(id_remedio: str):
    remedios = load_from_csv()
    # Filtrar o remédio com o id fornecido
    remedios = [r for r in remedios if r.id_remedio != id_remedio]
    
    if len(remedios) == len(load_from_csv()):  # Se o número de itens não mudar, o remédio não foi encontrado
        return {"message": "Remédio não encontrado"}
    
    # Reescrever o arquivo CSV sem o remédio deletado
    save_to_csv(remedios)
    return {"message": "Remédio deletado com sucesso"}
