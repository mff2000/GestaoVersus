import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Compliance import Prc_Compliance
from infra.repository.prc_compliance_repository import PrcComplianceRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_compliance_repository(session: Session):
    return PrcComplianceRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_compliance_table(session: Session):
    session.query(Prc_Compliance).delete()
    session.commit()

def test_create(prc_compliance_repository: PrcComplianceRepository):
    data = {
        'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
        'PRC_COMPLIANCE_DESCR_REGRA': fake.text(),
        'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word(),
        'PRC_COMPLIANCE_OBSERV': fake.text(),
        'PRC_COMPLIANCE_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_compliance = prc_compliance_repository.create(data)
    assert novo_compliance.PRC_COMPLIANCE_ID is not None
    for key, value in data.items():
        assert getattr(novo_compliance, key) == value

def test_get_all(prc_compliance_repository: PrcComplianceRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
            'PRC_COMPLIANCE_DESCR_REGRA': fake.text(),
            'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word(),
            'PRC_COMPLIANCE_OBSERV': fake.text(),
            'PRC_COMPLIANCE_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_compliance_repository.create(data)

    # Teste o método get_all
    todos_compliance = prc_compliance_repository.get_all()
    assert len(todos_compliance) == 3

def test_get_by_id(prc_compliance_repository: PrcComplianceRepository):
    data = {
        'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
        'PRC_COMPLIANCE_DESCR_REGRA': fake.text(),
        'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word(),
        'PRC_COMPLIANCE_OBSERV': fake.text(),
        'PRC_COMPLIANCE_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_compliance = prc_compliance_repository.create(data)

    # Teste com um ID válido
    compliance_encontrado = prc_compliance_repository.get_by_id(novo_compliance.PRC_COMPLIANCE_ID)
    assert compliance_encontrado == novo_compliance

    # Teste com um ID inválido
    compliance_nao_encontrado = prc_compliance_repository.get_by_id(9999)
    assert compliance_nao_encontrado is None

def test_update(prc_compliance_repository: PrcComplianceRepository):
    data = {
        'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
        'PRC_COMPLIANCE_DESCR_REGRA': fake.text(),
        'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word(),
        'PRC_COMPLIANCE_OBSERV': fake.text(),
        'PRC_COMPLIANCE_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    compliance = prc_compliance_repository.create(data)

    dados_atualizados = {
        'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
        'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word()
    }

    compliance_atualizado = prc_compliance_repository.update(compliance.PRC_COMPLIANCE_ID, dados_atualizados)

    assert compliance_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(compliance_atualizado, key) == value

def test_delete(prc_compliance_repository: PrcComplianceRepository):
    data = {
        'PRC_COMPLIANCE_TIPO_REGRA': fake.word(),
        'PRC_COMPLIANCE_DESCR_REGRA': fake.text(),
        'PRC_COMPLIANCE_SITUACAO_REGRA': fake.word(),
        'PRC_COMPLIANCE_OBSERV': fake.text(),
        'PRC_COMPLIANCE_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    compliance = prc_compliance_repository.create(data)

    resultado = prc_compliance_repository.delete(compliance.PRC_COMPLIANCE_ID)
    assert resultado is True

    compliance_excluido = prc_compliance_repository.get_by_id(compliance.PRC_COMPLIANCE_ID)
    assert compliance_excluido is None
