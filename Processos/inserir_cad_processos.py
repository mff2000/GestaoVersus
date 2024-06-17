import MySQLdb
import sys
from pathlib import Path


# Parâmetros de conexão

sys.path.append(str(Path('c:/gestaoversus/bd').resolve()))
from conexao_bd import connect_db

# Importar a engine do arquivo de conexão
from conexao_bd import engine, Base

# Definir a classe para a tabela GER_USUARIOS
class Processo(Base):
    __tablename__ = 'CAD_PROCESSOS'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Corrigido para autoincrement
    PRC_TIPO = Column(VARCHAR(20))  # Tamanho máximo definido
    PRC_PAI = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_NIVEL = Column(Integer)
    PRC_CODIGO = Column(VARCHAR(20))  # Tamanho máximo definido
    PRC_NOME = Column(VARCHAR(256))  # Tamanho máximo definido
    PRC_GERENCIAM = Column(VARCHAR(256))  # Tamanho máximo definido
    PRC_MISSAO = Column(VARCHAR(999))  # Tamanho máximo definido
    PRC_DONO_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_EXIG_QUALID = Column(VARCHAR(999))  # Tamanho máximo definido
    PRC_INDIC_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_ENTREGA_CLI_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_TIME_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    PRC_CONHEC_ID = Column(Integer, nullable=True)  # Aceita valores nulos
    # ... (outras colunas com os mesmos ajustes)
    PRC_DT_CADASTRO = Column(TIMESTAMP)
    PRC_DT_ALTERACAO = Column(TIMESTAMP)
    PRC_DT_EXCLUSAO = Column(TIMESTAMP)

# Cria a tabela se ela não existir
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar um novo processo
novo_processo = Processo(
    PRC_TIPO= "Tipo 1",  # String para VARCHAR
    PRC_PAI= None,
    PRC_NIVEL = 1,
    PRC_CODIGO = "COD001",  # String para VARCHAR
    PRC_NOME = "Processo Teste",
    PRC_GERENCIAM = "Gerencia 2",  # String para VARCHAR
    PRC_MISSAO = "Missão do Processo Versão 01",
    PRC_DONO_ID = 1,
    PRC_EXIG_QUALID = "É exigido a qualidade de 3,6 erro por milhão",
    PRC_INDIC_ID = 3,
    PRC_ENTREGA_CLI_ID = 1,  # Valor numérico para INT
    PRC_TIME_ID = 1,
    PRC_CONHEC_ID = 2,
    PRC_ESTR_FISICA_ID = 6,
    PRC_ESTR_LOGICA_ID = 7,
    PRC_MODELAGEM_ID = 4,
    PRC_ROTINA_ID = 5,
    PRC_CAPAC_OPERAC_ID = 2,
    PRC_FORNE_ITENS_CONS_ID = 6,
    PRC_ANALISE_CUSTOS_ID = 999,
    PRC_COMPLIANCE_ID = 99,
    PRC_AUDITORIA_ID = 121,
    PRC_DT_CADASTRO = datetime.strptime('08/06/2024', '%d/%m/%Y')
)

# Adicionar o novo processo à sessão e commitar para o banco de dados
session.add(novo_processo)
session.commit()

# Fechar a sessão
session.close()
