import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Rotina import Prc_Rotina
from infra.repository.prc_rotina_repository import PrcRotinaRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_rotina_repository(session: Session):
    return PrcRotinaRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_rotina_table(session: Session):
    session.query(Prc_Rotina).delete()
    session.commit()

def test_create(prc_rotina_repository: PrcRotinaRepository):
    data = {
        'PRC_ROTINA_TIPO': fake.word(),
        'PRC_ROTINA_START': fake.word(),
        'PRC_ROTINA_DESCR': fake.text(),
        'PRC_ROTINA_OBSERV': fake.text(),
        'PRC_ROTINA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_rotina = prc_rotina_repository.create(data)
    assert nova_rotina.PRC_ROTINA_ID is not None
    for key, value in data.items():
        assert getattr(nova_rotina, key) == value

def test_get_all(prc_rotina_repository: PrcRotinaRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_ROTINA_TIPO': fake.word(),
            'PRC_ROTINA_START': fake.word(),
            'PRC_ROTINA_DESCR': fake.text(),
            'PRC_ROTINA_OBSERV': fake.text(),
            'PRC_ROTINA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_rotina_repository.create(data)

    # Teste o método get_all
    todas_rotinas = prc_rotina_repository.get_all()
    assert len(todas_rotinas) == 3

def test_get_by_id(prc_rotina_repository: PrcRotinaRepository):
    data = {
        'PRC_ROTINA_TIPO': fake.word(),
        'PRC_ROTINA_START': fake.word(),
        'PRC_ROTINA_DESCR': fake.text(),
        'PRC_ROTINA_OBSERV': fake.text(),
        'PRC_ROTINA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_rotina = prc_rotina_repository.create(data)

    # Teste com um ID válido
    rotina_encontrada = prc_rotina_repository.get_by_id(nova_rotina.PRC_ROTINA_ID)
    assert rotina_encontrada == nova_rotina

    # Teste com um ID inválido
    rotina_nao_encontrada = prc_rotina_repository.get_by_id(9999)
    assert rotina_nao_encontrada is None

def test_update(prc_rotina_repository: PrcRotinaRepository):
    data = {
        'PRC_ROTINA_TIPO': fake.word(),
        'PRC_ROTINA_START': fake.word(),
        'PRC_ROTINA_DESCR': fake.text(),
        'PRC_ROTINA_OBSERV': fake.text(),
        'PRC_ROTINA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    rotina = prc_rotina_repository.create(data)

    dados_atualizados = {
        'PRC_ROTINA_TIPO': fake.word(),
        'PRC_ROTINA_DESCR': fake.text()
    }

    rotina_atualizada = prc_rotina_repository.update(rotina.PRC_ROTINA_ID, dados_atualizados)

    assert rotina_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(rotina_atualizada, key) == value

def test_delete(prc_rotina_repository: PrcRotinaRepository):
    data = {
        'PRC_ROTINA_TIPO': fake.word(),
        'PRC_ROTINA_START': fake.word(),
        'PRC_ROTINA_DESCR': fake.text(),
        'PRC_ROTINA_OBSERV': fake.text(),
        'PRC_ROTINA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    rotina = prc_rotina_repository.create(data)

    resultado = prc_rotina_repository.delete(rotina.PRC_ROTINA_ID)
    assert resultado is True

    rotina_excluida = prc_rotina_repository.get_by_id(rotina.PRC_ROTINA_ID)
    assert rotina_excluida is None
