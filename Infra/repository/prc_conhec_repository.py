from sqlalchemy.orm import Session
from infra.entities.Prc_Conhec import Prc_Conhec

class PrcConhecRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_prc_conhec = Prc_Conhec(**data)
        self._session.add(novo_prc_conhec)
        self._session.commit()
        return novo_prc_conhec

    def get_all(self):
        return self._session.query(Prc_Conhec).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Conhec).filter_by(PRC_CONHEC_ID=id).first()

    def update(self, id: int, data: dict):
        prc_conhec = self.get_by_id(id)
        if prc_conhec:
            for key, value in data.items():
                setattr(prc_conhec, key, value)
            self._session.commit()
            return prc_conhec
        return None

    def delete(self, id: int):
        prc_conhec = self.get_by_id(id)
        if prc_conhec:
            self._session.delete(prc_conhec)
            self._session.commit()
            return True
        return False
