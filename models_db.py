from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import CHAR
from uuid import uuid4
from database import Base
from schema import Genero, Roles


class Usuarios(Base):
    __tablename__ = "usuario";
    Id = Column((CHAR(36)), primary_key=True, default=lambda: str(uuid4()));
    Nome = Column(String(100));
    Sobrenome = Column (String(50));
    Cpf = Column(String(11));
    genero = Column(Enum(Genero));
    Funcao =  Column(Enum(Roles));