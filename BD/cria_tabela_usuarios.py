import MySQLdb
import sys
from pathlib import Path

# Parâmetros de conexão

sys.path.append(str(Path('c:/gestaoversus/bd').resolve()))
from conexao_bd import connect_db

# Definição da tabela de usuários
create_table_query = """
CREATE TABLE IF NOT EXISTS GER_USUARIOS (
    GER_USU_ID INT(3) NOT NULL AUTO_INCREMENT,
    GER_USU_NOME VARCHAR(256) NOT NULL,
    GER_USU_EMAIL VARCHAR(256) NOT NULL,
    GER_USU_SENHA VARCHAR(256) NOT NULL,
    GER_USU_GRUPOPERMISSAO VARCHAR(256),
    GER_USU_TIME VARCHAR(256),
    GER_USU_OBSERVACOES VARCHAR(999),
    GER_USU_DT_CRIACAO TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    GER_USU_DT_ALTERACAO TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    GER_USU_DT_INATIVACAO TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (GER_USU_ID)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
"""

# Criar a tabela
try:
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    print("Tabela GER_USUARIOS criada com sucesso!")
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Erro ao criar a tabela: {e}")
