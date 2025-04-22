from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    categoria = Column(String(50))
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    fornecedor = relationship("Fornecedor", back_populates="produtos")
