import sys
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Adicionar o diretório ao sys.path
sys.path.append('c:/gestaoversus/bd')

# Configurar a conexão com o banco de dados
engine = create_engine('mysql://seu_usuario:senha@localhost/gestaoversus')

Base = declarative_base()

import MySQLdb

# Função para conectar ao banco de dados MySQL
def connect_db():
    return MySQLdb.connect(
        host='localhost',
        user='fabiano',
        passwd='*Paraiso1978',
        db='gestaoversus',
        charset='utf8mb4'
    )

def get_engine():
    return engine

# Testar a conexão
if __name__ == "__main__":
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("Conexão com o banco de dados bem-sucedida!")
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
