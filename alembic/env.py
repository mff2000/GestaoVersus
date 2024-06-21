from dotenv import load_dotenv
load_dotenv()
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Adiciona o caminho da pasta entities ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'entities'))) 

# Importa a configuração de conexão e o modelo
from infra.configs.connection import DBConnectionHandler
from infra.configs.base import Base
from infra.entities.Prc_Cad import Processo  # Importe o modelo Processo


config = context.config

# Interpreta o arquivo .ini para configurar o log
fileConfig(config.config_file_name)

# Adiciona a metadada do modelo para suporte ao autogerenciamento
target_metadata = Base.metadata

# Para verificar se os modelos estão sendo detectados
print(f"Metadados detectados: {target_metadata.tables}")

def run_migrations_offline():
    """Executa migrações no modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa migrações no modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
