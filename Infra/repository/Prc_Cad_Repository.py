from sqlalchemy.orm import Session
from infra.entities.Prc_Cad import Prc_Cad
from sqlalchemy.exc import IntegrityError

class PrcCadRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: Prc_Cad):  # Recebe o objeto Prc_Cad como parâmetro
        try:
            self._session.add(data)  # Adiciona o objeto à sessão
            self._session.commit()
            return data
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao criar registro Prc_Cad: {e}")

    def get_all(self):
        return self._session.query(Prc_Cad).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Cad).filter(Prc_Cad.PRC_ID == id).first()

    def get_by_codigo(self, codigo: str):
        return self._session.query(Prc_Cad).filter(Prc_Cad.PRC_CODIGO == codigo).first()

    def update(self, id: int, data: dict):
        try:
            prc_cad = self.get_by_id(id)
            if prc_cad:
                for key, value in data.items():
                    setattr(prc_cad, key, value)
                self._session.commit()
                return prc_cad
            return None
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao atualizar registro Prc_Cad: {e}")

    def delete(self, id: int):
        try:
            prc_cad = self.get_by_id(id)
            if prc_cad:
                self._session.delete(prc_cad)
                self._session.commit()
                return True
            return False
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao deletar registro Prc_Cad: {e}")

