from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
import models_db
from models_db import Usuarios
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import os 

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login") 

class createRequisicaouser(BaseModel):
    nome: str
    username: str  
    sobrenome: str
    Cpf: str
    genero: str
    funcoes: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# ROTA DE CRIAÇÃO DE USUÁRIO
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: createRequisicaouser, db: db_dependency):

    create_user_model = Usuarios(
        username=user.username,
        hashed_password=bcrypt_context.hash(user.password)
    )

    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model) 

    return create_user_model  

# AUTENTICAÇÃO
def autenticar_usuario(db, username: str, password: str):
    user = db.query(Usuarios).filter(Usuarios.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

# CRIAÇÃO DO TOKEN
def criar_token_acesso(username: str, user_id: str, expires_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
        "exp": datetime.utcnow() + expires_delta
    }
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# LOGIN
@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = autenticar_usuario(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username ou senha incorretos."
        )

    access_token = criar_token_acesso(
        user.username,
        user.Id,
        timedelta(minutes=20)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

