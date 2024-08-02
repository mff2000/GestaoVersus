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

def initialize_form_data():
    """
    Inicializa o dicionário form_data no session_state com os valores padrão.
    """
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {}

    # Inicializa todas as chaves com valores padrão se não existirem
    st.session_state["form_data"].setdefault("GER_TIME_NOME", "")
    st.session_state["form_data"].setdefault("GER_TIME_SIGLA", "")
    st.session_state["form_data"].setdefault("GER_TIME_LIDER_ID", 0)
    st.session_state["form_data"].setdefault("GER_TIME_DT_CRIACAO", datetime.now())
    st.session_state["form_data"].setdefault("GER_TIME_DT_ALTERACAO", datetime.now())
    st.session_state["form_data"].setdefault("GER_TIME_DT_EXCLUSAO", None)

def cadastro_time():
    st.title("Cadastro de Times")

    # Inicializa o form_data se não existir
    initialize_form_data()

    # Campos do formulário utilizando os valores do dicionário form_data
    nome = st.text_input("Nome do Time", value=st.session_state["form_data"]["GER_TIME_NOME"])
    sigla = st.text_input("Sigla do Time", value=st.session_state["form_data"]["GER_TIME_SIGLA"])

    # Campo para selecionar o líder do time (você precisará buscar os usuários do banco de dados)
    lider_id = st.number_input("ID do Líder", min_value=0, value=st.session_state["form_data"]["GER_TIME_LIDER_ID"])

    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            with get_session() as session:
                repo = GerTimeRepository(session)

                # Atualiza o dicionário form_data com os valores do formulário
                st.session_state["form_data"].update({
                    "GER_TIME_NOME": nome,
                    "GER_TIME_SIGLA": sigla,
                    "GER_TIME_LIDER_ID": lider_id,
                    "GER_TIME_DT_CRIACAO": datetime.now(),
                    "GER_TIME_DT_ALTERACAO": datetime.now(),
                    "GER_TIME_DT_EXCLUSAO": None,
                })

                try:
                    # Passa o dicionário form_data diretamente para o create
                    novo_time = repo.create(st.session_state["form_data"])  
                    st.success(f"Time cadastrado com sucesso! (ID: {novo_time.GER_TIME_ID})")

                    # Limpa o dicionário form_data após o cadastro
                    initialize_form_data()

                    # Reinicia o aplicativo para limpar o formulário
                    st.experimental_rerun()

                except ValueError as e:
                    st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_time()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
