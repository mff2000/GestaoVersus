import MySQLdb

# Parâmetros de conexão
db_params = {
    'host': 'localhost',
    'user': 'fabiano',
    'passwd': '*Paraiso1978'
}

# Criação do banco de dados
try:
    connection = MySQLdb.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS gestaoversus CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print("Banco de dados gestaoversus criado com sucesso!")
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Erro ao criar o banco de dados: {e}")

