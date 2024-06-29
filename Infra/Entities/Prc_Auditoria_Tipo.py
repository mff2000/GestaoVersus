# infra/entities/Prc_Auditoria.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Auditoria_Tipo(Base):
    __tablename__ = 'PRC_AUDITORIA_TIPO'

    PRC_AUDITORIA_TIPO_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_AUDITORIA_TIPO_NOME = Column(String(255))  # Ajustado para String(255)
    PRC_AUDITORIA_PERIODIC = Column(String(255)) # Ajustado para String(255)
    PRC_AUDITORIA_DESCRICAO = Column(Text)  # Usei Text para permitir textos maiores
    PRC_AUDITORIA_OBSERV = Column(Text)  # Usei Text para permitir textos maiores
    PRC_AUDITORIA_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_AUDITORIA_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_AUDITORIA_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Auditoria_Tipo(PRC_AUDITORIA_TIPO_ID={self.PRC_AUDITORIA_TIPO_ID}, PRC_AUDITORIA_TIPO_NOME={self.PRC_AUDITORIA_TIPO_NOME})"
