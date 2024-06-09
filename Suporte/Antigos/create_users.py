from sqlalchemy import create_engine, Column, Integer, String, DateTime, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Define the database connection
DATABASE_URL = "postgresql+psycopg2://versus:Versus*2024@localhost:5432/gestao_versus?client_encoding=utf8"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

class GER_USUARIOS(Base):
    __tablename__ = 'GER_USUARIOS'
    
    GER_USU_ID = Column(Integer, Sequence('ger_usu_id_seq'), primary_key=True, autoincrement=True)
    GER_USU_NOME = Column(String(256), nullable=False)
    GER_USU_EMAIL = Column(String(256), nullable=False)
    GER_USU_SENHA = Column(String(256), nullable=False)
    GER_USU_GRUPOPERMISSAO = Column(String(256))
    GER_USU_TIME = Column(String(256))
    GER_USU_OBSERVACOES = Column(String(999))
    GER_USU_DT_CRIACAO = Column(DateTime, default=datetime.utcnow, nullable=False)
    GER_USU_DT_ALTERACAO = Column(DateTime)
    GER_USU_DT_INATIVACAO = Column(DateTime)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example of how to add a new user
new_user = GER_USUARIOS(
    GER_USU_NOME='John Doe',
    GER_USU_EMAIL='john.doe@example.com',
    GER_USU_SENHA='securepassword',
    GER_USU_GRUPOPERMISSAO='admin',
    GER_USU_TIME='team1',
    GER_USU_OBSERVACOES='No observations'
)

session.add(new_user)
session.commit()

