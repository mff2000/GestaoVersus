from sqlalchemy.orm import sessionmaker
from modelos import Session, tabela_prc_cad

def ler_todos_prc_cad():
    """
    Função para ler todos os registros da tabela PRC_CAD.

    Returns:
        list: Lista de registros da tabela PRC_CAD.
    """
    with Session() as session:
        registros = session.query(tabela_prc_cad).all()
        return registros

def ler_prc_cad_por_id(prc_cad_id):
    """
    Função para ler um registro específico da tabela PRC_CAD pelo ID.

    Args:
        prc_cad_id (int): ID do registro a ser lido.

    Returns:
        object: Registro da tabela PRC_CAD ou None se não encontrado.
    """
    with Session() as session:
        registro = session.query(tabela_prc_cad).filter_by(PRC_CAD=prc_cad_id).first()
        return registro
