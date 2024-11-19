from pydantic import BaseModel


class RemedioRequest(BaseModel):
    id: str
    nome: str
    tarja: str
    preco: float
    validade: str
