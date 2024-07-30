# infra/entities/Ger_Time.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, DateTime

class Ger_Time(Base):
    __tablename__ = 'GER_TIME'

    GER_TIME_ID = Column(Integer, primary_key=True, autoincrement=True)
    GER_TIME_NOME = Column(String(256), nullable=False)
    GER_TIME_SIGLA = Column(String(20), nullable=False)
    GER_TIME_LIDER_ID = Column(Integer, nullable=False)  # Pode ser chave estrangeira para GER_USUARIOS
    GER_TIME_DT_CRIACAO = Column(DateTime)
    GER_TIME_DT_ALTERACAO = Column(DateTime, nullable=False)
    GER_TIME_DT_EXCLUSAO = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Ger_Time(GER_TIME_ID={self.GER_TIME_ID}, GER_TIME_NOME={self.GER_TIME_NOME})"
