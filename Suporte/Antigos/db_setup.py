# db_setup.py

from sqlalchemy import MetaData, Table, Column, String, Integer, Date, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from conexao import get_database_url  # Atualizado a importação

# Configurar o engine para criar o banco de dados utilizando PostgreSQL
engine = create_engine(get_database_url())

# Criar metadados para as tabelas
metadata = MetaData()

# Base declarativa para mapeamento ORM
Base = declarative_base()

# Definir a classe Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)

# Definir a tabela PRC_CAD
tabela_prc_cad = Table(
    "PRC_CAD",
    metadata,
    Column("PRC_CAD", Integer, primary_key=True, autoincrement=True),
    Column("PRC_TIPO", String(20), nullable=False),
    Column("PRC_PAI", Integer, nullable=True),
    Column("PRC_NIVEL", Integer, nullable=False),
    Column("PRC_CODIGO", String(20), nullable=False),
    Column("PRC_NOME", String(256), nullable=False),
    Column("PRC_GERENCIAM", String(256), nullable=True),
    Column("PRC_MISSAO", String(999), nullable=True),
    Column("PRC_DONO_ID", Integer, nullable=True),
    Column("PRC_EXIG_QUALID", String(999), nullable=True),
    Column("PRC_INDIC_ID", Integer, nullable=True),
    Column("PRC_ENTREGA_CLI_ID", Integer, nullable=True),
    Column("PRC_TIME_ID", Integer, nullable=True),
    Column("PRC_CONHEC_ID", Integer, nullable=True),
    Column("PRC_ESTR_FISICA_ID", Integer, nullable=True),
    Column("PRC_ESTR_LOGICA_ID", Integer, nullable=True),
    Column("PRC_MODELAGEM_ID", Integer, nullable=True),
    Column("PRC_ROTINA_ID", Integer, nullable=True),
    Column("PRC_CAPAC_OPERAC_ID", Integer, nullable=True),
    Column("PRC_FORNE_ITENS_CONS_ID", Integer, nullable=True),
    Column("PRC_ANALISE_CUSTOS_ID", Integer, nullable=True),
    Column("PRC_COMPLIANCE_ID", Integer, nullable=True),
    Column("PRC_AUDITORIA_ID", Integer, nullable=True),
    Column("PRC_DT_CADASTRO", Date, nullable=False),
    Column("PRC_DT_ALTERACAO", Date),
    Column("PRC_DT_EXCLUSAO", Date),
)

# Criar todas as tabelas no banco de dados
metadata.create_all(engine)
Base.metadata.create_all(engine)

# Crie uma fábrica de sessões
Session = sessionmaker(bind=engine)
