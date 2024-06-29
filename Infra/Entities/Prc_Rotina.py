# infra/entities/Prc_Rotina.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Rotina(Base):
    __tablename__ = 'PRC_ROTINA'

    PRC_ROTINA_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ROTINA_NOME = Column(String(255))
    PRC_ROTINA_PERIOD = Column(String(255))
    PRC_ROTINA_START = Column(String(255))
    PRC_ROTINA_DESCR = Column(Text)
    PRC_ROTINA_OBSERV = Column(Text)
    PRC_ROTINA_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_ROTINA_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_ROTINA_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Rotina(PRC_ROTINA_ID={self.PRC_ROTINA_ID}, PRC_ROTINA_TIPO={self.PRC_ROTINA_NOME}, PRC_ROTINA_PERIOD={self.PRC_ROTINA_PERIOD})"
