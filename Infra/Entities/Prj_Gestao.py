# infra/entities/Prj_Gestao.py
from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, DateTime

class Prj_Gestao(Base):
    __tablename__ = 'PRJ_GESTAO'

    PRJ_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRJ_TIPO = Column(String(20), nullable=False)
    PRJ_PAI = Column(Integer, nullable=True)
    PRJ_NIVEL = Column(Integer, nullable=False)
    PRJ_CODIGO = Column(String(20), nullable=False)
    PRJ_TITULO = Column(String(256), nullable=False)
    PRJ_DESCRICAO = Column(String(999))
    PRJ_RESPONS_ID = Column(Integer)
    PRJ_EXECUTORES_ID = Column(Integer)
    PRJ_PROCESSO_ID = Column(Integer)
    PRJ_AREA = Column(String(256))
    PRJ_OBSERV_HISTOR = Column(String(999))
    PRJ_DT_CRIACAO = Column(DateTime, nullable=False)
    PRJ_DT_PREVISTA = Column(DateTime)
    PRJ_DT_PRORROGADA = Column(DateTime)
    PRJ_DT_CONCLUSAO = Column(DateTime)
    PRJ_DT_EXCLUSAO = Column(DateTime)

    def __repr__(self):
        return f"Prj_Gestao(PRJ_ID={self.PRJ_ID}, PRJ_TITULO={self.PRJ_TITULO})"
