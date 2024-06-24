import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Ger_Usuarios import Ger_Usuarios
from infra.repository.ger_usuarios_repository import GerUsuariosRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def ger_usuarios_repository(session: Session):
    return GerUsuariosRepository(session)

@pytest.fixture(autouse=True)
def clean_ger_usuarios_table(session: Session):
    session.query(Ger_Usuarios).delete()
    session.commit()

def test_create(ger_usuarios_repository: GerUsuariosRepository):
    data = {
        'GER_USU_NOME': fake.name(),
        'GER_USU_EMAIL': fake.email(),
        'GER_USU_SENHA': fake.password(),  # Assumindo que você tem um método para gerar hashes de senha
        'GER_USU_GRUPOPERMISSAO': fake.word(),
        'GER_USU_TIME': fake.word(),
        'GER_USU_OBSERVACOES': fake.text(),
        'GER_USU_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }

    novo_usuario = ger_usuarios_repository.create(data)

    assert novo_usuario.GER_USU_ID is not None
    for key, value in data.items():
        assert getattr(novo_usuario, key) == value

def test_get_all(ger_usuarios_repository: GerUsuariosRepository):
    for _ in range(3):
        ger_usuarios_repository.create({
            'GER_USU_NOME': fake.name(),
            'GER_USU_EMAIL': fake.email(),
            'GER_USU_SENHA': fake.password(),
            'GER_USU_GRUPOPERMISSAO': fake.word(),
            'GER_USU_TIME': fake.word(),
            'GER_USU_OBSERVACOES': fake.text(),
            'GER_USU_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
        })

    usuarios = ger_usuarios_repository.get_all()
    assert len(usuarios) == 3

def test_get_by_id(ger_usuarios_repository: GerUsuariosRepository):
    data = {
        'GER_USU_NOME': fake.name(),
        'GER_USU_EMAIL': fake.email(),
        'GER_USU_SENHA': fake.password(),
        'GER_USU_GRUPOPERMISSAO': fake.word(),
        'GER_USU_TIME': fake.word(),
        'GER_USU_OBSERVACOES': fake.text(),
        'GER_USU_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    novo_usuario = ger_usuarios_repository.create(data)

    usuario_encontrado = ger_usuarios_repository.get_by_id(novo_usuario.GER_USU_ID)
    assert usuario_encontrado == novo_usuario

    usuario_nao_encontrado = ger_usuarios_repository.get_by_id(9999)  # ID inexistente
    assert usuario_nao_encontrado is None

def test_update(ger_usuarios_repository: GerUsuariosRepository):
    data = {
        'GER_USU_NOME': fake.name(),
        'GER_USU_EMAIL': fake.email(),
        'GER_USU_SENHA': fake.password(),
        'GER_USU_GRUPOPERMISSAO': fake.word(),
        'GER_USU_TIME': fake.word(),
        'GER_USU_OBSERVACOES': fake.text(),
        'GER_USU_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    usuario = ger_usuarios_repository.create(data)

    dados_atualizados = {
        'GER_USU_NOME': fake.name(),
        'GER_USU_EMAIL': fake.email()
    }

    usuario_atualizado = ger_usuarios_repository.update(usuario.GER_USU_ID, dados_atualizados)

    assert usuario_atualizado is not None
    for key, value in dados_atualizados.items():
        assert getattr(usuario_atualizado, key) == value

def test_delete(ger_usuarios_repository: GerUsuariosRepository):
    data = {
        'GER_USU_NOME': fake.name(),
        'GER_USU_EMAIL': fake.email(),
        'GER_USU_SENHA': fake.password(),
        'GER_USU_GRUPOPERMISSAO': fake.word(),
        'GER_USU_TIME': fake.word(),
        'GER_USU_OBSERVACOES': fake.text(),
        'GER_USU_DT_CRIACAO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    usuario = ger_usuarios_repository.create(data)

    resultado = ger_usuarios_repository.delete(usuario.GER_USU_ID)
    assert resultado is True

    usuario_excluido = ger_usuarios_repository.get_by_id(usuario.GER_USU_ID)
    assert usuario_excluido is None
