from pydantic import BaseModel
from typing import Optional, List
from app.schemas.produto import ProdutoOut


class FornecedorBase(BaseModel):
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None


class FornecedorCreate(FornecedorBase):
    pass


class FornecedorUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    telefone: Optional[str]


class FornecedorOut(FornecedorBase):
    id: int
    produtos: List[ProdutoOut] = []

    class Config:
        orm_mode = True
