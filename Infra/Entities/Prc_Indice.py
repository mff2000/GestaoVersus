# infra/entities/Ger_Indic.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Ger_Indic(Base):
    __tablename__ = 'GER_INDIC'

    GER_INDIC_ID = Column(Integer, primary_key=True, autoincrement=True)
    GER_INDIC_TIPO = Column(String(255))
    GER_INDIC_NOME = Column(String(255))
    GER_INDIC_RESPONS = Column(String(255))
    GER_INDIC_CALCULO = Column(Text)
    GER_INDIC_OBSERV = Column(Text)
    GER_INDIC_DT_CRIACAO = Column(DateTime, nullable=False)
    GER_INDIC_DT_ALTERACAO = Column(DateTime, nullable=True)
    GER_INDIC_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Ger_Indic(GER_INDIC_ID={self.GER_INDIC_ID}, GER_INDIC_NOME={self.GER_INDIC_NOME})"
