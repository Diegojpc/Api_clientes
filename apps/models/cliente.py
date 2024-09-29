from sqlalchemy import Column, Integer, String
from db import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    idCliente = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    ubicacion = Column(String(100), nullable=False)
