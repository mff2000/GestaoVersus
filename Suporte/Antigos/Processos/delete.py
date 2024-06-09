from sqlalchemy.orm import sessionmaker
from modelos import Session, tabela_prc_cad

def excluir_prc_cad(prc_cad_id):
    """
    Função para excluir um registro da tabela PRC_CAD.

    Args:
        prc_cad_id (int): ID do registro a ser excluído.
    """
    with Session() as session:
        registro = session.query(tabela_prc_cad).filter_by(PRC_CAD=prc_cad_id).first()
        if registro:
            session.delete(registro)
            session.commit()