from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()


def verificar_senha(senha_plain, senha_hash):
    return pwd_context.verify(senha_plain, senha_hash)


def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hash_senha = pwd_context.hash(usuario.senha)
    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_senha,
        is_admin=usuario.is_admin,
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario
