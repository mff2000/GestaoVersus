from infra.configs.base import get_session
from infra.repository.prc_cad_repository import PrcCadRepository
from sqlalchemy import text

def check_login(email, password):
    with get_session() as session:  # Usa o gerenciador de contexto get_session()
        query = text("SELECT GER_USU_EMAIL, GER_USU_SENHA FROM GER_USUARIOS WHERE GER_USU_EMAIL = :email AND GER_USU_SENHA = :password")
        user = session.execute(query, {"email": email, "password": password}).fetchone()
        return user is not None

def get_all_processes():
    with get_session() as session:
        prc_cad_repo = PrcCadRepository(session)
        return prc_cad_repo.get_all()

def create_process(prc_tipo, prc_nome):
    with get_session() as session:
        prc_cad_repo = PrcCadRepository(session)
        # ... (Lógica para criar o processo)