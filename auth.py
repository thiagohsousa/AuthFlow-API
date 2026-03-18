from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
import models_db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = "134625bniai19890987b8a9c8e5f6a7b8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6u7v8w9x0y1z2"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Serve para criptografar (hash) as senhas dos usuários antes de salvá-las no banco de dados e para verificar as senhas durante o processo de login.
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login") #Serve para proteger os endpoints (rotas) da API. Ele cria um mecanismo que exige um token JWT válido no cabeçalho da requisição (a famosa parte de "Bearer Token") para que o usuário consiga acessar dados protegidos.

class createRequisicaouser(BaseModel):
    nome: str
    sobrenome: str
    Cpf: str
    genero: str
    funcoes: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str