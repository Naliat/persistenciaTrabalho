from fastapi import FastAPI
from pydantic import BaseModel
import csv
import os

# Definindo a classe do Remédio
class Remedio:
    def __init__(self, id_remedio, nome, tarja, preco, validade):
        self.id_remedio = id_remedio
        self.nome = nome
        self.tarja = tarja
        self.preco = preco
        self.validade = validade

    def to_dict(self):
        return {
            "id_remedio": self.id_remedio,
            "nome": self.nome,
            "tarja": self.tarja,
            "preco": self.preco,
            "validade": self.validade,
        }

    @staticmethod
    def from_dict(data):
        return Remedio(
            id_remedio=data["id_remedio"],
            nome=data["nome"],
            tarja=data["tarja"],
            preco=data["preco"],
            validade=data["validade"],
        )


# Inicializando o FastAPI
app = FastAPI()


# Função auxiliar para salvar os dados no arquivo CSV
def save_to_csv(remedios):
    with open("estoque_remedios.csv", mode="w", newline="") as file:
        fieldnames = ["id_remedio", "nome", "tarja", "preco", "validade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for remedio in remedios:
            writer.writerow(remedio.to_dict())


# Função auxiliar para carregar os dados do CSV
def load_from_csv():
    remedios = []
    if os.path.exists("estoque_remedios.csv"):
        with open("estoque_remedios.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                remedios.append(Remedio.from_dict(row))
    return remedios


# Classe para definir o modelo da requisição para criar o Remédio
class RemedioRequest(BaseModel):
    id_remedio: str
    nome: str
    tarja: str
    preco: float
    validade: str


# Endpoint para adicionar um remédio
@app.post("/remedios")
def add_remedio(remedio: RemedioRequest):
    remedio_obj = Remedio(
        remedio.id_remedio, remedio.nome, remedio.tarja, remedio.preco, remedio.validade
    )
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
@app.put("/remedios/{id_remedio}")
def update_remedio(id_remedio: str, remedio: RemedioRequest):
    remedios = load_from_csv()
    for r in remedios:
        if r.id_remedio == id_remedio:
            r.nome = remedio.nome
            r.tarja = remedio.tarja
            r.preco = remedio.preco
            r.validade = remedio.validade
            save_to_csv(remedios)
            return {"message": "Remédio atualizado com sucesso"}
    return {"message": "Remédio não encontrado"}


# Endpoint para deletar um remédio
@app.delete("/remedios/{id_remedio}")
def delete_remedio(id_remedio: str):
    remedios = load_from_csv()
    remedios_filtrados = [r for r in remedios if r.id_remedio != id_remedio]

    if len(remedios) == len(remedios_filtrados):
        return {"message": "Remédio não encontrado"}

    save_to_csv(remedios_filtrados)
    return {"message": "Remédio deletado com sucesso"}
