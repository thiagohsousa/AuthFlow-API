# FastAPI CRUD API

## 📌 Descrição

Este projeto é uma API REST desenvolvida com **FastAPI** para gerenciamento de usuários.  
A aplicação permite criar, listar, atualizar e deletar usuários utilizando operações CRUD, alem disso a api permite fazer login atraves da autenticação JWT.

O objetivo do projeto é praticar conceitos de desenvolvimento backend utilizando Python, APIs REST e integração com banco de dados.

---

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Uvicorn
- Swagger
---

## ⚙️ Funcionalidades

A API permite:

- Criar usuários
- Listar usuários
- Atualizar usuários
- Deletar usuários
- Fazer Login

---

## 📂 Estrutura do projeto

**main.py**  
Arquivo principal onde ficam as rotas da API.

**database.py**  
Responsável pela conexão com o banco de dados.

**models_db.py**  
Define as tabelas do banco utilizando SQLAlchemy.

**schemas.py**  
Define os schemas e validações de dados utilizando Pydantic.

**criar_tabela.py**
Responsável por criar as tabelas no banco de dados automaticamente.

**crud.py**  
Contém as funções responsáveis pelas operações CRUD (Create, Read, Update e Delete).

**auth.py**
Responsavel pela Autenticação JWT, Criptografa senhas, cria Tokens e Permite realizar Login
 
---

## ▶️ Como rodar o projeto

### 1️⃣ Clone o repositório
git clone: https://github.com/thiagohsousa/fastapi-crud-api.git


### 2️⃣ Instale as dependências
pip install -r requirements.txt

### 3️⃣ Execute o servidor
uvicorn app.main:app --reload


---

## 📡 Testando a API

Você pode testar os endpoints utilizando:

- Postman
- Insomnia
 
---

## 🎓 Objetivo acadêmico

Este projeto foi desenvolvido com fins educacionais para praticar conceitos de desenvolvimento backend utilizando Python e FastAPI.

O objetivo é reforçar conhecimentos em:

- APIs REST
- Operações CRUD
- Integração com banco de dados
- Estruturação de projetos backend

---

## 👨‍💻 Autor

Projeto desenvolvido por **Thiago Henrique Sousa Melo**.







