from fastapi import FastAPI, HTTPException, Depends
from typing import List
from schema import Usuario, Genero, Roles
from schema import RequisicaoAtualizacao
from uuid import UUID
from sqlalchemy.orm import Session
from crud import criar_usuario, deletar_usuario, atualizar_usuario, listar_usuario, buscar_usuario_por_nome
from database import get_db
import auth
import uvicorn
from database import engine, Base






app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(auth.router) 


##Método Get que busca por nome
@app.get("/usuarios")
async def buscar_usuario(
    nome: str = None,
    db: Session = Depends(get_db)
):
    try:
        if nome:
            return buscar_usuario_por_nome(db, nome)
        
        return listar_usuario(db)

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Nenhum usuario encontrado"
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)