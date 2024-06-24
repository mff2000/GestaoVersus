from sqlalchemy.orm import Session
from infra.entities.Ger_Usuarios import Ger_Usuarios

class GerUsuariosRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_ger_usuario = Ger_Usuarios(**data)
        self._session.add(novo_ger_usuario)
        self._session.commit()
        return novo_ger_usuario

    def get_all(self):
        return self._session.query(Ger_Usuarios).all()

    def get_by_id(self, id: int):
        return self._session.query(Ger_Usuarios).filter_by(GER_USU_ID=id).first()

    def update(self, id: int, data: dict):
        ger_usuario = self.get_by_id(id)
        if ger_usuario:
            for key, value in data.items():
                setattr(ger_usuario, key, value)
            self._session.commit()
            return ger_usuario
        return None

    def delete(self, id: int):
        ger_usuario = self.get_by_id(id)
        if ger_usuario:
            self._session.delete(ger_usuario)
            self._session.commit()
            return True
        return False
