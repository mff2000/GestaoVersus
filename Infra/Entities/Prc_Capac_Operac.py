# infra/entities/Prc_Capac_Operac.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Capac_Operac(Base):
    __tablename__ = 'PRC_CAPAC_OPERAC'

    PRC_CAPAC_OPERAC_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_CAPAC_OPERAC_ELEMEN = Column(String(255))
    PRC_CAPAC_OPERAC_UN_MED = Column(String(255))
    PRC_CAPAC_OPERAC_VALOR = Column(String(255))
    PRC_CAPAC_OPERAC_DESCR = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CAPAC_OPERAC_OBSERV = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CAPAC_OPERAC_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_CAPAC_OPERAC_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_CAPAC_OPERAC_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Capac_Operac(PRC_CAPAC_OPERAC_ID={self.PRC_CAPAC_OPERAC_ID}, PRC_CAPAC_OPERAC_ELEMEN={self.PRC_CAPAC_OPERAC_ELEMEN})"
