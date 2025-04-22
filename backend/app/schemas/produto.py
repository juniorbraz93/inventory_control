from pydantic import BaseModel
from typing import Optional


class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade: int
    categoria: Optional[str] = None
    fornecedor_id: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    quantidade: Optional[int]
    categoria: Optional[str]
    fornecedor_id: Optional[int]


class ProdutoOut(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
