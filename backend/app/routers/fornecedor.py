from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db
from app.auth import verificar_token, somente_admin

router = APIRouter()


@router.post("/", response_model=schemas.FornecedorOut)
def criar(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    return crud.criar_fornecedor(db, fornecedor)


@router.get("/", response_model=List[schemas.FornecedorOut])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    return crud.listar_fornecedores(db, skip, limit)


@router.get("/{fornecedor_id}", response_model=schemas.FornecedorOut)
def obter(fornecedor_id: int, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    fornecedor = crud.obter_fornecedor(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor


@router.put("/{fornecedor_id}", response_model=schemas.FornecedorOut)
def atualizar(fornecedor_id: int, dados: schemas.FornecedorUpdate, db: Session = Depends(get_db), usuario = Depends(somente_admin)):
    fornecedor = crud.atualizar_fornecedor(db, fornecedor_id, dados)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor


@router.delete("/{fornecedor_id}", response_model=schemas.FornecedorOut)
def deletar(fornecedor_id: int, db: Session = Depends(get_db), usuario = Depends(somente_admin)):
    fornecedor = crud.deletar_fornecedor(db, fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor
