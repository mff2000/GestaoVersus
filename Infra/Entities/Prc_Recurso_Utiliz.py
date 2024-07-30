from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric

class Prc_Recurso_Utiliz(Base):
    __tablename__ = 'PRC_RECURSO_UTILIZ'

    PRC_RECURSO_UTILIZ_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_RECURSO_UTILIZ_NOME = Column(String(256))  # Nome não deve ser nulo
    PRC_RECURSO_UTILIZ_DESCRICAO = Column(Text)  # Use Text para descrições longas
    PRC_RECURSO_UTILIZ_CUSTO_UNIT = Column(Numeric(10, 2))  # Corrigido tipo e removido nulo
    PRC_RECURSO_UTILIZ_OBSERV = Column(Text)  # Use Text para observações longas
    PRC_RECURSO_UTILIZ_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_RECURSO_UTILIZ_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_RECURSO_UTILIZ_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Recurso_Utiliz(PRC_RECURSO_UTILIZ_ID={self.PRC_RECURSO_UTILIZ_ID}, PRC_RECURSO_UTILIZ_NOME='{self.PRC_RECURSO_UTILIZ_NOME}')"
