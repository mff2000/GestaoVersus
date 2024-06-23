# infra/entities/Prc_Estr_Logica.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Estr_Logica(Base):
    __tablename__ = 'PRC_ESTR_LOGICA'

    PRC_ESTR_LOGICA_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ESTR_LOGICA_DESCR = Column(Text)
    PRC_ESTR_LOGICA_NECESSID = Column(Text)
    PRC_ESTR_LOGICA_OBSERV = Column(Text)
    PRC_ESTR_LOGICA_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_ESTR_LOGICA_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_ESTR_LOGICA_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Estr_Logica(PRC_ESTR_LOGICA_ID={self.PRC_ESTR_LOGICA_ID})"
