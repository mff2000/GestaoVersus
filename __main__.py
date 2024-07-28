import os
import sys

# Obtém o diretório do projeto (onde está o arquivo __main__.py)
project_dir = os.path.dirname(os.path.abspath(__file__))

# Adiciona o diretório do projeto ao sys.path
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Agora você pode importar os módulos usando caminhos relativos
from Home import app  # Importe a função app do seu Home.py

# Execute o aplicativo Streamlit
if __name__ == "__main__":
    app()