from infra.entities.Prc_Macropr_Pai import Prc_Macropr_Pai
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

class PrcMacroprocessoPaiRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, prc_macroprocesso_pai: Prc_Macropr_Pai) -> Prc_Macropr_Pai:
        """
        Adiciona um novo macroprocesso pai ao banco de dados.
        """
        self.session.add(prc_macroprocesso_pai)
        self.session.commit()
        self.session.refresh(prc_macroprocesso_pai)
        return prc_macroprocesso_pai

    def get_by_id(self, prc_macropr_pai_id: int) -> Optional[Prc_Macropr_Pai]:
        """
        Busca um macroprocesso pai pelo ID.
        """
        return self.session.query(Prc_Macropr_Pai).filter_by(PRC_MACROPR_PAI_ID=prc_macropr_pai_id).first()

    def get_all(self) -> List[Prc_Macropr_Pai]:
        """
        Retorna todos os macroprocessos pai.
        """
        return self.session.query(Prc_Macropr_Pai).all()

    def update(self, prc_macropr_pai_id: int, updated_data: dict) -> Optional[Prc_Macropr_Pai]:
        """
        Atualiza um macroprocesso pai existente.
        """
        prc_macropr_pai = self.get_by_id(prc_macropr_pai_id)
        if prc_macropr_pai:
            for key, value in updated_data.items():
                setattr(prc_macropr_pai, key, value)
            prc_macropr_pai.PRC_MACROPR_DT_ALTERACAO = datetime.now()
            self.session.commit()
            self.session.refresh(prc_macropr_pai)
        return prc_macropr_pai

    def delete(self, prc_macropr_pai_id: int) -> bool:
        """
        Exclui um macroprocesso pai pelo ID.
        """
        prc_macropr_pai = self.get_by_id(prc_macropr_pai_id)
        if prc_macropr_pai:
            self.session.delete(prc_macropr_pai)
            self.session.commit()
            return True
        return False


