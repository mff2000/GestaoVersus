# infra/entities/Prc_Conhec.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Conhec(Base):
    __tablename__ = 'PRC_CONHEC'

    PRC_CONHEC_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_CONHEC_TEC = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CONHEC_GEST = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CONHEC_RELAC = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CONHEC_DESCR = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CONHEC_OBSERV = Column(Text)  # Usei Text para permitir textos maiores
    PRC_CONHEC_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_CONHEC_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_CONHEC_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Conhec(PRC_CONHEC_ID={self.PRC_CONHEC_ID})"
