from sqlalchemy.orm import Session
from infra.entities.Prc_Modelagem import Prc_Modelagem

class PrcModelagemRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_modelagem = Prc_Modelagem(**data)
        self._session.add(nova_prc_modelagem)
        self._session.commit()
        return nova_prc_modelagem

    def get_all(self):
        return self._session.query(Prc_Modelagem).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Modelagem).filter_by(PRC_MODELAGEM_ID=id).first()

    def update(self, id: int, data: dict):
        prc_modelagem = self.get_by_id(id)
        if prc_modelagem:
            for key, value in data.items():
                setattr(prc_modelagem, key, value)
            self._session.commit()
            return prc_modelagem
        return None

    def delete(self, id: int):
        prc_modelagem = self.get_by_id(id)
        if prc_modelagem:
            self._session.delete(prc_modelagem)
            self._session.commit()
            return True
        return False
