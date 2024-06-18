import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ..entities.Prc_Cad import Processo 

from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Cad import Processo

class Prc_Cad_Repository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Processo).all()
            return data