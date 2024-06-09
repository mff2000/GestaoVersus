# db_utils.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_setup import Usuario, Session

# Função para verificar login
def check_login(email, password):
    session = Session()
    user = session.query(Usuario).filter_by(email=email, senha=password).first()
    session.close()
    return user
