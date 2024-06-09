import MySQLdb
import sys
from pathlib import Path

sys.path.append(str(Path('c:/gestaoversus/bd').resolve()))
from conexao_bd import connect_db

# Definição da tabela de processos
create_table_query = """
CREATE TABLE IF NOT EXISTS CAD_PROCESSOS (
    PRC_ID INT(3) NOT NULL AUTO_INCREMENT,  -- Corrigido para AUTO_INCREMENT
    PRC_TIPO VARCHAR(20) NOT NULL,
    PRC_PAI INT(3),
    PRC_NIVEL INT(3) NOT NULL,
    PRC_CODIGO VARCHAR(20) NOT NULL,
    PRC_NOME VARCHAR(256) NOT NULL,
    PRC_GERENCIAM VARCHAR(256),
    PRC_MISSAO VARCHAR(999),       
    PRC_DONO_ID INT(3),    
    PRC_EXIG_QUALID VARCHAR(999),           
    PRC_INDIC_ID INT(3),
    PRC_ENTREGA_CLI_ID INT(3),          
    PRC_TIME_ID INT(3),
    PRC_CONHEC_ID INT(3),
    PRC_ESTR_FISICA_ID INT(3),
    PRC_ESTR_LOGICA_ID INT(3),
    PRC_MODELAGEM_ID INT(3),
    PRC_ROTINA_ID INT(3),
    PRC_CAPAC_OPERAC_ID INT(3),
    PRC_FORNE_ITENS_CONS_ID INT(3),
    PRC_ANALISE_CUSTOS_ID INT(3),
    PRC_COMPLIANCE_ID INT(3),
    PRC_AUDITORIA_ID INT(3),
    PRC_DT_CADASTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRC_DT_ALTERACAO TIMESTAMP DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRC_DT_EXCLUSAO TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (PRC_ID)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
"""

# Criar a tabela
try:
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    print("Tabela CAD_PROCESSOS criada com sucesso!")

except MySQLdb.Error as e:
    print(f"Erro ao criar a tabela: {e}")

finally:
    # Certifique-se de fechar o cursor e a conexão
    if cursor:
        cursor.close()
    if connection:
        connection.close()
