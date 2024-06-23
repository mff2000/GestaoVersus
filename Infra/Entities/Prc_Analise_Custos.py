# infra/entities/Prc_Analise_Custos.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Analise_Custos(Base):
    __tablename__ = 'PRC_ANALISE_CUSTOS'

    PRC_ANALISE_CUSTOS_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ID = Column(Integer, nullable=False)
    PRC_ANALISE_CUSTOS_CUSTO_FIXO = Column(String(255))
    PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL = Column(String(255))
    PRC_ANALISE_CUSTOS_CUSTO_TOTAL = Column(String(255))
    PRC_ANALISE_CUSTOS_GASTOS_GERAIS = Column(String(255))
    PRC_ANALISE_CUSTOS_INVESTIMENTO = Column(String(255))
    PRC_ANALISE_CUSTOS_LUCRO = Column(String(255))
    PRC_ANALISE_CUSTOS_ROIC = Column(String(255))
    PRC_ANALISE_CUSTOS_OBSERVACOES = Column(Text)
    PRC_ANALISE_CUSTOS_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_ANALISE_CUSTOS_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_ANALISE_CUSTOS_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Analise_Custos(PRC_ANALISE_CUSTOS_ID={self.PRC_ANALISE_CUSTOS_ID}, PRC_ID={self.PRC_ID})"
