from sqlalchemy.orm import Session
from app import models, schemas


def criar_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    novo = models.Fornecedor(**fornecedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_fornecedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fornecedor).offset(skip).limit(limit).all()


def obter_fornecedor(db: Session, fornecedor_id: int):
    return db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()


def atualizar_fornecedor(db: Session, fornecedor_id: int, dados: schemas.FornecedorUpdate):
    fornecedor = obter_fornecedor(db, fornecedor_id)
    if not fornecedor:
        return None
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(fornecedor, key, value)
    db.commit()
    db.refresh(fornecedor)
    return fornecedor


def deletar_fornecedor(db: Session, fornecedor_id: int):
    fornecedor = obter_fornecedor(db, fornecedor_id)
    if fornecedor:
        db.delete(fornecedor)
        db.commit()
    return fornecedor
