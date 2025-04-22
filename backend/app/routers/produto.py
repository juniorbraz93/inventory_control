from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db
from app.auth import verificar_token, somente_admin

router = APIRouter()


@router.post("/", response_model=schemas.ProdutoOut)
def criar(produto: schemas.ProdutoCreate, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    return crud.criar_produto(db, produto)


@router.get("/", response_model=List[schemas.ProdutoOut])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    return crud.listar_produtos(db, skip, limit)


@router.get("/{produto_id}", response_model=schemas.ProdutoOut)
def obter(produto_id: int, db: Session = Depends(get_db), usuario = Depends(verificar_token)):
    produto = crud.obter_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.put("/{produto_id}", response_model=schemas.ProdutoOut)
def atualizar(produto_id: int, dados: schemas.ProdutoUpdate, db: Session = Depends(get_db), usuario = Depends(somente_admin)):
    produto = crud.atualizar_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.delete("/{produto_id}", response_model=schemas.ProdutoOut)
def deletar(produto_id: int, db: Session = Depends(get_db), usuario = Depends(somente_admin)):
    produto = crud.deletar_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
