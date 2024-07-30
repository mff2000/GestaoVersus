from sqlalchemy.orm import Session
from infra.entities.Prc_Rotina import Prc_Rotina
from sqlalchemy.exc import IntegrityError

class PrcRotinaRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: Prc_Rotina):  # Recebe o objeto Prc_Rotina como parâmetro
        try:
            self._session.add(data)
            self._session.commit()
            return data
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao criar rotina: {e}")  # Melhora a mensagem de erro

    def get_all(self):
        return self._session.query(Prc_Rotina).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Rotina).filter_by(PRC_ROTINA_ID=id).first()

    def update(self, id: int, data: dict):
        try:
            prc_rotina = self.get_by_id(id)
            if prc_rotina:
                for key, value in data.items():
                    setattr(prc_rotina, key, value)
                self._session.commit()
                return prc_rotina
            return None
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao atualizar rotina: {e}")

    def delete(self, id: int):
        try:
            prc_rotina = self.get_by_id(id)
            if prc_rotina:
                self._session.delete(prc_rotina)
                self._session.commit()
                return True
            return False
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao deletar rotina: {e}")

