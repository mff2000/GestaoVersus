from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from infra.configs.base import Base

class Prc_Cad(Base):
    __tablename__ = 'PRC_CAD'

    PRC_ID = Column(Integer, primary_key=True, autoincrement=True)
    PRC_CODIGO = Column(String(19), nullable=True)
    PRC_MP_PAI = Column(Integer, nullable=True)  # Adicionado nullable=True para consistência
    PRC_NIVEL = Column(Integer)
    PRC_NOME = Column(String(256))
    PRC_OBJETIVO = Column(String(512), nullable=True)

    PRC_CONHEC_TEC_NOTA = Column(Integer, nullable=True)
    PRC_CONHEC_GEST_NOTA = Column(Integer, nullable=True)
    PRC_CONHEC_RELAC_NOTA = Column(Integer, nullable=True)
    PRC_CONHEC_DESC_OBS = Column(String(512), nullable=True)

    PRC_ESTR_FISICA_NOTA = Column(Integer, nullable=True)
    PRC_ESTR_FISICA_DESCR = Column(String(512), nullable=True)
    PRC_ESTR_LOGICA_NOTA = Column(Integer, nullable=True)
    PRC_ESTR_LOGICA_DESCR = Column(String(512), nullable=True)

    PRC_TIME_ID = Column(Integer, nullable=True)
    PRC_ROTINA_ID = Column(Integer, nullable=True)

    PRC_COMPLIANCE_ID = Column(Integer, nullable=True)
    PRC_AUDITORIA_ID = Column(Integer, nullable=True)

    PRC_MODELAGEM_ID = Column(Integer, nullable=True)  #Sem uso por enquanto, será utilizada quando a tabela Prc_Modelagem começar a ser usada.
    PRC_RECURSOS_UTILIZ_ID = Column(Integer, nullable=True)  # Adicionado nullable=True para consistência
    PRC_FORNE_ITENS_CONS = Column(String(256), nullable=True)

    PRC_FLUXO_PROC = Column(String(256), nullable=True)
    PRC_POP_PROCESSO = Column(String(256), nullable=True)
    PRC_MODELAGEM_STATUS = Column(String(256), nullable=True)

    PRC_DT_CADASTRO = Column(DateTime, nullable=False)  # Corrigido para nullable=False
    PRC_DT_ALTERACAO = Column(DateTime, nullable=True)
    PRC_DT_EXCLUSAO = Column(DateTime, nullable=True)

    def __repr__(self):
        # Ajustado para incluir apenas as colunas existentes
        return f"Prc_Cad(PRC_id={self.PRC_id}, PRC_CODIGO={self.PRC_CODIGO}, PRC_MP_PAI={self.PRC_MP_PAI}, PRC_NIVEL={self.PRC_NIVEL}, PRC_NOME={self.PRC_NOME}, PRC_OBJETIVO={self.PRC_OBJETIVO}, ...)" 