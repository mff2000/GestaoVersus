from sqlalchemy.orm import Session
from infra.entities.Prc_Ativ_Cad import Prc_Ativ_Cad
from sqlalchemy.exc import IntegrityError

class PrcAtivCadRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        try:
            nova_prc_ativ_cad = Prc_Ativ_Cad(**data)
            self._session.add(nova_prc_ativ_cad)
            self._session.commit()
            return nova_prc_ativ_cad
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao criar atividade: {e}")

    def get_all(self):
        return self._session.query(Prc_Ativ_Cad).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Ativ_Cad).filter(Prc_Ativ_Cad.PRC_ATIV_ID == id).first()

    def update(self, id: int, data: dict):
        try:
            prc_ativ_cad = self.get_by_id(id)
            if prc_ativ_cad:
                for key, value in data.items():
                    setattr(prc_ativ_cad, key, value)
                self._session.commit()
                return prc_ativ_cad
            return None
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao atualizar atividade: {e}")

    def delete(self, id: int):
        try:
            prc_ativ_cad = self.get_by_id(id)
            if prc_ativ_cad:
                self._session.delete(prc_ativ_cad)
                self._session.commit()
                return True
            return False
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao deletar atividade: {e}")
