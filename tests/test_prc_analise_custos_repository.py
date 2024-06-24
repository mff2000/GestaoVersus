import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Analise_Custos import Prc_Analise_Custos
from infra.repository.prc_analise_custos_repository import PrcAnaliseCustosRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_analise_custos_repository(session: Session):
    return PrcAnaliseCustosRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_analise_custos_table(session: Session):
    session.query(Prc_Analise_Custos).delete()
    session.commit()

def test_create(prc_analise_custos_repository: PrcAnaliseCustosRepository):
    data = {
        'PRC_ID': 1,  # Substitua por um ID válido de Prc_Cad
        'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_TOTAL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_GASTOS_GERAIS': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_INVESTIMENTO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_LUCRO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_ROIC': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text(),
        'PRC_ANALISE_CUSTOS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    nova_analise_custos = prc_analise_custos_repository.create(data)

    assert nova_analise_custos.PRC_ANALISE_CUSTOS_ID is not None
    for key, value in data.items():
        assert getattr(nova_analise_custos, key) == value

def test_get_all(prc_analise_custos_repository: PrcAnaliseCustosRepository):
    expected_analises = []

    for _ in range(3):
        data = {
            'PRC_ID': 1,
            'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_CUSTO_TOTAL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_GASTOS_GERAIS': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_INVESTIMENTO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_LUCRO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_ROIC': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text(),
            'PRC_ANALISE_CUSTOS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        created_analise = prc_analise_custos_repository.create(data)
        expected_analises.append(created_analise)

    analises = prc_analise_custos_repository.get_all()

    assert len(analises) == len(expected_analises), f"Esperado {len(expected_analises)} registros, mas obtido {len(analises)}"
    for analise in expected_analises:
        assert analise in analises

def test_get_by_id(prc_analise_custos_repository: PrcAnaliseCustosRepository):
    data = {
        'PRC_ID': 1,
        'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_TOTAL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_GASTOS_GERAIS': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_INVESTIMENTO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_LUCRO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_ROIC': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text(),
        'PRC_ANALISE_CUSTOS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_analise = prc_analise_custos_repository.create(data)
    analise_by_id = prc_analise_custos_repository.get_by_id(created_analise.PRC_ANALISE_CUSTOS_ID)

    assert analise_by_id is not None
    assert analise_by_id.PRC_ANALISE_CUSTOS_ID == created_analise.PRC_ANALISE_CUSTOS_ID
    for key, value in data.items():
        assert getattr(analise_by_id, key) == value

def test_update(prc_analise_custos_repository: PrcAnaliseCustosRepository):
    data = {
        'PRC_ID': 1,
        'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_TOTAL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_GASTOS_GERAIS': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_INVESTIMENTO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_LUCRO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_ROIC': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text(),
        'PRC_ANALISE_CUSTOS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_analise = prc_analise_custos_repository.create(data)

    updated_data = {
        'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text()
    }

    updated_analise = prc_analise_custos_repository.update(created_analise.PRC_ANALISE_CUSTOS_ID, updated_data)

    assert updated_analise is not None
    assert updated_analise.PRC_ANALISE_CUSTOS_ID == created_analise.PRC_ANALISE_CUSTOS_ID
    for key, value in updated_data.items():
        assert getattr(updated_analise, key) == value

def test_delete(prc_analise_custos_repository: PrcAnaliseCustosRepository):
    data = {
        'PRC_ID': 1,
        'PRC_ANALISE_CUSTOS_CUSTO_FIXO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_VARIAVEL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_CUSTO_TOTAL': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_GASTOS_GERAIS': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_INVESTIMENTO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_LUCRO': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_ROIC': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        'PRC_ANALISE_CUSTOS_OBSERVACOES': fake.text(),
        'PRC_ANALISE_CUSTOS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_analise = prc_analise_custos_repository.create(data)
    delete_result = prc_analise_custos_repository.delete(created_analise.PRC_ANALISE_CUSTOS_ID)

    assert delete_result == True

    analise_by_id = prc_analise_custos_repository.get_by_id(created_analise.PRC_ANALISE_CUSTOS_ID)
    assert analise_by_id is None
