from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    telefone: str = None
    cpf: str
    compra_fiado: int
    dia_fiado: int
    senha: str = None