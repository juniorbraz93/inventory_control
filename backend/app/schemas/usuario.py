from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    email: str


class UsuarioCreate(UsuarioBase):
    senha: str
    is_admin: Optional[bool] = False


class UsuarioOut(UsuarioBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True


class UsuarioLogin(BaseModel):
    email: str
    senha: str
