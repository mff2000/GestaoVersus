import streamlit as st
from infra.repository.ger_time_repository import GerTimeRepository
from infra.configs.base import get_session
from infra.entities.Ger_Time import Ger_Time
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Cadastro de Times",
    page_icon="👥",  # Ícone de grupo de pessoas
    layout="wide",
)

def cadastro_time():
    st.title("Cadastro de Times")

    # Dicionário para armazenar os valores do formulário
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {
            "GER_TIME_NOME": "",
            "GER_TIME_SIGLA": "",
            "GER_TIME_LIDER_ID": 0,  # Valor inicial para o ID do líder (0 ou None)
            "GER_TIME_DT_CRIACAO": datetime.now(),
            "GER_TIME_DT_ALTERACAO": datetime.now(),
            "GER_TIME_DT_EXCLUSAO": None,
        }

    # Campos do formulário utilizando os valores do dicionário form_data
    nome = st.text_input("Nome do Time", key="nome", value=st.session_state["form_data"]["GER_TIME_NOME"])
    sigla = st.text_input("Sigla do Time", key="sigla", value=st.session_state["form_data"]["GER_TIME_SIGLA"])

    # Campo para selecionar o líder do time (você precisará buscar os usuários do banco de dados)
    lider_id = st.number_input("ID do Líder", min_value=0, key="lider_id", value=st.session_state["form_data"]["GER_TIME_LIDER_ID"])

    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            with get_session() as session:
                repo = GerTimeRepository(session)

                # Atualiza o dicionário form_data com os valores do formulário, usando os nomes corretos dos atributos
                st.session_state["form_data"]["GER_TIME_NOME"] = nome
                st.session_state["form_data"]["GER_TIME_SIGLA"] = sigla
                st.session_state["form_data"]["GER_TIME_LIDER_ID"] = lider_id
                st.session_state["form_data"]["GER_TIME_DT_CRIACAO"] = datetime.now()
                st.session_state["form_data"]["GER_TIME_DT_ALTERACAO"] = datetime.now()

                try:
                    # Passa o dicionário form_data diretamente para o create
                    novo_time = repo.create(st.session_state["form_data"])  
                    st.success(f"Time cadastrado com sucesso! (ID: {novo_time.GER_TIME_ID})")

                    # Limpa o dicionário form_data após o cadastro
                    st.session_state["form_data"] = {
                        "GER_TIME_NOME": "",
                        "GER_TIME_SIGLA": "",
                        "GER_TIME_LIDER_ID": 0,
                        "GER_TIME_DT_CRIACAO": datetime.now(),
                        "GER_TIME_DT_ALTERACAO": datetime.now(),
                        "GER_TIME_DT_EXCLUSAO": None,
                    }
                except ValueError as e:
                    st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_time()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
