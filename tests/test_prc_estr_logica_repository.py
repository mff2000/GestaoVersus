import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Estr_Logica import Prc_Estr_Logica
from infra.repository.prc_estr_logica_repository import PrcEstrLogicaRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_estr_logica_repository(session: Session):
    return PrcEstrLogicaRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_estr_logica_table(session: Session):
    session.query(Prc_Estr_Logica).delete()
    session.commit()

def test_create(prc_estr_logica_repository: PrcEstrLogicaRepository):
    data = {
        'PRC_ESTR_LOGICA_DESCR': fake.text(),
        'PRC_ESTR_LOGICA_NECESSID': fake.text(),
        'PRC_ESTR_LOGICA_OBSERV': fake.text(),
        'PRC_ESTR_LOGICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_estr_logica = prc_estr_logica_repository.create(data)
    assert nova_estr_logica.PRC_ESTR_LOGICA_ID is not None
    for key, value in data.items():
        assert getattr(nova_estr_logica, key) == value

def test_get_all(prc_estr_logica_repository: PrcEstrLogicaRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_ESTR_LOGICA_DESCR': fake.text(),
            'PRC_ESTR_LOGICA_NECESSID': fake.text(),
            'PRC_ESTR_LOGICA_OBSERV': fake.text(),
            'PRC_ESTR_LOGICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_estr_logica_repository.create(data)

    # Teste o método get_all
    todas_estr_logica = prc_estr_logica_repository.get_all()
    assert len(todas_estr_logica) == 3

def test_get_by_id(prc_estr_logica_repository: PrcEstrLogicaRepository):
    data = {
        'PRC_ESTR_LOGICA_DESCR': fake.text(),
        'PRC_ESTR_LOGICA_NECESSID': fake.text(),
        'PRC_ESTR_LOGICA_OBSERV': fake.text(),
        'PRC_ESTR_LOGICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_estr_logica = prc_estr_logica_repository.create(data)

    # Teste com um ID válido
    estr_logica_encontrada = prc_estr_logica_repository.get_by_id(nova_estr_logica.PRC_ESTR_LOGICA_ID)
    assert estr_logica_encontrada == nova_estr_logica

    # Teste com um ID inválido
    estr_logica_nao_encontrada = prc_estr_logica_repository.get_by_id(9999)
    assert estr_logica_nao_encontrada is None

def test_update(prc_estr_logica_repository: PrcEstrLogicaRepository):
    data = {
        'PRC_ESTR_LOGICA_DESCR': fake.text(),
        'PRC_ESTR_LOGICA_NECESSID': fake.text(),
        'PRC_ESTR_LOGICA_OBSERV': fake.text(),
        'PRC_ESTR_LOGICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    estr_logica = prc_estr_logica_repository.create(data)

    dados_atualizados = {
        'PRC_ESTR_LOGICA_DESCR': fake.text(),
        'PRC_ESTR_LOGICA_NECESSID': fake.text()
    }

    estr_logica_atualizada = prc_estr_logica_repository.update(estr_logica.PRC_ESTR_LOGICA_ID, dados_atualizados)

    assert estr_logica_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(estr_logica_atualizada, key) == value

def test_delete(prc_estr_logica_repository: PrcEstrLogicaRepository):
    data = {
        'PRC_ESTR_LOGICA_DESCR': fake.text(),
        'PRC_ESTR_LOGICA_NECESSID': fake.text(),
        'PRC_ESTR_LOGICA_OBSERV': fake.text(),
        'PRC_ESTR_LOGICA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    estr_logica = prc_estr_logica_repository.create(data)

    resultado = prc_estr_logica_repository.delete(estr_logica.PRC_ESTR_LOGICA_ID)
    assert resultado is True

    estr_logica_excluida = prc_estr_logica_repository.get_by_id(estr_logica.PRC_ESTR_LOGICA_ID)
    assert estr_logica_excluida is None
