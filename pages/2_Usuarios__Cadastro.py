import streamlit as st
from infra.repository.ger_usuarios_repository import GerUsuariosRepository
from infra.configs.base import get_session
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Cadastro de Usuários",
    page_icon="👤",  # Ícone de usuário
    layout="wide",
)

def cadastro_usuario():
    st.title("Cadastro de Usuários")

    # Dicionário para armazenar os valores do formulário
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {
            "GER_USU_NOME": "",
            "GER_USU_EMAIL": "",
            "GER_USU_SENHA": "",
            "GER_USU_CONFIRMA_SENHA": "",  # Adicionei essa chave para o campo de confirmação de senha
            "GER_USU_GRUPOPERMISSAO": "Administrador",
            "GER_USU_TIME": "Time A",
            "GER_USU_OBSERVACOES": ""
        }

    # Campos do formulário utilizando os valores do dicionário form_data
    nome = st.text_input("Nome Completo", max_chars=256, key="nome", value=st.session_state["form_data"]["GER_USU_NOME"])
    email = st.text_input("Email", max_chars=256, key="email", value=st.session_state["form_data"]["GER_USU_EMAIL"])
    senha = st.text_input("Senha", type="password", key="senha", value=st.session_state["form_data"]["GER_USU_SENHA"])
    confirma_senha = st.text_input("Confirmar Senha", type="password", key="confirma_senha", value=st.session_state["form_data"]["GER_USU_CONFIRMA_SENHA"])
    grupo_permissao = st.selectbox("Grupo de Permissão", ["Administrador", "Usuário"], key="grupo_permissao", index=["Administrador", "Usuário"].index(st.session_state["form_data"]["GER_USU_GRUPOPERMISSAO"]))
    time = st.selectbox("Time", ["Time A", "Time B"], key="time", index=["Time A", "Time B"].index(st.session_state["form_data"]["GER_USU_TIME"]))
    observacoes = st.text_area("Observações", max_chars=999, key="observacoes", value=st.session_state["form_data"]["GER_USU_OBSERVACOES"])

    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            if senha != confirma_senha:
                st.error("As senhas não coincidem!")
            else:
                with get_session() as session:
                    repo = GerUsuariosRepository(session)

                    # Atualiza o dicionário form_data com os valores do formulário
                    st.session_state["form_data"]["GER_USU_NOME"] = nome
                    st.session_state["form_data"]["GER_USU_EMAIL"] = email
                    st.session_state["form_data"]["GER_USU_SENHA"] = senha
                    st.session_state["form_data"]["GER_USU_CONFIRMA_SENHA"] = confirma_senha  # Atualiza também a confirmação de senha
                    st.session_state["form_data"]["GER_USU_GRUPOPERMISSAO"] = grupo_permissao
                    st.session_state["form_data"]["GER_USU_TIME"] = time
                    st.session_state["form_data"]["GER_USU_OBSERVACOES"] = observacoes

                    try:
                        # Cadastra o usuário usando os valores do dicionário form_data
                        novo_usuario = repo.create(st.session_state["form_data"])
                        st.success(f"Usuário {novo_usuario.GER_USU_NOME} cadastrado com sucesso!")

                        # Limpa o dicionário form_data após o cadastro
                        st.session_state["form_data"] = {
                            "GER_USU_NOME": "",
                            "GER_USU_EMAIL": "",
                            "GER_USU_SENHA": "",
                            "GER_USU_CONFIRMA_SENHA": "",
                            "GER_USU_GRUPOPERMISSAO": "Administrador",
                            "GER_USU_TIME": "Time A",
                            "GER_USU_OBSERVACOES": ""
                        }
                    except ValueError as e:
                        st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_usuario()
else:
    st.warning("Você precisa fazer login para acessar esta página.")

