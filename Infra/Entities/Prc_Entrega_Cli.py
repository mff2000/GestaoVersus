# infra/entities/Prc_Entrega_Cli.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Entrega_Cli(Base):
    __tablename__ = 'PRC_ENTREGA_CLI'

    PRC_ENTREGA_CLI_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ID = Column(Integer, nullable=False)
    PRC_ENTREGA_CLI_DESCR = Column(Text)
    PRC_ENTREGA_CLI_OBSERV = Column(Text)
    PRC_ENTREGA_CLI_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_ENTREGA_CLI_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_ENTREGA_CLI_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Entrega_Cli(PRC_ENTREGA_CLI_ID={self.PRC_ENTREGA_CLI_ID}, PRC_ID={self.PRC_ID})"
