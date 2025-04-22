from fastapi import FastAPI
from app.routers import produto, fornecedor, auth
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Inventário")

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(produto.router, prefix="/produtos", tags=["Produtos"])
app.include_router(fornecedor.router, prefix="/fornecedores", tags=["Fornecedores"])
