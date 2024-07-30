import streamlit as st
from infra.repository.ger_usuarios_repository import GerUsuariosRepository
from infra.configs.base import get_session
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Cadastro de Usuários",
    page_icon="👤",
    layout="wide",
)

def cadastro_usuario():
    st.title("Cadastro de Usuários")

    # Dicionário para armazenar os valores do formulário
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {
            "nome": "",
            "email": "",
            "senha": "",
            "confirma_senha": "",
            "grupo_permissao": "Administrador",
            "time": "Time A",
            "observacoes": ""
        }

    # Campos do formulário utilizando os valores do dicionário form_data
    nome = st.text_input("Nome Completo", max_chars=256, key="nome", value=st.session_state["form_data"]["nome"])
    email = st.text_input("Email", max_chars=256, key="email", value=st.session_state["form_data"]["email"])
    senha = st.text_input("Senha", type="password", key="senha", value=st.session_state["form_data"]["senha"])
    confirma_senha = st.text_input("Confirmar Senha", type="password", key="confirma_senha", value=st.session_state["form_data"]["confirma_senha"])
    grupo_permissao = st.selectbox("Grupo de Permissão", ["Administrador", "Usuário"], key="grupo_permissao", index=["Administrador", "Usuário"].index(st.session_state["form_data"]["grupo_permissao"]))
    time = st.selectbox("Time", ["Time A", "Time B"], key="time", index=["Time A", "Time B"].index(st.session_state["form_data"]["time"]))
    observacoes = st.text_area("Observações", max_chars=999, key="observacoes", value=st.session_state["form_data"]["observacoes"])

    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            if senha != confirma_senha:
                st.error("As senhas não coincidem!")
            else:
                with get_session() as session:
                    repo = GerUsuariosRepository(session)

                    # Atualiza o dicionário form_data com os valores do formulário
                    st.session_state["form_data"]["nome"] = nome
                    st.session_state["form_data"]["email"] = email
                    st.session_state["form_data"]["senha"] = senha
                    st.session_state["form_data"]["grupo_permissao"] = grupo_permissao
                    st.session_state["form_data"]["time"] = time
                    st.session_state["form_data"]["observacoes"] = observacoes

                    try:
                        # Cadastra o usuário usando os valores do dicionário form_data
                        novo_usuario = repo.create({
                            "GER_USU_NOME": st.session_state["form_data"]["nome"],
                            "GER_USU_EMAIL": st.session_state["form_data"]["email"],
                            "GER_USU_SENHA": st.session_state["form_data"]["senha"],  # Lembre-se de fazer o hash da senha no repositório!
                            "GER_USU_GRUPOPERMISSAO": st.session_state["form_data"]["grupo_permissao"],
                            "GER_USU_TIME": st.session_state["form_data"]["time"],
                            "GER_USU_OBSERVACOES": st.session_state["form_data"]["observacoes"],
                            "GER_USU_DT_CRIACAO": datetime.now(),
                        })
                        st.success(f"Usuário {novo_usuario.GER_USU_NOME} cadastrado com sucesso!")

                        # Limpa o dicionário form_data após o cadastro
                        st.session_state["form_data"] = {
                            "nome": "",
                            "email": "",
                            "senha": "",
                            "confirma_senha": "",
                            "grupo_permissao": "Administrador",
                            "time": "Time A",
                            "observacoes": ""
                        }
                    except ValueError as e:
                        st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_usuario()
else:
    st.warning("Você precisa fazer login para acessar esta página.")

