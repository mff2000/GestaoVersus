from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP

# Definir a classe para a tabela Prc_Cad
class Prc_Cad(Base):
    __tablename__ = 'Prc_Cad'
    
    PRC_id = Column(Integer, primary_key=True, autoincrement=True)  # Corrigido para autoincrement
    PRC_TIPO = Column(String(20))  # Tamanho máximo definido
    PRC_PAI = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_NIVEL = Column(Integer)
    PRC_CODIGO = Column(String(20))  # Tamanho máximo definido
    PRC_NOME = Column(String(256))  # Tamanho máximo definido
    PRC_GERENCIAM = Column(String(256))  # Tamanho máximo definido
    PRC_MISSAO = Column(String(999))  # Tamanho máximo definido
    PRC_DONO_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_EXIG_QUALID = Column(String(999))  # Tamanho máximo definido
    PRC_INDICE_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ENTREGA_CLI_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_TIME_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_CONHEC_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ESTR_FISICA_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ESTR_LOGICA_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_MODELAGEM_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ROTINA_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_CAPAC_OPERAC_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_FORNE_ITENS_CONS_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ANALISE_CUSTOS_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_COMPLIANCE_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_AUDITORIA_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    TESTEMFF = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_DT_CADASTRO = Column(TIMESTAMP)
    PRC_DT_ALTERACAO = Column(TIMESTAMP)
    PRC_DT_EXCLUSAO = Column(TIMESTAMP)

    def __repr__(self):
        return f"Cadastro de Processo [PRC_id={self.PRC_id}, PRC_TIPO={self.PRC_TIPO}, PRC_PAI={self.PRC_PAI}, PRC_NIVEL={self.PRC_NIVEL}, PRC_CODIGO={self.PRC_CODIGO}, PRC_NOME={self.PRC_NOME}, PRC_GERENCIAM={self.PRC_GERENCIAM}, PRC_MISSAO={self.PRC_MISSAO}, PRC_DONO_ID={self.PRC_DONO_ID}, PRC_EXIG_QUALID={self.PRC_EXIG_QUALID}, PRC_INDICE_ID={self.PRC_INDICE_ID}, PRC_ENTREGA_CLI_ID={self.PRC_ENTREGA_CLI_ID}, PRC_TIME_ID={self.PRC_TIME_ID}, PRC_CONHEC_ID={self.PRC_CONHEC_ID}, PRC_ESTR_FISICA_ID={self.PRC_ESTR_FISICA_ID}, PRC_ESTR_LOGICA_ID={self.PRC_ESTR_LOGICA_ID}, PRC_MODELAGEM_ID={self.PRC_MODELAGEM_ID}, PRC_ROTINA_ID={self.PRC_ROTINA_ID}, PRC_CAPAC_OPERAC_ID={self.PRC_CAPAC_OPERAC_ID}, PRC_FORNE_ITENS_CONS_ID={self.PRC_FORNE_ITENS_CONS_ID}, PRC_ANALISE_CUSTOS_ID={self.PRC_ANALISE_CUSTOS_ID}, PRC_COMPLIANCE_ID={self.PRC_COMPLIANCE_ID}, PRC_AUDITORIA_ID={self.PRC_AUDITORIA_ID}, PRC_DT_CADASTRO={self.PRC_DT_CADASTRO}, PRC_DT_ALTERACAO={self.PRC_DT_ALTERACAO}, PRC_DT_EXCLUSAO={self.PRC_DT_EXCLUSAO}]"
