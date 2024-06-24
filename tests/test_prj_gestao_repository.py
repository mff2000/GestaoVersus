import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prj_Gestao import Prj_Gestao
from infra.repository.prj_gestao_repository import PrjGestaoRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prj_gestao_repository(session: Session):
    return PrjGestaoRepository(session)

@pytest.fixture(autouse=True)
def clean_prj_gestao_table(session: Session):
    session.query(Prj_Gestao).delete()
    session.commit()

def test_create(prj_gestao_repository: PrjGestaoRepository):
    data = {
        'PRJ_TIPO': fake.word(),
        'PRJ_PAI': None,
        'PRJ_NIVEL': fake.random_int(min=1, max=5),
        'PRJ_CODIGO': fake.bothify(text='????-####'),
        'PRJ_TITULO': fake.sentence(),
        'PRJ_DESCRICAO': fake.text(),
        'PRJ_RESPONS_ID': None,
        'PRJ_EXECUTORES_ID': None,
        'PRJ_PROCESSO_ID': None,
        'PRJ_AREA': fake.word(),
        'PRJ_OBSERV_HISTOR': fake.text(),
        'PRJ_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRJ_DT_PREVISTA': fake.future_datetime(),
        'PRJ_DT_PRORROGADA': None,
        'PRJ_DT_CONCLUSAO': None,
        'PRJ_DT_EXCLUSAO': None
    }
    novo_projeto = prj_gestao_repository.create(data)
    assert novo_projeto.PRJ_ID is not None
    for key, value in data.items():
        assert getattr(novo_projeto, key) == value

def test_get_all(prj_gestao_repository: PrjGestaoRepository):
    # Crie alguns registros de teste
    for _ in range(3):
        prj_gestao_repository.create({
            'PRJ_TIPO': fake.word(),
            'PRJ_PAI': None,
            'PRJ_NIVEL': fake.random_int(min=1, max=5),
            'PRJ_CODIGO': fake.bothify(text='????-####'),
            'PRJ_TITULO': fake.sentence(),
            'PRJ_DESCRICAO': fake.text(),
            'PRJ_RESPONS_ID': None,
            'PRJ_EXECUTORES_ID': None,
            'PRJ_PROCESSO_ID': None,
            'PRJ_AREA': fake.word(),
            'PRJ_OBSERV_HISTOR': fake.text(),
            'PRJ_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now'),
            'PRJ_DT_PREVISTA': fake.future_datetime(),
            'PRJ_DT_PRORROGADA': None,
            'PRJ_DT_CONCLUSAO': None,
            'PRJ_DT_EXCLUSAO': None
        })

    # Teste o método get_all
    todos_projetos = prj_gestao_repository.get_all()
    assert len(todos_projetos) == 3

def test_get_by_id(prj_gestao_repository: PrjGestaoRepository):
    data = {
        'PRJ_TIPO': fake.word(),
        'PRJ_PAI': None,
        'PRJ_NIVEL': fake.random_int(min=1, max=5),
        'PRJ_CODIGO': fake.bothify(text='????-####'),
        'PRJ_TITULO': fake.sentence(),
        'PRJ_DESCRICAO': fake.text(),
        'PRJ_RESPONS_ID': None,
        'PRJ_EXECUTORES_ID': None,
        'PRJ_PROCESSO_ID': None,
        'PRJ_AREA': fake.word(),
        'PRJ_OBSERV_HISTOR': fake.text(),
        'PRJ_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRJ_DT_PREVISTA': fake.future_datetime(),
        'PRJ_DT_PRORROGADA': None,
        'PRJ_DT_CONCLUSAO': None,
        'PRJ_DT_EXCLUSAO': None
    }
    novo_projeto = prj_gestao_repository.create(data)

    # Teste com um ID válido
    projeto_encontrado = prj_gestao_repository.get_by_id(novo_projeto.PRJ_ID)
    assert projeto_encontrado == novo_projeto

    # Teste com um ID inválido
    projeto_nao_encontrado = prj_gestao_repository.get_by_id(9999)
    assert projeto_nao_encontrado is None

def test_update(prj_gestao_repository: PrjGestaoRepository):
    data = {
        'PRJ_TIPO': fake.word(),
        'PRJ_PAI': None,
        'PRJ_NIVEL': fake.random_int(min=1, max=5),
        'PRJ_CODIGO': fake.bothify(text='????-####'),
        'PRJ_TITULO': fake.sentence(),
        'PRJ_DESCRICAO': fake.text(),
        'PRJ_RESPONS_ID': None,
        'PRJ_EXECUTORES_ID': None,
        'PRJ_PROCESSO_ID': None,
        'PRJ_AREA': fake.word(),
        'PRJ_OBSERV_HISTOR': fake.text(),
        'PRJ_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRJ_DT_PREVISTA': fake.future_datetime(),
        'PRJ_DT_PRORROGADA': None,
        'PRJ_DT_CONCLUSAO': None,
        'PRJ_DT_EXCLUSAO': None
    }
    projeto = prj_gestao_repository.create(data)

    dados_atualizados = {
        'PRJ_TITULO': fake.sentence(),
        'PRJ_DESCRICAO': fake.text()
    }

    projeto_atualizado = prj_gestao_repository.update(projeto.PRJ_ID, dados_atualizados)

    assert projeto_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(projeto_atualizado, key) == value

def test_delete(prj_gestao_repository: PrjGestaoRepository):
    data = {
        'PRJ_TIPO': fake.word(),
        'PRJ_PAI': None,
        'PRJ_NIVEL': fake.random_int(min=1, max=5),
        'PRJ_CODIGO': fake.bothify(text='????-####'),
        'PRJ_TITULO': fake.sentence(),
        'PRJ_DESCRICAO': fake.text(),
        'PRJ_RESPONS_ID': None,
        'PRJ_EXECUTORES_ID': None,
        'PRJ_PROCESSO_ID': None,
        'PRJ_AREA': fake.word(),
        'PRJ_OBSERV_HISTOR': fake.text(),
        'PRJ_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRJ_DT_PREVISTA': fake.future_datetime(),
        'PRJ_DT_PRORROGADA': None,
        'PRJ_DT_CONCLUSAO': None,
        'PRJ_DT_EXCLUSAO': None
    }
    projeto = prj_gestao_repository.create(data)

    resultado = prj_gestao_repository.delete(projeto.PRJ_ID)
    assert resultado is True

    projeto_excluido = prj_gestao_repository.get_by_id(projeto.PRJ_ID)
    assert projeto_excluido is None
