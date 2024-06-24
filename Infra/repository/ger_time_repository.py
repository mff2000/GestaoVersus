from sqlalchemy.orm import Session
from infra.entities.Ger_Time import Ger_Time

class GerTimeRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_ger_time = Ger_Time(**data)
        self._session.add(novo_ger_time)
        self._session.commit()
        return novo_ger_time

    def get_all(self):
        return self._session.query(Ger_Time).all()

    def get_by_id(self, id: int):
        return self._session.query(Ger_Time).filter_by(GER_TIME_ID=id).first()

    def update(self, id: int, data: dict):
        ger_time = self.get_by_id(id)
        if ger_time:
            for key, value in data.items():
                setattr(ger_time, key, value)
            self._session.commit()
            return ger_time
        return None

    def delete(self, id: int):
        ger_time = self.get_by_id(id)
        if ger_time:
            self._session.delete(ger_time)
            self._session.commit()
            return True
        return False
