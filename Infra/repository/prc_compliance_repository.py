from sqlalchemy.orm import Session
from infra.entities.Prc_Compliance import Prc_Compliance

class PrcComplianceRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_prc_compliance = Prc_Compliance(**data)
        self._session.add(novo_prc_compliance)
        self._session.commit()
        return novo_prc_compliance

    def get_all(self):
        return self._session.query(Prc_Compliance).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Compliance).filter_by(PRC_COMPLIANCE_ID=id).first()

    def update(self, id: int, data: dict):
        prc_compliance = self.get_by_id(id)
        if prc_compliance:
            for key, value in data.items():
                setattr(prc_compliance, key, value)
            self._session.commit()
            return prc_compliance
        return None

    def delete(self, id: int):
        prc_compliance = self.get_by_id(id)
        if prc_compliance:
            self._session.delete(prc_compliance)
            self._session.commit()
            return True
        return False
