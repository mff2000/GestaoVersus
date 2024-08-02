from sqlalchemy.orm import Session
from infra.entities.Ger_Time import Ger_Time
from datetime import datetime
from sqlalchemy.exc import IntegrityError

class GerTimeRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        try:
            novo_ger_time = Ger_Time(**data)
            self._session.add(novo_ger_time)
            self._session.commit()
            return novo_ger_time
        except IntegrityError as e:
            self._session.rollback()
            if "UNIQUE constraint failed" in str(e):
                raise ValueError("Sigla já cadastrada.")
            else:
                raise ValueError(f"Erro ao criar time: {e}")

    def get_all(self):
        return self._session.query(Ger_Time).all()

    def get_by_id(self, id: int):
        return self._session.query(Ger_Time).filter_by(GER_TIME_ID=id).first()

    def get_by_sigla(self, sigla: str):
        return self._session.query(Ger_Time).filter_by(GER_TIME_SIGLA=sigla).first()

    def update(self, id: int, data: dict):
        try:
            ger_time = self.get_by_id(id)
            if ger_time:
                for key, value in data.items():
                    setattr(ger_time, key, value)
                ger_time.GER_TIME_DT_ALTERACAO = datetime.now()  # Atualiza a data de alteração
                self._session.commit()
                return ger_time
            return None
        except IntegrityError as e:
            self._session.rollback()
            if "UNIQUE constraint failed" in str(e):
                raise ValueError("Sigla já cadastrada.")
            else:
                raise ValueError(f"Erro ao atualizar time: {e}")

    def delete(self, id: int):
        try:
            ger_time = self.get_by_id(id)
            if ger_time:
                self._session.delete(ger_time)
                self._session.commit()
                return True
            return False
        except IntegrityError as e:
            self._session.rollback()
            raise ValueError(f"Erro ao deletar time: {e}")

