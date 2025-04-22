from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import schemas, crud
from app.database import get_db
from app.auth import criar_token
from app.crud.usuario import verificar_senha, get_usuario_by_email

router = APIRouter()


@router.post("/register", response_model=schemas.UsuarioOut)
def register(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    if get_usuario_by_email(db, usuario.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.criar_usuario(db, usuario)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = get_usuario_by_email(db, form_data.username)
    if not usuario or not verificar_senha(form_data.password, usuario.senha):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
