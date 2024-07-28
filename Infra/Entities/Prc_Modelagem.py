# infra/entities/prc_modelagem.py

from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship  # Para relacionamentos (opcional)

class Prc_Modelagem(Base):
    """
    Representa uma etapa de modelagem em um processo.
    """

    __tablename__ = 'PRC_MODELAGEM'

    PRC_MODELAGEM_ID = Column(Integer, primary_key=True, autoincrement=True)  # ID da etapa
    PRC_MODELAGEM_ID_PROCESSO = Column(Integer, nullable=False)  # ID do processo
    PRC_MODELAGEM_ORDEM_ATIVIDADE = Column(Integer, nullable=False)  # Número da etapa
    PRC_MODELAGEM_NOME_ATIVIDADE = Column(String(256), nullable=False)  # Nome detalhado da etapa
    PRC_MODELAGEM_DESCR_ATIVIDADE = Column(String(512))  # Descrição da etapa (opcional)
    PRC_MODELAGEM_TIME_RESP_ID = Column(Integer, nullable=False)  # ID do time (opcional)
    PRC_MODELAGEM_EH_PONTO_DECISAO = Column(Boolean, default=False)  # Ponto de decisão?
    PRC_MODELAGEM_POP = Column(String(256))
    PRC_MODELAGEM_VIDEO = Column(String(256))
    PRC_MODELAGEM_DATA_CRIACAO = Column(DateTime, nullable=False)
    PRC_MODELAGEM_DATA_ALTERACAO = Column(DateTime)
    PRC_MODELAGEM_DATA_EXCLUSAO = Column(DateTime)

    # Relacionamento com o time (opcional)
    # time_responsavel = relationship("Ger_Time", backref="PRC_MODELAGEM_TIME_RESP_ID")  

    def __repr__(self):
        return f"PrcModelagem(id={self.id}, nome='{self.nome}', numero_etapa={self.numero_etapa})"
