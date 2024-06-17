import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Agora você pode importar o módulo

from infra.configs.connection import DBConnectionHandler
from infra.entities.Prc_Cad import Prc_Cad

class Prc_Cad_Repository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Prc_Cad).all()
            return data