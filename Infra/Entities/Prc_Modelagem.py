# infra/entities/Prc_Modelagem.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Modelagem(Base):
    __tablename__ = 'PRC_MODELAGEM'

    PRC_MODELAGEM_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_MODELAGEM_TIPO = Column(String(255))
    PRC_MODELAGEM_DESCR = Column(Text)
    PRC_MODELAGEM_OBSERV = Column(Text)
    PRC_MODELAGEM_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_MODELAGEM_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_MODELAGEM_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Modelagem(PRC_MODELAGEM_ID={self.PRC_MODELAGEM_ID}, PRC_MODELAGEM_TIPO={self.PRC_MODELAGEM_TIPO})"
