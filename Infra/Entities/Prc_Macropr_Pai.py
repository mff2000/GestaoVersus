# infra/entities/Prc_Modelagem.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Macropr_Pai(Base):
    __tablename__ = 'PRC_MACROPR_PAI'

    PRC_MACROPR_PAI_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_MACROPR_PAI_GERENC_ID = Column(String(255))
    PRC_MACROPR_PAI_MISSAO = Column(String(255))
    PRC_MACROPR_PAI_DONO_ID = Column(Integer, nullable=True)
    PRC_MACROPR_PAI_EXIG_QUAL = Column(String(255))
    PRC_MACROPR_AVO_ID = Column(Integer, nullable=True)
    PRC_MACROPR_INDICAD_ID = Column(String(255))
    PRC_MACROPR_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_MACROPR_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_MACROPR_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Macropr_Pai(PRC_MACROPR_PAI_ID={self.PRC_MACROPR_PAI_ID}, PRC_MACROPR_PAI_GERENC_ID={self.PRC_MACROPR_PAI_GERENC_ID}, PRC_MACROPR_PAI_DONO_ID={self.PRC_MACROPR_PAI_DONO_ID}, PRC_MACROPR_PAI_EXIG_QUAL={self.PRC_MACROPR_PAI_EXIG_QUAL}, PRC_MACROPR_AVO_ID={self.PRC_MACROPR_AVO_ID}, PRC_MACROPR_INDICAD_ID={self.PRC_MACROPR_INDICAD_ID})"