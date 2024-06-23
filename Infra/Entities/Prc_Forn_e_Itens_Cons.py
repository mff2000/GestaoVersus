# infra/entities/Prc_Forne_Itens_Cons.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Forne_Itens_Cons(Base):
    __tablename__ = 'PRC_FORNE_ITENS_CONS'

    PRC_FORNE_ITENS_CONS_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_FORNE_ITENS_CONS_NOME = Column(String(255))  # Nome do fornecedor ou item
    PRC_FORNE_ITENS_CONS_UN_MED = Column(String(20))  # Unidade de medida
    PRC_FORNE_ITENS_CONS_VALOR = Column(String(20))  # Valor
    PRC_FORNE_ITENS_CONS_OBSERV = Column(Text)  # Observações
    PRC_FORNE_ITENS_CONS_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_FORNE_ITENS_CONS_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_FORNE_ITENS_CONS_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Forne_Itens_Cons(PRC_FORNE_ITENS_CONS_ID={self.PRC_FORNE_ITENS_CONS_ID}, PRC_FORNE_ITENS_CONS_NOME={self.PRC_FORNE_ITENS_CONS_NOME})"
