import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Auditoria_Tipo import Prc_Auditoria
from infra.repository.prc_auditoria_repository import PrcAuditoriaRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_auditoria_repository(session: Session):
    return PrcAuditoriaRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_auditoria_table(session: Session):
    session.query(Prc_Auditoria).delete()
    session.commit()

def test_create(prc_auditoria_repository: PrcAuditoriaRepository):
    data = {
        'PRC_AUDITORIA_TIPO': fake.word(),
        'PRC_AUDITORIA_PERIODIC': fake.word(),
        'PRC_AUDITORIA_DESCRICAO': fake.text(),
        'PRC_AUDITORIA_OBSERV': fake.text(),
        'PRC_AUDITORIA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    nova_auditoria = prc_auditoria_repository.create(data)

    assert nova_auditoria.PRC_AUDITORIA_ID is not None
    for key, value in data.items():
        assert getattr(nova_auditoria, key) == value

def test_get_all(prc_auditoria_repository: PrcAuditoriaRepository):
    for _ in range(3):
        prc_auditoria_repository.create({
            'PRC_AUDITORIA_TIPO': fake.word(),
            'PRC_AUDITORIA_PERIODIC': fake.word(),
            'PRC_AUDITORIA_DESCRICAO': fake.text(),
            'PRC_AUDITORIA_OBSERV': fake.text(),
            'PRC_AUDITORIA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        })

    auditorias = prc_auditoria_repository.get_all()
    assert len(auditorias) == 3

def test_get_by_id(prc_auditoria_repository: PrcAuditoriaRepository):
    data = {
        'PRC_AUDITORIA_TIPO': fake.word(),
        'PRC_AUDITORIA_PERIODIC': fake.word(),
        'PRC_AUDITORIA_DESCRICAO': fake.text(),
        'PRC_AUDITORIA_OBSERV': fake.text(),
        'PRC_AUDITORIA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_auditoria = prc_auditoria_repository.create(data)

    auditoria_encontrada = prc_auditoria_repository.get_by_id(nova_auditoria.PRC_AUDITORIA_ID)
    assert auditoria_encontrada == nova_auditoria

    auditoria_nao_encontrada = prc_auditoria_repository.get_by_id(9999)  # ID inexistente
    assert auditoria_nao_encontrada is None

def test_update(prc_auditoria_repository: PrcAuditoriaRepository):
    data = {
        'PRC_AUDITORIA_TIPO': fake.word(),
        'PRC_AUDITORIA_PERIODIC': fake.word(),
        'PRC_AUDITORIA_DESCRICAO': fake.text(),
        'PRC_AUDITORIA_OBSERV': fake.text(),
        'PRC_AUDITORIA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    auditoria = prc_auditoria_repository.create(data)

    dados_atualizados = {
        'PRC_AUDITORIA_TIPO': fake.word(),
        'PRC_AUDITORIA_OBSERV': fake.text()
    }

    auditoria_atualizada = prc_auditoria_repository.update(auditoria.PRC_AUDITORIA_ID, dados_atualizados)

    assert auditoria_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(auditoria_atualizada, key) == value

def test_delete(prc_auditoria_repository: PrcAuditoriaRepository):
    data = {
        'PRC_AUDITORIA_TIPO': fake.word(),
        'PRC_AUDITORIA_PERIODIC': fake.word(),
        'PRC_AUDITORIA_DESCRICAO': fake.text(),
        'PRC_AUDITORIA_OBSERV': fake.text(),
        'PRC_AUDITORIA_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    auditoria = prc_auditoria_repository.create(data)

    resultado = prc_auditoria_repository.delete(auditoria.PRC_AUDITORIA_ID)
    assert resultado is True

    auditoria_excluida = prc_auditoria_repository.get_by_id(auditoria.PRC_AUDITORIA_ID)
    assert auditoria_excluida is None
