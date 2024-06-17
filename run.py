import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Agora você pode importar o módulo
from infra.repository.Prc_Cad_Repository import Prc_Cad_Repository

repo = Prc_Cad_Repository()

data = repo.select()

print(data)


