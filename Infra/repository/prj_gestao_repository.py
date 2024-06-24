from sqlalchemy.orm import Session
from infra.entities.Prj_Gestao import Prj_Gestao  # Importando a entidade correta

class PrjGestaoRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        novo_prj_gestao = Prj_Gestao(**data)
        self._session.add(novo_prj_gestao)
        self._session.commit()
        return novo_prj_gestao

    def get_all(self):
        return self._session.query(Prj_Gestao).all()

    def get_by_id(self, id: int):
        return self._session.query(Prj_Gestao).filter_by(PRJ_ID=id).first() # Corrigido o nome da entidade

    def update(self, id: int, data: dict):
        prj_gestao = self.get_by_id(id)  # Corrigido o nome da variável
        if prj_gestao:
            for key, value in data.items():
                setattr(prj_gestao, key, value)
            self._session.commit()
            return prj_gestao
        return None

    def delete(self, id: int):
        prj_gestao = self.get_by_id(id)  # Corrigido o nome da variável
        if prj_gestao:
            self._session.delete(prj_gestao)
            self._session.commit()
            return True
        return False
