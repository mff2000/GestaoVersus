from sqlalchemy.orm import Session
from infra.entities.Prc_Analise_Custos import Prc_Analise_Custos

class PrcAnaliseCustosRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_analise_custos = Prc_Analise_Custos(**data)
        self._session.add(nova_analise_custos)
        self._session.commit()
        return nova_analise_custos

    def get_all(self):
        return self._session.query(Prc_Analise_Custos).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Analise_Custos).filter_by(PRC_ANALISE_CUSTOS_ID=id).first()

    def update(self, id: int, data: dict):
        analise_custos = self.get_by_id(id)
        if analise_custos:
            for key, value in data.items():
                setattr(analise_custos, key, value)
            self._session.commit()
            return analise_custos
        return None

    def delete(self, id: int):
        analise_custos = self.get_by_id(id)
        if analise_custos:
            self._session.delete(analise_custos)
            self._session.commit()
            return True
        return False
