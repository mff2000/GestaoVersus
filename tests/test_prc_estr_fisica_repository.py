import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Estr_Fisica import Prc_Estr_Fisica
from infra.repository.prc_estr_fisica_repository import PrcEstrFisicaRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_estr_fisica_repository(session: Session):
    return PrcEstrFisicaRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_estr_fisica_table(session: Session):
    session.query(Prc_Estr_Fisica).delete()
    session.commit()

def test_create(prc_estr_fisica_repository: PrcEstrFisicaRepository):
    data = {
        'PRC_ESTR_FISICA_DESCR': fake.text(),
        'PRC_ESTR_FISICA_NECESSID': fake.text(),
        'PRC_ESTR_FISICA_OBSERV': fake.text(),
        'PRC_ESTR_FISICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_estr_fisica = prc_estr_fisica_repository.create(data)
    assert nova_estr_fisica.PRC_ESTR_FISICA_ID is not None
    for key, value in data.items():
        assert getattr(nova_estr_fisica, key) == value

def test_get_all(prc_estr_fisica_repository: PrcEstrFisicaRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_ESTR_FISICA_DESCR': fake.text(),
            'PRC_ESTR_FISICA_NECESSID': fake.text(),
            'PRC_ESTR_FISICA_OBSERV': fake.text(),
            'PRC_ESTR_FISICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_estr_fisica_repository.create(data)

    # Teste o método get_all
    todas_estr_fisica = prc_estr_fisica_repository.get_all()
    assert len(todas_estr_fisica) == 3

def test_get_by_id(prc_estr_fisica_repository: PrcEstrFisicaRepository):
    data = {
        'PRC_ESTR_FISICA_DESCR': fake.text(),
        'PRC_ESTR_FISICA_NECESSID': fake.text(),
        'PRC_ESTR_FISICA_OBSERV': fake.text(),
        'PRC_ESTR_FISICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_estr_fisica = prc_estr_fisica_repository.create(data)

    # Teste com um ID válido
    estr_fisica_encontrada = prc_estr_fisica_repository.get_by_id(nova_estr_fisica.PRC_ESTR_FISICA_ID)
    assert estr_fisica_encontrada == nova_estr_fisica

    # Teste com um ID inválido
    estr_fisica_nao_encontrada = prc_estr_fisica_repository.get_by_id(9999)
    assert estr_fisica_nao_encontrada is None

def test_update(prc_estr_fisica_repository: PrcEstrFisicaRepository):
    data = {
        'PRC_ESTR_FISICA_DESCR': fake.text(),
        'PRC_ESTR_FISICA_NECESSID': fake.text(),
        'PRC_ESTR_FISICA_OBSERV': fake.text(),
        'PRC_ESTR_FISICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    estr_fisica = prc_estr_fisica_repository.create(data)

    dados_atualizados = {
        'PRC_ESTR_FISICA_DESCR': fake.text(),
        'PRC_ESTR_FISICA_NECESSID': fake.text()
    }

    estr_fisica_atualizada = prc_estr_fisica_repository.update(estr_fisica.PRC_ESTR_FISICA_ID, dados_atualizados)

    assert estr_fisica_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(estr_fisica_atualizada, key) == value

def test_delete(prc_estr_fisica_repository: PrcEstrFisicaRepository):
    data = {
        'PRC_ESTR_FISICA_DESCR': fake.text(),
        'PRC_ESTR_FISICA_NECESSID': fake.text(),
        'PRC_ESTR_FISICA_OBSERV': fake.text(),
        'PRC_ESTR_FISICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    estr_fisica = prc_estr_fisica_repository.create(data)

    resultado = prc_estr_fisica_repository.delete(estr_fisica.PRC_ESTR_FISICA_ID)
    assert resultado is True

    estr_fisica_excluida = prc_estr_fisica_repository.get_by_id(estr_fisica.PRC_ESTR_FISICA_ID)
    assert estr_fisica_excluida is None
