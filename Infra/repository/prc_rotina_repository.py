from sqlalchemy.orm import Session
from infra.entities.Prc_Rotina import Prc_Rotina

class PrcRotinaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_rotina = Prc_Rotina(**data)
        self._session.add(nova_prc_rotina)
        self._session.commit()
        return nova_prc_rotina

    def get_all(self):
        return self._session.query(Prc_Rotina).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Rotina).filter_by(PRC_ROTINA_ID=id).first()

    def update(self, id: int, data: dict):
        prc_rotina = self.get_by_id(id)
        if prc_rotina:
            for key, value in data.items():
                setattr(prc_rotina, key, value)
            self._session.commit()
            return prc_rotina
        return None

    def delete(self, id: int):
        prc_rotina = self.get_by_id(id)
        if prc_rotina:
            self._session.delete(prc_rotina)
            self._session.commit()
            return True
        return False
