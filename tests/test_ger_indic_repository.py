import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Ger_Indic import Ger_Indic
from infra.repository.ger_indic_repository import GerIndicRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def ger_indic_repository(session: Session):
    return GerIndicRepository(session)

@pytest.fixture(autouse=True)
def clean_ger_indic_table(session: Session):
    session.query(Ger_Indic).delete()
    session.commit()

def test_create(ger_indic_repository: GerIndicRepository):
    data = {
        'GER_INDIC_TIPO': fake.word(),
        'GER_INDIC_NOME': fake.word(),
        'GER_INDIC_RESPONS': fake.name(),
        'GER_INDIC_CALCULO': fake.text(),
        'GER_INDIC_OBSERV': fake.text(),
        'GER_INDIC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_indicador = ger_indic_repository.create(data)
    assert novo_indicador.GER_INDIC_ID is not None
    for key, value in data.items():
        assert getattr(novo_indicador, key) == value

def test_get_all(ger_indic_repository: GerIndicRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'GER_INDIC_TIPO': fake.word(),
            'GER_INDIC_NOME': fake.word(),
            'GER_INDIC_RESPONS': fake.name(),
            'GER_INDIC_CALCULO': fake.text(),
            'GER_INDIC_OBSERV': fake.text(),
            'GER_INDIC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        ger_indic_repository.create(data)

    # Teste o método get_all
    todos_indicadores = ger_indic_repository.get_all()
    assert len(todos_indicadores) == 3

def test_get_by_id(ger_indic_repository: GerIndicRepository):
    data = {
        'GER_INDIC_TIPO': fake.word(),
        'GER_INDIC_NOME': fake.word(),
        'GER_INDIC_RESPONS': fake.name(),
        'GER_INDIC_CALCULO': fake.text(),
        'GER_INDIC_OBSERV': fake.text(),
        'GER_INDIC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_indicador = ger_indic_repository.create(data)

    # Teste com um ID válido
    indicador_encontrado = ger_indic_repository.get_by_id(novo_indicador.GER_INDIC_ID)
    assert indicador_encontrado == novo_indicador

    # Teste com um ID inválido
    indicador_nao_encontrado = ger_indic_repository.get_by_id(9999)
    assert indicador_nao_encontrado is None

def test_update(ger_indic_repository: GerIndicRepository):
    data = {
        'GER_INDIC_TIPO': fake.word(),
        'GER_INDIC_NOME': fake.word(),
        'GER_INDIC_RESPONS': fake.name(),
        'GER_INDIC_CALCULO': fake.text(),
        'GER_INDIC_OBSERV': fake.text(),
        'GER_INDIC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    indicador = ger_indic_repository.create(data)

    dados_atualizados = {
        'GER_INDIC_TIPO': fake.word(),
        'GER_INDIC_CALCULO': fake.text()
    }

    indicador_atualizado = ger_indic_repository.update(indicador.GER_INDIC_ID, dados_atualizados)

    assert indicador_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(indicador_atualizado, key) == value

def test_delete(ger_indic_repository: GerIndicRepository):
    data = {
        'GER_INDIC_TIPO': fake.word(),
        'GER_INDIC_NOME': fake.word(),
        'GER_INDIC_RESPONS': fake.name(),
        'GER_INDIC_CALCULO': fake.text(),
        'GER_INDIC_OBSERV': fake.text(),
        'GER_INDIC_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    indicador = ger_indic_repository.create(data)

    resultado = ger_indic_repository.delete(indicador.GER_INDIC_ID)
    assert resultado is True

    indicador_excluido = ger_indic_repository.get_by_id(indicador.GER_INDIC_ID)
    assert indicador_excluido is None
