import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Capac_Operac import Prc_Capac_Operac
from infra.repository.prc_cap_operac_repository import PrcCapacOperacRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_cap_operac_repository(session: Session):
    return PrcCapacOperacRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_cap_operac_table(session: Session):
    session.query(Prc_Capac_Operac).delete()
    session.commit()

def test_create(prc_cap_operac_repository: PrcCapacOperacRepository):
    data = {
        'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
        'PRC_CAPAC_OPERAC_UN_MED': fake.word(),
        'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat()),
        'PRC_CAPAC_OPERAC_DESCR': fake.text(),
        'PRC_CAPAC_OPERAC_OBSERV': fake.text(),
        'PRC_CAPAC_OPERAC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    nova_capac_operac = prc_cap_operac_repository.create(data)

    assert nova_capac_operac.PRC_CAPAC_OPERAC_ID is not None
    for key, value in data.items():
        assert getattr(nova_capac_operac, key) == value

def test_get_all(prc_cap_operac_repository: PrcCapacOperacRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
            'PRC_CAPAC_OPERAC_UN_MED': fake.word(),
            'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat()),
            'PRC_CAPAC_OPERAC_DESCR': fake.text(),
            'PRC_CAPAC_OPERAC_OBSERV': fake.text(),
            'PRC_CAPAC_OPERAC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_cap_operac_repository.create(data)

    # Teste o método get_all
    todas_capac_operac = prc_cap_operac_repository.get_all()
    assert len(todas_capac_operac) == 3

def test_get_by_id(prc_cap_operac_repository: PrcCapacOperacRepository):
    data = {
        'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
        'PRC_CAPAC_OPERAC_UN_MED': fake.word(),
        'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat()),
        'PRC_CAPAC_OPERAC_DESCR': fake.text(),
        'PRC_CAPAC_OPERAC_OBSERV': fake.text(),
        'PRC_CAPAC_OPERAC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_capac_operac = prc_cap_operac_repository.create(data)

    # Teste com um ID válido
    capac_operac_encontrada = prc_cap_operac_repository.get_by_id(nova_capac_operac.PRC_CAPAC_OPERAC_ID)
    assert capac_operac_encontrada == nova_capac_operac

    # Teste com um ID inválido
    capac_operac_nao_encontrada = prc_cap_operac_repository.get_by_id(9999)
    assert capac_operac_nao_encontrada is None

def test_update(prc_cap_operac_repository: PrcCapacOperacRepository):
    data = {
        'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
        'PRC_CAPAC_OPERAC_UN_MED': fake.word(),
        'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat()),
        'PRC_CAPAC_OPERAC_DESCR': fake.text(),
        'PRC_CAPAC_OPERAC_OBSERV': fake.text(),
        'PRC_CAPAC_OPERAC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    capac_operac = prc_cap_operac_repository.create(data)

    dados_atualizados = {
        'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
        'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat())
    }

    capac_operac_atualizada = prc_cap_operac_repository.update(capac_operac.PRC_CAPAC_OPERAC_ID, dados_atualizados)

    assert capac_operac_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(capac_operac_atualizada, key) == value

def test_delete(prc_cap_operac_repository: PrcCapacOperacRepository):
    data = {
        'PRC_CAPAC_OPERAC_ELEMEN': fake.word(),
        'PRC_CAPAC_OPERAC_UN_MED': fake.word(),
        'PRC_CAPAC_OPERAC_VALOR': str(fake.pyfloat()),
        'PRC_CAPAC_OPERAC_DESCR': fake.text(),
        'PRC_CAPAC_OPERAC_OBSERV': fake.text(),
        'PRC_CAPAC_OPERAC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    capac_operac = prc_cap_operac_repository.create(data)

    resultado = prc_cap_operac_repository.delete(capac_operac.PRC_CAPAC_OPERAC_ID)
    assert resultado is True

    capac_operac_excluida = prc_cap_operac_repository.get_by_id(capac_operac.PRC_CAPAC_OPERAC_ID)
    assert capac_operac_excluida is None

