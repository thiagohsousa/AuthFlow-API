
from database import criar_tabelas
from models_db import Usuarios  

## Script para criar as tabelas no banco de dados usando SQLAlchemy. Este script deve ser executado apenas uma vez para configurar o banco de dados antes de usar a aplicação.

if __name__ == "__main__":
    print("Criando tabelas no banco de dados...")
    criar_tabelas()
    print("✓ Tabelas criadas com sucesso!")
