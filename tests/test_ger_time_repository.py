import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Ger_Time import Ger_Time
from infra.repository.ger_time_repository import GerTimeRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def ger_time_repository(session: Session):
    return GerTimeRepository(session)

@pytest.fixture(autouse=True)  # Limpa a tabela antes de cada teste
def clean_ger_time_table(session: Session):
    session.query(Ger_Time).delete()
    session.commit()

def test_create(ger_time_repository: GerTimeRepository):
    data = {
        'GER_TIME_NOME': fake.company(),
        'GER_TIME_SIGLA': fake.lexify(text='???'),  # Gera uma sigla de 3 letras
        'GER_TIME_LIDER_ID': None,  # Ou gere um ID válido se tiver a tabela GER_USUARIOS
        'GER_TIME_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    novo_time = ger_time_repository.create(data)

    assert novo_time.GER_TIME_ID is not None
    for key, value in data.items():
        assert getattr(novo_time, key) == value

def test_get_all(ger_time_repository: GerTimeRepository):
    for _ in range(3):
        ger_time_repository.create({
            'GER_TIME_NOME': fake.company(),
            'GER_TIME_SIGLA': fake.lexify(text='???'),
            'GER_TIME_LIDER_ID': None,
            'GER_TIME_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        })

    times = ger_time_repository.get_all()
    assert len(times) == 3

def test_get_by_id(ger_time_repository: GerTimeRepository):
    data = {
        'GER_TIME_NOME': fake.company(),
        'GER_TIME_SIGLA': fake.lexify(text='???'),
        'GER_TIME_LIDER_ID': None,
        'GER_TIME_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_time = ger_time_repository.create(data)

    time_encontrado = ger_time_repository.get_by_id(novo_time.GER_TIME_ID)
    assert time_encontrado == novo_time

    time_nao_encontrado = ger_time_repository.get_by_id(9999)  # ID inexistente
    assert time_nao_encontrado is None

def test_update(ger_time_repository: GerTimeRepository):
    data = {
        'GER_TIME_NOME': fake.company(),
        'GER_TIME_SIGLA': fake.lexify(text='???'),
        'GER_TIME_LIDER_ID': None,
        'GER_TIME_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    time = ger_time_repository.create(data)

    dados_atualizados = {
        'GER_TIME_NOME': fake.company(),
        'GER_TIME_SIGLA': fake.lexify(text='???')
    }

    time_atualizado = ger_time_repository.update(time.GER_TIME_ID, dados_atualizados)

    assert time_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(time_atualizado, key) == value

def test_delete(ger_time_repository: GerTimeRepository):
    data = {
        'GER_TIME_NOME': fake.company(),
        'GER_TIME_SIGLA': fake.lexify(text='???'),
        'GER_TIME_LIDER_ID': None,
        'GER_TIME_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    time = ger_time_repository.create(data)

    resultado = ger_time_repository.delete(time.GER_TIME_ID)
    assert resultado is True

    time_excluido = ger_time_repository.get_by_id(time.GER_TIME_ID)
    assert time_excluido is None
