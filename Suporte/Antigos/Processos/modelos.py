from sqlalchemy import MetaData, Table, Column, String, Integer, Date, create_engine

# Configurar o engine para criar o banco de dados na pasta especificada
engine = create_engine('sqlite:///c:/GestaoVersus/BD/gestao_versus.db')

# Criar metadados para as tabelas
metadata = MetaData()

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
