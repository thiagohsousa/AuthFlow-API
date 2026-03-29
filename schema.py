from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum

##schema.py - Define os modelos de dados para a aplicação usando Pydantic. Este modelo é usado para validar e serializar os dados que entram e saem da aplicação, garantindo que os dados estejam no formato correto e atendam aos requisitos definidos.

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
    username: str
    sobrenome: str
    Cpf: Optional[str] = None
    genero: Genero
    funcoes: List[Roles]
    hashed_password: str

class RequisicaoAtualizacao(BaseModel):
    nome: str = None
    sobrenome: str = None
    Cpf: Optional[str] = None
    genero: Genero = None
    funcoes: List[Roles] = None
    hashed_password: str = None   