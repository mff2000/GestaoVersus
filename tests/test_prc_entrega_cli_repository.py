import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Entrega_Cli import Prc_Entrega_Cli
from infra.repository.prc_entrega_cli_repository import PrcEntregaCliRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_entrega_cli_repository(session: Session):
    return PrcEntregaCliRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_entrega_cli_table(session: Session):
    session.query(Prc_Entrega_Cli).delete()
    session.commit()

def test_create(prc_entrega_cli_repository: PrcEntregaCliRepository):
    data = {
        'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
        'PRC_ENTREGA_CLI_DESCR': fake.text(),
        'PRC_ENTREGA_CLI_OBSERV': fake.text(),
        'PRC_ENTREGA_CLI_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_entrega_cli = prc_entrega_cli_repository.create(data)
    assert nova_entrega_cli.PRC_ENTREGA_CLI_ID is not None
    for key, value in data.items():
        assert getattr(nova_entrega_cli, key) == value

def test_get_all(prc_entrega_cli_repository: PrcEntregaCliRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
            'PRC_ENTREGA_CLI_DESCR': fake.text(),
            'PRC_ENTREGA_CLI_OBSERV': fake.text(),
            'PRC_ENTREGA_CLI_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_entrega_cli_repository.create(data)

    # Teste o método get_all
    todas_entregas_cli = prc_entrega_cli_repository.get_all()
    assert len(todas_entregas_cli) == 3

def test_get_by_id(prc_entrega_cli_repository: PrcEntregaCliRepository):
    data = {
        'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
        'PRC_ENTREGA_CLI_DESCR': fake.text(),
        'PRC_ENTREGA_CLI_OBSERV': fake.text(),
        'PRC_ENTREGA_CLI_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_entrega_cli = prc_entrega_cli_repository.create(data)

    # Teste com um ID válido
    entrega_cli_encontrada = prc_entrega_cli_repository.get_by_id(nova_entrega_cli.PRC_ENTREGA_CLI_ID)
    assert entrega_cli_encontrada == nova_entrega_cli

    # Teste com um ID inválido
    entrega_cli_nao_encontrada = prc_entrega_cli_repository.get_by_id(9999)
    assert entrega_cli_nao_encontrada is None

def test_update(prc_entrega_cli_repository: PrcEntregaCliRepository):
    data = {
        'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
        'PRC_ENTREGA_CLI_DESCR': fake.text(),
        'PRC_ENTREGA_CLI_OBSERV': fake.text(),
        'PRC_ENTREGA_CLI_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    entrega_cli = prc_entrega_cli_repository.create(data)

    dados_atualizados = {
        'PRC_ENTREGA_CLI_DESCR': fake.text(),
        'PRC_ENTREGA_CLI_OBSERV': fake.text()
    }

    entrega_cli_atualizada = prc_entrega_cli_repository.update(entrega_cli.PRC_ENTREGA_CLI_ID, dados_atualizados)

    assert entrega_cli_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(entrega_cli_atualizada, key) == value

def test_delete(prc_entrega_cli_repository: PrcEntregaCliRepository):
    data = {
        'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
        'PRC_ENTREGA_CLI_DESCR': fake.text(),
        'PRC_ENTREGA_CLI_OBSERV': fake.text(),
        'PRC_ENTREGA_CLI_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    entrega_cli = prc_entrega_cli_repository.create(data)

    resultado = prc_entrega_cli_repository.delete(entrega_cli.PRC_ENTREGA_CLI_ID)
    assert resultado is True

    entrega_cli_excluida = prc_entrega_cli_repository.get_by_id(entrega_cli.PRC_ENTREGA_CLI_ID)
    assert entrega_cli_excluida is None
