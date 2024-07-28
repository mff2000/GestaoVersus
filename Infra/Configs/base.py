from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@contextmanager
def get_session():
    from .connection import DBConnectionHandler
    """
    Gerenciador de contexto para obter uma sessão de banco de dados.

    Este gerenciador de contexto simplifica a obtenção e o uso de uma sessão 
    do banco de dados, garantindo que a sessão seja fechada corretamente após o uso.
    """

    with DBConnectionHandler() as db_connection:
        yield db_connection.session

