# conexao.py

from sqlalchemy import create_engine

def get_database_url():
    user = "your_user"
    password = "Versus2024"
    host = "your_host"
    port = "5432"  # Porta padrão do PostgreSQL
    dbname = "your_dbname"
    charset = 'utf-8'  # Adicione o parâmetro charset aqui
    
    # Certifique-se de que o URL de conexão está correto
    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

def get_engine():
    return create_engine(get_database_url())
