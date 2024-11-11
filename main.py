from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import csv
import os
from hashlib import sha256
import zipfile
from io import BytesIO
from typing import List


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
            "id_remedio": self.id_remedio,
        }

    @staticmethod
    def from_dict(data):
        return Remedio(
            nome=data["nome"],
            tarja=data["tarja"],
            preco=float(data["preco"]),
            validade=data["validade"],
            id_remedio=data["id_remedio"],
        )


app = FastAPI()


# Função auxiliar para salvar os dados no arquivo CSV
def save_to_csv(remedios: List[Remedio]):
    with open("estoque_remedios.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=remedios[0].to_dict().keys())
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


class RemedioRequest(BaseModel):
    nome: str
    tarja: str
    preco: float
    validade: str
    id_remedio: str


@app.post("/remedio")
def add_remedio(remedio: RemedioRequest):
    remedios = load_from_csv()

    # Regras de validação
    if any(r.id_remedio == remedio.id_remedio for r in remedios):
        raise HTTPException(status_code=400, detail="ID do remédio já existe.")
    if any(
        r.nome == remedio.nome
        and r.tarja == remedio.tarja
        and r.preco == remedio.preco
        and r.validade == remedio.validade
        for r in remedios
    ):
        raise HTTPException(
            status_code=400,
            detail="Já existe um remédio com os mesmos dados cadastrados.",
        )

    remedios.append(Remedio(**remedio.dict()))
    save_to_csv(remedios)
    return {"message": "Remédio inserido com sucesso"}


@app.get("/remedios")
def get_remedios():
    remedios = load_from_csv()
    return [remedio.to_dict() for remedio in remedios]


@app.put("/remedio/{id_remedio}")
def update_remedio(id_remedio: str, remedio: RemedioRequest):
    remedios = load_from_csv()

    for r in remedios:
        if r.id_remedio == id_remedio:
            # Regras de validação para evitar duplicação na atualização
            if any(
                r2.id_remedio != id_remedio
                and r2.nome == remedio.nome
                and r2.tarja == remedio.tarja
                and r2.preco == remedio.preco
                and r2.validade == remedio.validade
                for r2 in remedios
            ):
                raise HTTPException(
                    status_code=400,
                    detail="Já existe outro remédio com os mesmos dados.",
                )

            r.nome = remedio.nome
            r.tarja = remedio.tarja
            r.preco = remedio.preco
            r.validade = remedio.validade
            save_to_csv(remedios)
            return {"message": "Remédio atualizado com sucesso"}

    raise HTTPException(status_code=404, detail="Remédio não encontrado")


@app.delete("/remedio/{id_remedio}")
def delete_remedio(id_remedio: str):
    remedios = load_from_csv()
    remedios_filtrados = [r for r in remedios if r.id_remedio != id_remedio]

    if len(remedios) == len(remedios_filtrados):
        raise HTTPException(status_code=404, detail="Remédio não encontrado")

    if remedios_filtrados:
        save_to_csv(remedios_filtrados)
    else:
        os.remove("estoque_remedios.csv")

    return {"message": "Remédio deletado com sucesso"}


@app.get("/quantidade_remedios")
def get_quantidade_remedios():
    remedios = load_from_csv()
    return {"quantidade": len(remedios)}


@app.get("/compactar_csv")
def compactar_csv():
    if not os.path.exists("estoque_remedios.csv"):
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado")

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write("estoque_remedios.csv", arcname="estoque_remedios.csv")
    zip_buffer.seek(0)

    return StreamingResponse(
        zip_buffer,
        media_type="application/x-zip-compressed",
        headers={"Content-Disposition": "attachment; filename=estoque_remedios.zip"},
    )


@app.get("/hash_csv")
def get_hash_csv():
    if not os.path.exists("estoque_remedios.csv"):
        raise HTTPException(status_code=404, detail="Arquivo CSV não encontrado")

    with open("estoque_remedios.csv", "rb") as file:
        file_data = file.read()
        hash_sha256 = sha256(file_data).hexdigest()
    return {"hash_sha256": hash_sha256}


@app.get("/")
def read_root():
    return {"message": "API de Controle de Estoque de Remédios funcionando!"}
