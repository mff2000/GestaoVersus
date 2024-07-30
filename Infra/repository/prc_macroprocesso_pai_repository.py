from sqlalchemy.orm import Session
from infra.entities.Prc_Macropr_Pai import Prc_Macropr_Pai
from sqlalchemy.exc import IntegrityError

class PrcMacroprocessoPaiRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: Prc_Macropr_Pai):  # Recebe o objeto Prc_Macropr_Pai como parâmetro
        try:
            self._session.add(data)  # Adiciona o objeto à sessão
            self._session.commit()
            return data
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao criar registro Prc_Macropr_Pai: {str(e)}")  # Fornece detalhes do erro

    def get_all(self):
        return self._session.query(Prc_Macropr_Pai).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Macropr_Pai).filter_by(PRC_MACROPR_PAI_ID=id).first()

    # Não há um campo "codigo" na entidade Prc_Macropr_Pai, então vamos criar um get_by_gerenc_id()
    def get_by_gerenc_id(self, gerenc_id: str):
        return self._session.query(Prc_Macropr_Pai).filter_by(PRC_MACROPR_PAI_GERENC_ID=gerenc_id).first()
   
    def update(self, id: int, data: dict):
        try:
            macroprocesso_pai = self.get_by_id(id)
            if macroprocesso_pai:
                for key, value in data.items():
                    setattr(macroprocesso_pai, key, value)
                self._session.commit()
                return macroprocesso_pai
            return None
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao atualizar registro Prc_Macropr_Pai: {str(e)}")  # Fornece detalhes do erro

    def delete(self, id: int):
        try:
            macroprocesso_pai = self.get_by_id(id)
            if macroprocesso_pai:
                self._session.delete(macroprocesso_pai)
                self._session.commit()
                return True
            return False
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao deletar registro Prc_Macropr_Pai: {str(e)}")  # Fornece detalhes do erro
