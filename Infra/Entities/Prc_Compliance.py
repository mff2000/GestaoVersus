# infra/entities/Prc_Compliance.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Compliance(Base):
    __tablename__ = 'PRC_COMPLIANCE'

    PRC_COMPLIANCE_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_COMPLIANCE_TIPO_REGRA = Column(String(255), nullable=True)
    PRC_COMPLIANCE_DESCR_REGRA = Column(Text, nullable=True)  # Usei Text para permitir textos maiores
    PRC_COMPLIANCE_SITUACAO_REGRA = Column(String(255), nullable=True)
    PRC_COMPLIANCE_OBSERV = Column(Text, nullable=True)  # Usei Text para permitir textos maiores
    PRC_COMPLIANCE_DT_CRIACAO = Column(DateTime)
    PRC_COMPLIANCE_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_COMPLIANCE_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Compliance(PRC_COMPLIANCE_ID={self.PRC_COMPLIANCE_ID}, PRC_COMPLIANCE_TIPO_REGRA={self.PRC_COMPLIANCE_TIPO_REGRA})"
