import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Forn_e_Itens_Cons import Prc_Forne_Itens_Cons
from infra.repository.prc_forn_e_itens_cons_repository import PrcForneItensConsRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_forn_e_itens_cons_repository(session: Session):
    return PrcForneItensConsRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_forn_e_itens_cons_table(session: Session):
    session.query(Prc_Forne_Itens_Cons).delete()
    session.commit()

def test_create(prc_forn_e_itens_cons_repository: PrcForneItensConsRepository):
    data = {
        'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
        'PRC_FORNE_ITENS_CONS_UN_MED': fake.word(),
        'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat()),
        'PRC_FORNE_ITENS_CONS_OBSERV': fake.text(),
        'PRC_FORNE_ITENS_CONS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_registro = prc_forn_e_itens_cons_repository.create(data)
    assert novo_registro.PRC_FORNE_ITENS_CONS_ID is not None
    for key, value in data.items():
        assert getattr(novo_registro, key) == value

def test_get_all(prc_forn_e_itens_cons_repository: PrcForneItensConsRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        data = {
            'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
            'PRC_FORNE_ITENS_CONS_UN_MED': fake.word(),
            'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat()),
            'PRC_FORNE_ITENS_CONS_OBSERV': fake.text(),
            'PRC_FORNE_ITENS_CONS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        }
        prc_forn_e_itens_cons_repository.create(data)

    # Teste o método get_all
    todos_registros = prc_forn_e_itens_cons_repository.get_all()
    assert len(todos_registros) == 3

def test_get_by_id(prc_forn_e_itens_cons_repository: PrcForneItensConsRepository):
    data = {
        'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
        'PRC_FORNE_ITENS_CONS_UN_MED': fake.word(),
        'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat()),
        'PRC_FORNE_ITENS_CONS_OBSERV': fake.text(),
        'PRC_FORNE_ITENS_CONS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_registro = prc_forn_e_itens_cons_repository.create(data)

    # Teste com um ID válido
    registro_encontrado = prc_forn_e_itens_cons_repository.get_by_id(novo_registro.PRC_FORNE_ITENS_CONS_ID)
    assert registro_encontrado == novo_registro

    # Teste com um ID inválido
    registro_nao_encontrado = prc_forn_e_itens_cons_repository.get_by_id(9999)
    assert registro_nao_encontrado is None

def test_update(prc_forn_e_itens_cons_repository: PrcForneItensConsRepository):
    data = {
        'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
        'PRC_FORNE_ITENS_CONS_UN_MED': fake.word(),
        'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat()),
        'PRC_FORNE_ITENS_CONS_OBSERV': fake.text(),
        'PRC_FORNE_ITENS_CONS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    registro = prc_forn_e_itens_cons_repository.create(data)

    dados_atualizados = {
        'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
        'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat())
    }

    registro_atualizado = prc_forn_e_itens_cons_repository.update(registro.PRC_FORNE_ITENS_CONS_ID, dados_atualizados)

    assert registro_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(registro_atualizado, key) == value

def test_delete(prc_forn_e_itens_cons_repository: PrcForneItensConsRepository):
    data = {
        'PRC_FORNE_ITENS_CONS_NOME': fake.company(),
        'PRC_FORNE_ITENS_CONS_UN_MED': fake.word(),
        'PRC_FORNE_ITENS_CONS_VALOR': str(fake.pyfloat()),
        'PRC_FORNE_ITENS_CONS_OBSERV': fake.text(),
        'PRC_FORNE_ITENS_CONS_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    registro = prc_forn_e_itens_cons_repository.create(data)

    resultado = prc_forn_e_itens_cons_repository.delete(registro.PRC_FORNE_ITENS_CONS_ID)
    assert resultado is True

    registro_excluido = prc_forn_e_itens_cons_repository.get_by_id(registro.PRC_FORNE_ITENS_CONS_ID)
    assert registro_excluido is None
