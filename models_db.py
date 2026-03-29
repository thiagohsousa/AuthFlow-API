from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import CHAR
from uuid import uuid4
from database import Base
from schema import Genero, Roles

##models_db.py - Define os modelos de banco de dados usando SQLAlchemy. Este modelo é usado para criar as tabelas no banco de dados. O modelo Usuarios representa a tabela de usuários, com campos para id, nome, sobrenome, cpf, gênero e função. O campo id é do tipo CHAR(36) e é gerado automaticamente usando uuid4 para garantir que cada usuário tenha um identificador único. Os campos genero e Funcao são do tipo Enum, limitando os valores possíveis a opções pré-definidas.

class Usuarios(Base):
    __tablename__ = "usuario";
    Id=Column((CHAR(36)), primary_key=True, default=lambda: str(uuid4()));
    Nome=Column(String(100));
    username=Column(String(100), unique=True);
    Sobrenome=Column (String(50));
    Cpf=Column(String(11));
    genero=Column(Enum(Genero));
    Funcao=Column(Enum(Roles));
    hashed_password= Column(String(100));
