# infra/entities/Prc_Modelagem.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Macropr_Avo(Base):
    __tablename__ = 'PRC_MACROPR_AVO'

    PRC_MACROPR_AVO_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_MACROPR_AVO_NOME = Column(String(255))
    PRC_MACROPR_AVO_DONO_ID = Column(Integer, nullable=True)
    PRC_MACROPR_AREA_ID = Column(Integer, nullable=True)
    PRC_MACROPR_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_MACROPR_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_MACROPR_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Macropr_Avo(PRC_MACROPR_AVO_ID={self.PRC_MACROPR_AVO_ID}, PRC_MACROPR_AVO_NOME={self.PRC_MACROPR_AVO_NOME})"