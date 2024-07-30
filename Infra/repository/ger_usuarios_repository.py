from sqlalchemy.orm import Session
from infra.entities.Ger_Usuarios import Ger_Usuarios
from sqlalchemy.exc import IntegrityError
import bcrypt

class GerUsuariosRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data: dict):
        try:
            # Criptografa a senha antes de salvar
            data["GER_USU_SENHA"] = bcrypt.hashpw(
                data["GER_USU_SENHA"].encode("utf-8"), bcrypt.gensalt()
            )

            novo_ger_usuario = Ger_Usuarios(**data)
            self._session.add(novo_ger_usuario)
            self._session.commit()
            return novo_ger_usuario
        except IntegrityError:
            self._session.rollback()
            raise ValueError("Email já cadastrado.")

    def get_all(self):
        return self._session.query(Ger_Usuarios).all()

    def get_by_id(self, id: int):
        return self._session.query(Ger_Usuarios).filter_by(GER_USU_ID=id).first()

    def get_by_email(self, email: str):  # Novo método para buscar por email
        return self._session.query(Ger_Usuarios).filter_by(GER_USU_EMAIL=email).first()

    def update(self, id: int, data: dict):
        try:
            ger_usuario = self.get_by_id(id)
            if ger_usuario:
                for key, value in data.items():
                    # Trata a atualização da senha, se houver
                    if key == "GER_USU_SENHA":
                        value = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt())
                    setattr(ger_usuario, key, value)
                self._session.commit()
                return ger_usuario
            return None
        except IntegrityError:
            self._session.rollback()
            raise ValueError("Erro ao atualizar o usuário. Verifique os dados.")

    def delete(self, id: int):
        try:
            ger_usuario = self.get_by_id(id)
            if ger_usuario:
                self._session.delete(ger_usuario)
                self._session.commit()
                return True
            return False
        except IntegrityError:
            self._session.rollback()
            raise ValueError("Erro ao deletar o usuário. Verifique as dependências.")

