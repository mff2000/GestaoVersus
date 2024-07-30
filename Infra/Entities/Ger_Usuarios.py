# infra/entities/Ger_Usuarios.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, DateTime

class Ger_Usuarios(Base):
    __tablename__ = 'GER_USUARIOS'

    GER_USU_ID = Column(Integer, primary_key=True, autoincrement=True)
    GER_USU_NOME = Column(String(256), nullable=False)
    GER_USU_EMAIL = Column(String(256), nullable=False, unique=True)
    GER_USU_SENHA = Column(String(256), nullable=True)  # Assumindo que a senha será armazenada como hash
    GER_USU_GRUPOPERMISSAO = Column(String(256))
    GER_USU_TIME = Column(String(256))
    GER_USU_OBSERVACOES = Column(String(999), nullable=False)
    GER_USU_DT_CRIACAO = Column(DateTime, nullable=False)
    GER_USU_DT_ALTERACAO = Column(DateTime)
    GER_USU_DT_INATIVACAO = Column(DateTime)

    def __repr__(self):
        return f"Ger_Usuarios(GER_USU_ID={self.GER_USU_ID}, GER_USU_NOME={self.GER_USU_NOME}, GER_USU_EMAIL={self.GER_USU_EMAIL})"
