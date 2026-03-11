from sqlalchemy.orm import Session
from models_db import Usuarios
from schema import Usuario

##função para criar usuario, recebe um objeto do tipo Usuario e salva no banco de dados, retorna o usuario criado.

def criar_usuario(db: Session, usuario: Usuario):
    novo_usuario = Usuarios(
        Id=str(usuario.id),
        Nome=usuario.nome,
        Sobrenome=usuario.sobrenome,
        Cpf=usuario.Cpf,
        genero=usuario.genero,
        Funcao=usuario.funcoes[0] if usuario.funcoes else None
    )

    db.add(novo_usuario)
    db.commit()

    return novo_usuario

##função para deletar usuario, recebe o id do usuario e deleta o usuario correspondente, caso o usuario não seja encontrado, retorna um erro.

def deletar_usuario(db: Session, usuario_id):
    usuario = db.query(Usuarios).filter(Usuarios.Id == str(usuario_id)).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    else: 
        raise ValueError("Usuario não encontrado") 
    
##função para listar usuario por id, recebe o id do usuario e retorna o usuario correspondente, caso o usuario não seja encontrado, retorna um erro

def listar_usuario(db : Session, usuario_id):
    usuario = db.query(Usuarios).filter(Usuarios.Id == str(usuario_id)).first()
    
    if usuario:
        return usuario
    else:
        raise ValueError("Usuario não encontrado")
    

##função para buscar usuario por nome, recebe o nome do usuario e retorna uma lista de usuarios que possuem o nome informado, caso nenhum usuario seja encontrado, retorna um erro

def buscar_usuario_por_nome(db: Session, nome: str):
    usuarios = db.query(Usuarios).filter(Usuarios.Nome.ilike(f"%{nome}%")).all()
    
    if usuarios:
        return usuarios
    else:
        raise ValueError("Nenhum usuario encontrado com esse nome")

##função para atualizar o usuario, recebe o id do usuario e os dados a serem atualizados, verifica se o usuario existe, se existir atualiza os campos que foram enviados e salva no banco de dados

def atualizar_usuario(db : Session, usuario_id, dados):
    usuario = db.query(Usuarios).filter(Usuarios.Id == str(usuario_id)).first()
    if not usuario:
        raise ValueError("Usuario não encontrado")
    
    if dados.nome:
        usuario.Nome = dados.nome
    
    if dados.sobrenome:
        usuario.Sobrenome = dados.sobrenome

    if dados.Cpf:
        usuario.Cpf = dados.Cpf

    if dados.genero:
        usuario.genero = dados.genero

    if dados.funcoes:
        usuario.Funcao = dados.funcoes[0]

    db.commit()
    return usuario

