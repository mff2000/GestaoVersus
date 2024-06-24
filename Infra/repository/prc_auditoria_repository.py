from sqlalchemy.orm import Session
from infra.entities.Prc_Auditoria import Prc_Auditoria

class PrcAuditoriaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_auditoria = Prc_Auditoria(**data)
        self._session.add(nova_prc_auditoria)
        self._session.commit()
        return nova_prc_auditoria

    def get_all(self):
        return self._session.query(Prc_Auditoria).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Auditoria).filter_by(PRC_AUDITORIA_ID=id).first()

    def update(self, id: int, data: dict):
        prc_auditoria = self.get_by_id(id)
        if prc_auditoria:
            for key, value in data.items():
                setattr(prc_auditoria, key, value)
            self._session.commit()
            return prc_auditoria
        return None

    def delete(self, id: int):
        prc_auditoria = self.get_by_id(id)
        if prc_auditoria:
            self._session.delete(prc_auditoria)
            self._session.commit()
            return True
        return False
