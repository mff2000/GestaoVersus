from sqlalchemy.orm import Session
from infra.entities.Prc_Estr_Logica import Prc_Estr_Logica

class PrcEstrLogicaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_estr_logica = Prc_Estr_Logica(**data)
        self._session.add(nova_prc_estr_logica)
        self._session.commit()
        return nova_prc_estr_logica

    def get_all(self):
        return self._session.query(Prc_Estr_Logica).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Estr_Logica).filter_by(PRC_ESTR_LOGICA_ID=id).first()

    def update(self, id: int, data: dict):
        prc_estr_logica = self.get_by_id(id)
        if prc_estr_logica:
            for key, value in data.items():
                setattr(prc_estr_logica, key, value)
            self._session.commit()
            return prc_estr_logica
        return None

    def delete(self, id: int):
        prc_estr_logica = self.get_by_id(id)
        if prc_estr_logica:
            self._session.delete(prc_estr_logica)
            self._session.commit()
            return True
        return False
