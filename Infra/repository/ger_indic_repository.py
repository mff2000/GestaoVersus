from sqlalchemy.orm import Session
from infra.entities.Ger_Indic import Ger_Indic
from sqlalchemy.types import DECIMAL

class GerIndicRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_ger_indic = Ger_Indic(**data)
        self._session.add(novo_ger_indic)
        self._session.commit()
        return novo_ger_indic

    def get_all(self):
        return self._session.query(Ger_Indic).all()

    def get_by_id(self, id: int):
        return self._session.query(Ger_Indic).filter_by(GER_INDIC_ID=id).first()  # Corrigido aqui

    def update(self, id: int, data: dict):
        Ger_Indic = self.get_by_id(id)
        if Ger_Indic:
            for key, value in data.items():
                setattr(Ger_Indic, key, value)
            self._session.commit()
            return Ger_Indic
        return None

    def delete(self, id: int):
        Ger_Indic = self.get_by_id(id)
        if Ger_Indic:
            self._session.delete(Ger_Indic)
            self._session.commit()
            return True
        return False
