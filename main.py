from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import remedio  

app = FastAPI()

class RemedioRequest(BaseModel):
    id: str
    nome: str
    tarja: str
    preco: float
    validade: str

@app.post("/remedios")
def add_remedios(remedio_req: RemedioRequest):
    try:
        remedio.add_remedio(remedio_req.dict())
        return {"message": "Remédio inserido com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/remedios")
def get_remedios():
    return remedio.get_remedios()

@app.put("/remedios/{id}")
def update_remedios(id: str, remedio_req: RemedioRequest):
    try:
        remedio.update_remedio(id, remedio_req.dict())
        return {"message": "Remédio atualizado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/remedios/{id}")
def delete_remedios(id: str):
    try:
        remedio.delete_remedio(id)
        return {"message": "Remédio deletado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/remedios/quantidade")
def get_quantidade_remedios():
    return {"quantidade": remedio.get_quantidade_remedios()}

@app.get("/remedios/compactar")
def compactar_remedios():
    try:
        zip_buffer = remedio.compactar_remedios()
        return StreamingResponse(
            zip_buffer,
            media_type="application/x-zip-compressed",
            headers={"Content-Disposition": "attachment; filename=estoque_remedios.zip"},
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/remedios/hash")
def get_hash_remedios():
    try:
        return {"hash_sha256": remedio.get_hash_remedios()}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "API de Controle de Estoque de Remédios funcionando!"}
