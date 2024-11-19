from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from models.remedio import RemedioRequest
import services.remedio as remedio_service

app = FastAPI()


@app.post("/remedios")
def add_remedios(remedio_req: RemedioRequest):
    try:
        remedio_service.add_remedio(remedio_req.model_dump())
        return {"message": "Remédio inserido com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/remedios")
def get_remedios():
    return remedio_service.get_remedios()


@app.put("/remedios/{id}")
def update_remedios(id: str, remedio_req: RemedioRequest):
    try:
        remedio_service.update_remedio(id, remedio_req.model_dump())
        return {"message": "Remédio atualizado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete("/remedios/{id}")
def delete_remedios(id: str):
    try:
        remedio_service.delete_remedio(id)
        return {"message": "Remédio deletado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/remedios/quantidade")
def get_quantidade_remedios():
    return {"quantidade": remedio_service.get_quantidade_remedios()}


@app.get("/remedios/compactar")
def compactar_remedios():
    try:
        zip_buffer = remedio_service.compactar_remedios()
        return StreamingResponse(
            zip_buffer,
            media_type="application/x-zip-compressed",
            headers={
                "Content-Disposition": "attachment; filename=estoque_remedios.zip"
            },
        )
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/remedios/hash")
def get_hash_remedios():
    try:
        return {"hash_sha256": remedio_service.get_hash_remedios()}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "API de Controle de Estoque de Remédios funcionando!"}
