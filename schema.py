from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum

class Genero(str, Enum):
    Masculino = "Masculino"
    Feminino = "Feminino"

class Roles(str, Enum):
    admin = "Admin"
    user = "User"
    estudante = "estudante"

class Usuario(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str
    sobrenome: str
    nome_meio: Optional[str] = None
    genero: Genero
    funcoes: List[Roles]

class RequisicaoAtualizacao(BaseModel):
    nome: str = None
    sobrenome: str = None
    nome_meio: Optional[str] = None
    genero: Genero = None
    funcoes: List[Roles] = None
        