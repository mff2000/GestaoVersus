import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Modelagem import Prc_Modelagem
from infra.repository.prc_modelagem_repository import PrcModelagemRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_modelagem_repository(session: Session):
    return PrcModelagemRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_modelagem_table(session: Session):
    session.query(Prc_Modelagem).delete()
    session.commit()

def test_create(prc_modelagem_repository: PrcModelagemRepository):
    data = {
        'PRC_MODELAGEM_TIPO': fake.word(),
        'PRC_MODELAGEM_DESCR': fake.text(),
        'PRC_MODELAGEM_OBSERV': fake.text(),
        'PRC_MODELAGEM_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_modelagem = prc_modelagem_repository.create(data)
    assert nova_modelagem.PRC_MODELAGEM_ID is not None
    for key, value in data.items():
        assert getattr(nova_modelagem, key) == value

def test_get_all(prc_modelagem_repository: PrcModelagemRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_MODELAGEM_TIPO': fake.word(),
            'PRC_MODELAGEM_DESCR': fake.text(),
            'PRC_MODELAGEM_OBSERV': fake.text(),
            'PRC_MODELAGEM_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_modelagem_repository.create(data)

    # Teste o método get_all
    todas_modelagens = prc_modelagem_repository.get_all()
    assert len(todas_modelagens) == 3

def test_get_by_id(prc_modelagem_repository: PrcModelagemRepository):
    data = {
        'PRC_MODELAGEM_TIPO': fake.word(),
        'PRC_MODELAGEM_DESCR': fake.text(),
        'PRC_MODELAGEM_OBSERV': fake.text(),
        'PRC_MODELAGEM_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    nova_modelagem = prc_modelagem_repository.create(data)

    # Teste com um ID válido
    modelagem_encontrada = prc_modelagem_repository.get_by_id(nova_modelagem.PRC_MODELAGEM_ID)
    assert modelagem_encontrada == nova_modelagem

    # Teste com um ID inválido
    modelagem_nao_encontrada = prc_modelagem_repository.get_by_id(9999)
    assert modelagem_nao_encontrada is None

def test_update(prc_modelagem_repository: PrcModelagemRepository):
    data = {
        'PRC_MODELAGEM_TIPO': fake.word(),
        'PRC_MODELAGEM_DESCR': fake.text(),
        'PRC_MODELAGEM_OBSERV': fake.text(),
        'PRC_MODELAGEM_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    modelagem = prc_modelagem_repository.create(data)

    dados_atualizados = {
        'PRC_MODELAGEM_TIPO': fake.word(),
        'PRC_MODELAGEM_DESCR': fake.text()
    }

    modelagem_atualizada = prc_modelagem_repository.update(modelagem.PRC_MODELAGEM_ID, dados_atualizados)

    assert modelagem_atualizada is not None
    for key, value in dados_atualizados.items():
        assert getattr(modelagem_atualizada, key) == value

def test_delete(prc_modelagem_repository: PrcModelagemRepository):
    data = {
        'PRC_MODELAGEM_TIPO': fake.word(),
        'PRC_MODELAGEM_DESCR': fake.text(),
        'PRC_MODELAGEM_OBSERV': fake.text(),
        'PRC_MODELAGEM_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    modelagem = prc_modelagem_repository.create(data)

    resultado = prc_modelagem_repository.delete(modelagem.PRC_MODELAGEM_ID)
    assert resultado is True

    modelagem_excluida = prc_modelagem_repository.get_by_id(modelagem.PRC_MODELAGEM_ID)
    assert modelagem_excluida is None
