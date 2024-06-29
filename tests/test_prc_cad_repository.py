import pytest
from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import inspect  # Para o método to_dict
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Cad import Prc_Cad  # Importa a classe do módulo correto
from infra.repository.prc_cad_repository import PrcCadRepository
from infra.configs.base import Base  # Importa a classe Base

fake = Faker()

# ----------------------------------------------------------------------
# MODELO (ENTIDADE) Prc_Cad
# ----------------------------------------------------------------------

class Prc_Cad(Base):
    # ... (definição da classe Prc_Cad com suas colunas)

    def to_dict(self):
        """Converte o objeto Prc_Cad em um dicionário, excluindo _sa_instance_state."""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs if c.key != '_sa_instance_state'}

# ----------------------------------------------------------------------
# FIXTURES (CONFIGURAÇÃO DOS TESTES)
# ----------------------------------------------------------------------

@pytest.fixture(scope="module")
def session():
    """Gerencia a sessão do banco de dados, com rollback após cada teste."""
    with DBConnectionHandler() as db_connection:
        yield db_connection.session
        db_connection.session.rollback()

@pytest.fixture
def prc_cad_repository(session: Session):
    """Fornece uma instância do repositório PrcCadRepository."""
    return PrcCadRepository(session)

@pytest.fixture
def create_prc_cad_data(session: Session):
    """Cria um objeto Prc_Cad com dados de teste e o salva no banco."""
    data = {
        'PRC_CODIGO': fake.bothify(text='PRC-????##'),
        'PRC_MP_PAI': fake.pyint(),
        'PRC_NIVEL': fake.pyint(min_value=1, max_value=5),
        'PRC_NOME': fake.company(),
        'PRC_OBJETIVO': fake.paragraph(),
        'PRC_CONHEC_TEC_NOTA': fake.pyint(min_value=1, max_value=5),
        'PRC_CONHEC_GEST_NOTA': fake.pyint(min_value=1, max_value=5),
        'PRC_CONHEC_RELAC_NOTA': fake.pyint(min_value=1, max_value=5),
        'PRC_CONHEC_DESC_OBS': fake.paragraph(),
        'PRC_ESTR_FISICA_NOTA': fake.pyint(min_value=1, max_value=5),
        'PRC_ESTR_FISICA_DESCR': fake.paragraph(),
        'PRC_ESTR_LOGICA_NOTA': fake.pyint(min_value=1, max_value=5),
        'PRC_ESTR_LOGICA_DESCR': fake.paragraph(),
        'PRC_TIME_ID': fake.pyint(),
        'PRC_ROTINA_ID': fake.pyint(),
        'PRC_COMPLIANCE_ID': fake.pyint(),
        'PRC_AUDITORIA_ID': fake.pyint(),
        'PRC_MODELAGEM_ID': fake.pyint(),
        'PRC_RECURSOS_UTILIZ_ID': fake.pyint(),
        'PRC_FORNE_ITENS_CONS': fake.company(),
        'PRC_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now')
    }
    prc_cad = Prc_Cad(**data)
    session.add(prc_cad)
    session.commit()
    return prc_cad

# ----------------------------------------------------------------------
# TESTES (VERIFICAÇÃO DO FUNCIONAMENTO)
# ----------------------------------------------------------------------

def test_create(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    """Verifica a criação de um novo Prc_Cad com todos os campos."""
    novo_prc_cad = create_prc_cad_data
    assert novo_prc_cad.PRC_id is not None

    # Verifica todos os campos, exceto os autoincrement e de datas de alteração/exclusão
    for col in Prc_Cad.__table__.columns:
        if col.name not in ['PRC_id', 'PRC_DT_ALTERACAO', 'PRC_DT_EXCLUSAO']:
            assert getattr(novo_prc_cad, col.name) is not None, f"Campo {col.name} não deveria ser nulo"

def test_get_all(prc_cad_repository: PrcCadRepository, session: Session, create_prc_cad_data: Prc_Cad):
    """Verifica se a consulta de todos os registros retorna o esperado."""
    # Criando mais 3 registros para teste
    for _ in range(3):
        prc_cad_data_dict = create_prc_cad_data.to_dict()
        prc_cad_data_dict.pop('_sa_instance_state', None)
        session.add(Prc_Cad(**prc_cad_data_dict))
        session.commit()

    prc_cads = prc_cad_repository.get_all()
    assert len(prc_cads) == 4  # Total de 4 registros criados

def test_get_by_id(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    """Verifica se a consulta por ID retorna o registro correto."""
    prc_cad_id = create_prc_cad_data.PRC_id
    prc_cad = prc_cad_repository.get_by_id(prc_cad_id)

    assert prc_cad is not None
    assert prc_cad.PRC_id == prc_cad_id

def test_update(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    """Verifica se a atualização de um registro funciona corretamente."""
    prc_cad_id = create_prc_cad_data.PRC_id
    dados_atualizados = {
        'PRC_NOME': fake.company(),
        'PRC_OBJETIVO': fake.paragraph(),
        # ... (outros campos que você deseja atualizar)
    }
    prc_cad_atualizado = prc_cad_repository.update(prc_cad_id, dados_atualizados)

    assert prc_cad_atualizado is not None
    assert prc_cad_atualizado.PRC_id == prc_cad_id
    for key, value in dados_atualizados.items():
        assert getattr(prc_cad_atualizado, key) == value

def test_delete(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    """Verifica se a exclusão de um registro funciona corretamente."""
    prc_cad_id = create_prc_cad_data.PRC_id
    resultado_delete = prc_cad_repository.delete(prc_cad_id)

    assert resultado_delete == True
    prc_cad_excluido = prc_cad_repository.get_by_id(prc_cad_id)
    assert prc_cad_excluido is None
