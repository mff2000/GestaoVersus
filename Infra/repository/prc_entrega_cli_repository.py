from sqlalchemy.orm import Session
from infra.entities.Prc_Entrega_Cli import Prc_Entrega_Cli

class PrcEntregaCliRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        nova_prc_entrega_cli = Prc_Entrega_Cli(**data)
        self._session.add(nova_prc_entrega_cli)
        self._session.commit()
        return nova_prc_entrega_cli

    def get_all(self):
        return self._session.query(Prc_Entrega_Cli).all()

    def get_by_id(self, id: int):
        return self._session.query(Prc_Entrega_Cli).filter_by(PRC_ENTREGA_CLI_ID=id).first()

    def update(self, id: int, data: dict):
        prc_entrega_cli = self.get_by_id(id)
        if prc_entrega_cli:
            for key, value in data.items():
                setattr(prc_entrega_cli, key, value)
            self._session.commit()
            return prc_entrega_cli
        return None

    def delete(self, id: int):
        prc_entrega_cli = self.get_by_id(id)
        if prc_entrega_cli:
            self._session.delete(prc_entrega_cli)
            self._session.commit()
            return True
        return False
