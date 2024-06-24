import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Ativ_Cad import Prc_Ativ_Cad
from infra.entities.Prc_Cad import Prc_Cad
from infra.repository.prc_ativ_cad_repository import PrcAtivCadRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_ativ_cad_repository(session: Session):
    return PrcAtivCadRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_ativ_cad_table(session: Session):
    session.query(Prc_Ativ_Cad).delete()
    session.commit()

def test_create(prc_ativ_cad_repository: PrcAtivCadRepository, session: Session):
    # Verifica se existe um registro válido na tabela Prc_Cad com o ID 1
    prc_cad_exists = session.query(Prc_Cad).filter(Prc_Cad.PRC_id == 1).first() is not None
    if not prc_cad_exists:
        pytest.skip("Não existe um registro válido na tabela Prc_Cad com o ID 1")

    data = {
        'PRC_ID': 1,
        'PRC_ATIV_TITULO': fake.sentence(),
        'PRC_ATIV_ANEXOS': fake.file_path(depth=3, extension='pdf'),
        'PRC_ATIV_OBS': fake.paragraph(),
        'PRC_ATIV_TIME_ID': None,
        'PRC_ATIV_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    nova_ativ_cad = prc_ativ_cad_repository.create(data)

    assert nova_ativ_cad.PRC_ATIV_ID is not None
    for key, value in data.items():
        assert getattr(nova_ativ_cad, key) == value, f"O campo {key} não corresponde ao esperado"

def test_get_all(prc_ativ_cad_repository: PrcAtivCadRepository, session: Session):
    expected_atividades = []

    for _ in range(3):
        data = {
            'PRC_ID': 1,
            'PRC_ATIV_TITULO': fake.sentence(),
            'PRC_ATIV_ANEXOS': fake.file_path(depth=3, extension='pdf'),
            'PRC_ATIV_OBS': fake.paragraph(),
            'PRC_ATIV_TIME_ID': None,
            'PRC_ATIV_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        created_atividade = prc_ativ_cad_repository.create(data)
        expected_atividades.append(created_atividade)

    atividades = prc_ativ_cad_repository.get_all()

    assert len(atividades) == len(expected_atividades), f"Esperado {len(expected_atividades)} registros, mas obtido {len(atividades)}"
    for atividade in expected_atividades:
        assert atividade in atividades, f"A atividade {atividade.PRC_ATIV_ID} não foi encontrada nas atividades retornadas"

def test_get_by_id(prc_ativ_cad_repository: PrcAtivCadRepository, session: Session):
    data = {
        'PRC_ID': 1,
        'PRC_ATIV_TITULO': fake.sentence(),
        'PRC_ATIV_ANEXOS': fake.file_path(depth=3, extension='pdf'),
        'PRC_ATIV_OBS': fake.paragraph(),
        'PRC_ATIV_TIME_ID': None,
        'PRC_ATIV_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_atividade = prc_ativ_cad_repository.create(data)
    atividade_by_id = prc_ativ_cad_repository.get_by_id(created_atividade.PRC_ATIV_ID)

    assert atividade_by_id is not None
    assert atividade_by_id.PRC_ATIV_ID == created_atividade.PRC_ATIV_ID
    for key, value in data.items():
        assert getattr(atividade_by_id, key) == value

def test_update(prc_ativ_cad_repository: PrcAtivCadRepository, session: Session):
    data = {
        'PRC_ID': 1,
        'PRC_ATIV_TITULO': fake.sentence(),
        'PRC_ATIV_ANEXOS': fake.file_path(depth=3, extension='pdf'),
        'PRC_ATIV_OBS': fake.paragraph(),
        'PRC_ATIV_TIME_ID': None,
        'PRC_ATIV_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_atividade = prc_ativ_cad_repository.create(data)

    updated_data = {
        'PRC_ATIV_TITULO': fake.sentence(),
        'PRC_ATIV_OBS': fake.paragraph()
    }

    updated_atividade = prc_ativ_cad_repository.update(created_atividade.PRC_ATIV_ID, updated_data)

    assert updated_atividade is not None
    assert updated_atividade.PRC_ATIV_ID == created_atividade.PRC_ATIV_ID
    for key, value in updated_data.items():
        assert getattr(updated_atividade, key) == value

def test_delete(prc_ativ_cad_repository: PrcAtivCadRepository, session: Session):
    data = {
        'PRC_ID': 1,
        'PRC_ATIV_TITULO': fake.sentence(),
        'PRC_ATIV_ANEXOS': fake.file_path(depth=3, extension='pdf'),
        'PRC_ATIV_OBS': fake.paragraph(),
        'PRC_ATIV_TIME_ID': None,
        'PRC_ATIV_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    created_atividade = prc_ativ_cad_repository.create(data)
    delete_result = prc_ativ_cad_repository.delete(created_atividade.PRC_ATIV_ID)

    assert delete_result == True

    atividade_by_id = prc_ativ_cad_repository.get_by_id(created_atividade.PRC_ATIV_ID)
    assert atividade_by_id is None
