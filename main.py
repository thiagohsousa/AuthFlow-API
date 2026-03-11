from fastapi import FastAPI, HTTPException, Depends
from typing import List
from schema import Usuario, Genero, Roles
from schema import RequisicaoAtualizacao
from uuid import UUID
from sqlalchemy.orm import Session
from crud import criar_usuario, deletar_usuario, atualizar_usuario, listar_usuario, buscar_usuario_por_nome
from database import get_db





app = FastAPI()

    
##Método Get que busca por Id
@app.get("/usuarios/{usuario_id}")  
async def fetch_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    try:
        return listar_usuario(db, usuario_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario com Id {usuario_id} não existe"
        )

##Método Get que busca por nome
@app.get("/usuarios/buscar/{nome}")
async def buscar_usuario(nome: str, db: Session = Depends(get_db)):
    try:
        return buscar_usuario_por_nome(db, nome)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum usuario encontrado com esse nome"
        )

##Método post recebe os dados enviados pelo cliente e cria um novo registro de usuário no banco de dados
@app.post("/usuarios")
async def registrar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        return criar_usuario(db, usuario)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao criar usuario: {str(e)}"
        )
   
##Método delete ele deleta um usuario existente
@app.delete("/usuarios/{Usuario_id}")
async def deletar(Usuario_id: UUID, db: Session = Depends(get_db)):
    try:
        return deletar_usuario(db, Usuario_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario com Id {Usuario_id} não existe"
        )

##Método put atualiza as informações de um usuario
@app.put("/usuarios/{Usuario_id}")
async def update(Usuario_id: UUID, usuario: RequisicaoAtualizacao, db: Session = Depends(get_db)):
    try:
        usuario_atualizado = atualizar_usuario(db, Usuario_id, usuario)
        return usuario_atualizado
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario com Id {Usuario_id} não existe"
        )