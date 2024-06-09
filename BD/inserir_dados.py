from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Importar a engine do arquivo de conexão
from conexao_bd import engine

Base = declarative_base()

# Definir a classe para a tabela GER_USUARIOS
class Usuario(Base):
    __tablename__ = 'GER_USUARIOS'

    id = Column(Integer, primary_key=True)
    GER_USU_NOME = Column(String)
    GER_USU_EMAIL = Column(String)
    GER_USU_SENHA = Column(String)
    GER_USU_GRUPOPERMISSAO = Column(String)
    GER_USU_TIME = Column(String)
    GER_USU_OBSERVACOES = Column(String)
    GER_USU_DT_CRIACAO = Column(DateTime)
    GER_USU_DT_ALTERACAO = Column(DateTime)
    GER_USU_DT_INATIVACAO = Column(DateTime)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar um novo usuário
novo_usuario = Usuario(
    GER_USU_NOME='Marcos Ferreira',
    GER_USU_EMAIL='versusconsultoria@gmail.com',
    GER_USU_SENHA='4617',
    GER_USU_GRUPOPERMISSAO='gestor',
    GER_USU_TIME='diretoria',
    GER_USU_OBSERVACOES='criador do projeto',
    GER_USU_DT_CRIACAO=datetime.strptime('08/06/2024', '%d/%m/%Y')
)

# Adicionar o novo usuário à sessão e commitar para o banco de dados
session.add(novo_usuario)
session.commit()

# Fechar a sessão
session.close()
