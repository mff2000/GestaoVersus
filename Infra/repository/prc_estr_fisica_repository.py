from sqlalchemy.orm import Session
from infra.entities.Prc_Estr_Fisica import Prc_Estr_Fisica

class PrcEstrFisicaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_estr_fisica = Prc_Estr_Fisica(**data)
        self._session.add(nova_prc_estr_fisica)
        self._session.commit()
        return nova_prc_estr_fisica

    def get_all(self):
        return self._session.query(Prc_Estr_Fisica).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Estr_Fisica).filter_by(PRC_ESTR_FISICA_ID=id).first()

    def update(self, id: int, data: dict):
        prc_estr_fisica = self.get_by_id(id)
        if prc_estr_fisica:
            for key, value in data.items():
                setattr(prc_estr_fisica, key, value)
            self._session.commit()
            return prc_estr_fisica
        return None

    def delete(self, id: int):
        prc_estr_fisica = self.get_by_id(id)
        if prc_estr_fisica:
            self._session.delete(prc_estr_fisica)
            self._session.commit()
            return True
        return False
