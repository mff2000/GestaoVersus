import pytest
from faker import Faker
from sqlalchemy.orm import Session
from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Cad import Prc_Cad
from infra.repository.prc_cad_repository import PrcCadRepository

fake = Faker()

@pytest.fixture(scope="module")
def session():
    with DBConnectionHandler() as db_connection:
        yield db_connection.session

@pytest.fixture
def prc_cad_repository(session: Session):
    return PrcCadRepository(session)

@pytest.fixture(autouse=True)
def clean_prc_cad_table(session: Session):
    session.query(Prc_Cad).delete()
    session.commit()

@pytest.fixture
def create_prc_cad_data(session: Session):
    data = {
        'PRC_TIPO': fake.random_element(['Produto', 'Serviço', 'Projeto']),
        'PRC_PAI': fake.pyint(),
        'PRC_NIVEL': fake.pyint(min_value=1, max_value=5),
        'PRC_CODIGO': fake.bothify(text='PRC-????##'),
        'PRC_NOME': fake.company(),
        'PRC_GERENCIAM': fake.name(),
        'PRC_MISSAO': fake.paragraph(),
        'PRC_DONO_ID': fake.pyint(), 
        'PRC_EXIG_QUALID': fake.paragraph(),
        'PRC_INDICE_ID': fake.pyint(),
        'PRC_ENTREGA_CLI_ID': fake.pyint(),
        'PRC_TIME_ID': fake.pyint(),
        'PRC_CONHEC_ID': fake.pyint(),
        'PRC_ESTR_FISICA_ID': fake.pyint(),
        'PRC_ESTR_LOGICA_ID': fake.pyint(),
        'PRC_MODELAGEM_ID': fake.pyint(),
        'PRC_ROTINA_ID': fake.pyint(),
        'PRC_CAPAC_OPERAC_ID': fake.pyint(),
        'PRC_FORNE_ITENS_CONS_ID': fake.pyint(),
        'PRC_ANALISE_CUSTOS_ID': fake.pyint(),
        'PRC_COMPLIANCE_ID': fake.pyint(),
        'PRC_AUDITORIA_ID': fake.pyint(),
        'PRC_DT_CADASTRO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRC_DT_ALTERACAO': fake.date_time_between(start_date='-1y', end_date='now'),
        'PRC_DT_EXCLUSAO': fake.date_time_between(start_date='-1y', end_date='now')        
    }
    prc_cad = Prc_Cad(**data)
    session.add(prc_cad)
    session.commit()
    return prc_cad

def test_create(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    novo_prc_cad = create_prc_cad_data

    # Verificar se o ID foi gerado automaticamente e se os dados foram salvos corretamente
    assert novo_prc_cad.PRC_id is not None
    for key, value in novo_prc_cad.__dict__.items():
        if not key.startswith('_sa_instance_state'):
            assert value is not None, f"O campo {key} está None"

def test_get_all(prc_cad_repository: PrcCadRepository, session: Session):
    expected_prc_cads = []

    for _ in range(4):
        prc_cad_data = Prc_Cad(
            PRC_TIPO=fake.random_element(['Produto', 'Serviço', 'Projeto']),
            PRC_PAI=fake.pyint(),
            PRC_NIVEL=fake.pyint(min_value=1, max_value=5),
            PRC_CODIGO=fake.bothify(text='PRC-????##'),
            PRC_NOME=fake.company(),
            PRC_GERENCIAM=fake.name(),
            PRC_MISSAO=fake.paragraph(),
            PRC_DONO_ID=fake.pyint(), 
            PRC_EXIG_QUALID=fake.paragraph(),
            PRC_INDICE_ID=fake.pyint(),
            PRC_ENTREGA_CLI_ID=fake.pyint(),
            PRC_TIME_ID=fake.pyint(),
            PRC_CONHEC_ID=fake.pyint(),
            PRC_ESTR_FISICA_ID=fake.pyint(),
            PRC_ESTR_LOGICA_ID=fake.pyint(),
            PRC_MODELAGEM_ID=fake.pyint(),
            PRC_ROTINA_ID=fake.pyint(),
            PRC_CAPAC_OPERAC_ID=fake.pyint(),
            PRC_FORNE_ITENS_CONS_ID=fake.pyint(),
            PRC_ANALISE_CUSTOS_ID=fake.pyint(),
            PRC_COMPLIANCE_ID=fake.pyint(),
            PRC_AUDITORIA_ID=fake.pyint(),
            PRC_DT_CADASTRO=fake.date_time_between(start_date='-1y', end_date='now'),
            PRC_DT_ALTERACAO=fake.date_time_between(start_date='-1y', end_date='now'),
            PRC_DT_EXCLUSAO=fake.date_time_between(start_date='-1y', end_date='now')
        )
        session.add(prc_cad_data)
        session.commit()
        expected_prc_cads.append(prc_cad_data)

    prc_cads = prc_cad_repository.get_all()

    assert len(prc_cads) == len(expected_prc_cads), f"Esperado {len(expected_prc_cads)} registros, mas obtido {len(prc_cads)}"
    for prc_cad in prc_cads:
        assert prc_cad in expected_prc_cads

def test_get_by_id(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    prc_cad_id = create_prc_cad_data.PRC_id
    prc_cad = prc_cad_repository.get_by_id(prc_cad_id)

    assert prc_cad is not None
    assert prc_cad.PRC_id == prc_cad_id

def test_update(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad, session: Session):
    prc_cad_id = create_prc_cad_data.PRC_id
    dados_atualizados = {
        'PRC_NOME': fake.company(),
        'PRC_GERENCIAM': fake.name()
    }
    prc_cad_atualizado = prc_cad_repository.update(prc_cad_id, dados_atualizados)

    assert prc_cad_atualizado is not None
    assert prc_cad_atualizado.PRC_id == prc_cad_id
    for key, value in dados_atualizados.items():
        assert getattr(prc_cad_atualizado, key) == value

def test_delete(prc_cad_repository: PrcCadRepository, create_prc_cad_data: Prc_Cad):
    prc_cad_id = create_prc_cad_data.PRC_id
    resultado_delete = prc_cad_repository.delete(prc_cad_id)

    assert resultado_delete == True

    prc_cad_excluido = prc_cad_repository.get_by_id(prc_cad_id)
    assert prc_cad_excluido is None

