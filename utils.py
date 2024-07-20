from infra import DBConnectionHandler
from infra.repository.prc_cad_repository import PrcCadRepository
from sqlalchemy import text

def check_login(email, password):
    with DBConnectionHandler() as db_connection:
        session = db_connection.session
        query = text("SELECT GER_USU_EMAIL, GER_USU_SENHA FROM GER_USUARIOS WHERE GER_USU_EMAIL = :email AND GER_USU_SENHA = :password")
        user = session.execute(query, {"email": email, "password": password}).fetchone()
        return user is not None

def get_all_processes():
    with DBConnectionHandler() as db_connection:
        prc_cad_repo = PrcCadRepository(db_connection.session)
        return prc_cad_repo.get_all()

def create_process(prc_tipo, prc_nome):
    with DBConnectionHandler() as db_connection:
        prc_cad_repo = PrcCadRepository(db_connection.session)
        # Aqui você deve criar o objeto prc_cad com os dados do formulário
        # e usar o método create do repositório para salvar no banco de dados
        # Retorne True se o processo for criado com sucesso, False caso contrário
        return True  # Substitua isso pela lógica real de criação do processo
