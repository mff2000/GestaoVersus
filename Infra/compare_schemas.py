from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import Inspector
from infra.entities.Prc_Cad import Prc_Cad

# Configuração da conexão com o banco de dados (substitua pelos seus dados)
engine = create_engine('mysql+pymysql://fabiano:*Paraiso1978@localhost:3306/gestaoversus')

# Metadados para refletir o esquema do banco de dados
metadata_db = MetaData()
metadata_db.reflect(bind=engine)

# Metadados dos seus modelos SQLAlchemy
metadata_models = Prc_Cad.metadata

# Inspetor do SQLAlchemy
inspector = Inspector.from_engine(engine)

# Comparar os metadados
diff = {}
for table_name in metadata_models.tables.keys():
    table_diff = []
    for col in metadata_models.tables[table_name].columns:
        if col.name not in [c['name'] for c in inspector.get_columns(table_name)]:
            table_diff.append(f'Coluna faltante: {col.name}')
    if table_diff:
        diff[table_name] = table_diff

# Exibir as diferenças encontradas
if diff:
    print("Diferenças encontradas:")
    for table_name, table_diffs in diff.items():
        print(f"- Tabela '{table_name}':")
        for diff in table_diffs:
            print(f"  * {diff}")
else:
    print("Os esquemas são idênticos.")
