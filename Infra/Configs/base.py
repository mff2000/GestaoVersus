from sqlalchemy.orm import declarative_base
from .connection import DBConnectionHandler  # Importe a classe de conexão

# Definição da classe Base
Base = declarative_base()

# Função para obter uma sessão com o banco de dados
def get_session():
    db_connection = DBConnectionHandler()  # Cria uma instância da classe
    session = db_connection.session          # Obtém a sessão
    try:
        yield session                      # Retorna a sessão
    finally:
        db_connection.session.close()       # Garante o fechamento da sessão
