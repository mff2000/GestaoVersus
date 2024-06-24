from sqlalchemy.orm import Session
from infra.entities.Prc_Capac_Operac import Prc_Capac_Operac

class PrcCapacOperacRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_capac_operac = Prc_Capac_Operac(**data)
        self._session.add(nova_prc_capac_operac)
        self._session.commit()
        return nova_prc_capac_operac

    def get_all(self):
        return self._session.query(Prc_Capac_Operac).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Capac_Operac).filter_by(PRC_CAPAC_OPERAC_ID=id).first()

    def update(self, id: int, data: dict):
        prc_capac_operac = self.get_by_id(id)
        if prc_capac_operac:
            for key, value in data.items():
                setattr(prc_capac_operac, key, value)
            self._session.commit()
            return prc_capac_operac
        return None

    def delete(self, id: int):
        prc_capac_operac = self.get_by_id(id)
        if prc_capac_operac:
            self._session.delete(prc_capac_operac)
            self._session.commit()
            return True
        return False
