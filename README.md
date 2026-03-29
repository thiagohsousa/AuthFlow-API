# 🚀 AuthFlow API

## 📌 Descrição

API REST desenvolvida com **FastAPI** para gerenciamento de usuários, incluindo autenticação segura com **JWT** e operações completas de CRUD.

A aplicação permite o cadastro, autenticação e gerenciamento de usuários, com proteção de rotas e criptografia de senhas.

Este projeto tem como foco o desenvolvimento de habilidades em **back-end**, boas práticas de APIs REST e integração com banco de dados.

---

## 🌐 Deploy

🔗 API Online: https://authflow-api-d0i1.onrender.com/  
🔗 Documentação Swagger: https://authflow-api-d0i1.onrender.com/docs  

---

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Uvicorn
- JWT (JSON Web Token)
- Passlib (criptografia de senhas)
- Swagger (documentação automática)

---

## 🔐 Funcionalidades

A API permite:

- ✅ Cadastro de usuários
- ✅ Autenticação com JWT
- ✅ Login seguro
- ✅ Criptografia de senhas com bcrypt
- ✅ Proteção de rotas autenticadas
- ✅ CRUD completo:
  - Criar usuários
  - Listar usuários
  - Atualizar usuários
  - Deletar usuários

---

## 📂 Estrutura do projeto


app/
├── main.py
├── database.py
├── models_db.py
├── schemas.py
├── crud.py
├── auth.py
└── criar_tabela.py


---

## ▶️ Como rodar o projeto

### 1️⃣ Clone o repositório

git clone https://github.com/thiagohsousa/fastapi-crud-api.git


### 2️⃣ Acesse a pasta

cd fastapi-crud-api


### 3️⃣ Instale as dependências

pip install -r requirements.txt


### 4️⃣ Execute o servidor

uvicorn main:app --reload


---

## 📡 Testando a API

Você pode testar os endpoints utilizando:

- Swagger: http://localhost:8000/docs
- Postman
- Insomnia

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

### 🔑 Fluxo:

1. Usuário faz login em `/auth/login`
2. Recebe um `access_token`
3. Envia o token nas requisições protegidas:


Authorization: Bearer SEU_TOKEN_AQUI


---

## ⚙️ Variáveis de ambiente

Para produção, utilize:


SECRET_KEY=sua_chave_secreta


---

## 🎓 Objetivo

Projeto desenvolvido para prática de:

- APIs REST
- Autenticação
- Banco de dados
- Back-end com Python

---

## 👨‍💻 Autor

Thiago Henrique Sousa Melo

GitHub: https://github.com/thiagohsousa  
LinkedIn: https://www.linkedin.com/in/thiago-henrique-sousa01






