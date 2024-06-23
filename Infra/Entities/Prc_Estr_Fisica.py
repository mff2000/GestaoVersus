# infra/entities/Prc_Estr_Fisica.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Prc_Estr_Fisica(Base):
    __tablename__ = 'PRC_ESTR_FISICA'

    PRC_ESTR_FISICA_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ESTR_FISICA_DESCR = Column(Text)
    PRC_ESTR_FISICA_NECESSID = Column(Text)
    PRC_ESTR_FISICA_OBSERV = Column(Text)
    PRC_ESTR_FISICA_DT_CRIACAO = Column(DateTime, nullable=False)
    PRC_ESTR_FISICA_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_ESTR_FISICA_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Prc_Estr_Fisica(PRC_ESTR_FISICA_ID={self.PRC_ESTR_FISICA_ID})"
