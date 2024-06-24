from sqlalchemy.orm import Session
from infra.entities.Prc_Forn_e_Itens_Cons import Prc_Forne_Itens_Cons

class PrcForneItensConsRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_registro = Prc_Forne_Itens_Cons(**data)
        self._session.add(novo_registro)
        self._session.commit()
        return novo_registro

    def get_all(self):
        return self._session.query(Prc_Forne_Itens_Cons).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Forne_Itens_Cons).filter_by(PRC_FORNE_ITENS_CONS_ID=id).first()

    def update(self, id: int, data: dict):
        registro = self.get_by_id(id)
        if registro:
            for key, value in data.items():
                setattr(registro, key, value)
            self._session.commit()
            return registro
        return None

    def delete(self, id: int):
        registro = self.get_by_id(id)
        if registro:
            self._session.delete(registro)
            self._session.commit()
            return True
        return False
