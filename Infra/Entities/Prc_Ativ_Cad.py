from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, DateTime

class Prc_Ativ_Cad(Base):
    __tablename__ = 'PRC_ATIV_CAD'

    PRC_ATIV_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_ID = Column(Integer, nullable=False)
    PRC_ATIV_CODIGO = Column(String(20), nullable=False)
    PRC_ATIV_TITULO = Column(String(256), nullable=False)
    PRC_ATIV_ANEXOS = Column(String(256))  
    PRC_ATIV_OBS = Column(String(999))  
    PRC_ATIV_TIME_ID = Column(Integer)
    PRC_ATIV_DT_CADASTRO = Column(DateTime, nullable=False)  
    PRC_ATIV_DT_ALTERACAO = Column(DateTime)
    PRC_ATIV_DT_EXCLUSAO = Column(DateTime)

    def __repr__(self):
        return f"Prc_Ativ_Cad(PRC_ATIV_ID={self.PRC_ATIV_ID}, PRC_ID={self.PRC_ID}, PRC_ATIV_CODIGO={self.PRC_ATIV_CODIGO}, PRC_ATIV_TITULO={self.PRC_ATIV_TITULO})"