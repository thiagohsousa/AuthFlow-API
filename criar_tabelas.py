
from database import criar_tabelas
from models_db import Usuarios  

if __name__ == "__main__":
    print("Criando tabelas no banco de dados...")
    criar_tabelas()
    print("✓ Tabelas criadas com sucesso!")
