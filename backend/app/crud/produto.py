from sqlalchemy.orm import Session
from app import models, schemas


def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    novo_produto = models.Produto(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto


def listar_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produto).offset(skip).limit(limit).all()


def obter_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()


def atualizar_produto(db: Session, produto_id: int, dados: schemas.ProdutoUpdate):
    produto = obter_produto(db, produto_id)
    if not produto:
        return None
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(produto, key, value)
    db.commit()
    db.refresh(produto)
    return produto


def deletar_produto(db: Session, produto_id: int):
    produto = obter_produto(db, produto_id)
    if produto:
        db.delete(produto)
        db.commit()
    return produto
