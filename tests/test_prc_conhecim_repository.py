import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Conhec import Prc_Conhec
from infra.repository.prc_conhec_repository import PrcConhecRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_conhecim_repository(session: Session):
    return PrcConhecRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_conhecim_table(session: Session):
    session.query(Prc_Conhec).delete()
    session.commit()

def test_create(prc_conhecim_repository: PrcConhecRepository):
    data = {
        'PRC_CONHEC_TEC': fake.text(),
        'PRC_CONHEC_GEST': fake.text(),
        'PRC_CONHEC_RELAC': fake.text(),
        'PRC_CONHEC_DESCR': fake.text(),
        'PRC_CONHEC_OBSERV': fake.text(),
        'PRC_CONHEC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_conhec = prc_conhecim_repository.create(data)
    assert novo_conhec.PRC_CONHEC_ID is not None
    for key, value in data.items():
        assert getattr(novo_conhec, key) == value

def test_get_all(prc_conhecim_repository: PrcConhecRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_CONHEC_TEC': fake.text(),
            'PRC_CONHEC_GEST': fake.text(),
            'PRC_CONHEC_RELAC': fake.text(),
            'PRC_CONHEC_DESCR': fake.text(),
            'PRC_CONHEC_OBSERV': fake.text(),
            'PRC_CONHEC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_conhecim_repository.create(data)

    # Teste o método get_all
    todos_conhecimentos = prc_conhecim_repository.get_all()
    assert len(todos_conhecimentos) == 3

def test_get_by_id(prc_conhecim_repository: PrcConhecRepository):
    data = {
        'PRC_CONHEC_TEC': fake.text(),
        'PRC_CONHEC_GEST': fake.text(),
        'PRC_CONHEC_RELAC': fake.text(),
        'PRC_CONHEC_DESCR': fake.text(),
        'PRC_CONHEC_OBSERV': fake.text(),
        'PRC_CONHEC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_conhec = prc_conhecim_repository.create(data)

    # Teste com um ID válido
    conhec_encontrado = prc_conhecim_repository.get_by_id(novo_conhec.PRC_CONHEC_ID)
    assert conhec_encontrado == novo_conhec

    # Teste com um ID inválido
    conhec_nao_encontrado = prc_conhecim_repository.get_by_id(9999)
    assert conhec_nao_encontrado is None

def test_update(prc_conhecim_repository: PrcConhecRepository):
    data = {
        'PRC_CONHEC_TEC': fake.text(),
        'PRC_CONHEC_GEST': fake.text(),
        'PRC_CONHEC_RELAC': fake.text(),
        'PRC_CONHEC_DESCR': fake.text(),
        'PRC_CONHEC_OBSERV': fake.text(),
        'PRC_CONHEC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    conhec = prc_conhecim_repository.create(data)

    dados_atualizados = {
        'PRC_CONHEC_TEC': fake.text(),
        'PRC_CONHEC_GEST': fake.text()
    }

    conhec_atualizado = prc_conhecim_repository.update(conhec.PRC_CONHEC_ID, dados_atualizados)

    assert conhec_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(conhec_atualizado, key) == value

def test_delete(prc_conhecim_repository: PrcConhecRepository):
    data = {
        'PRC_CONHEC_TEC': fake.text(),
        'PRC_CONHEC_GEST': fake.text(),
        'PRC_CONHEC_RELAC': fake.text(),
        'PRC_CONHEC_DESCR': fake.text(),
        'PRC_CONHEC_OBSERV': fake.text(),
        'PRC_CONHEC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    conhec = prc_conhecim_repository.create(data)

    resultado = prc_conhecim_repository.delete(conhec.PRC_CONHEC_ID)
    assert resultado is True

    conhec_excluido = prc_conhecim_repository.get_by_id(conhec.PRC_CONHEC_ID)
    assert conhec_excluido is None
