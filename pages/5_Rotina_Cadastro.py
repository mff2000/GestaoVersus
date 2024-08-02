import streamlit as st
from infra.repository.prc_rotina_repository import PrcRotinaRepository
from infra.configs.base import get_session
from infra.entities.Prc_Rotina import Prc_Rotina
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Cadastro de Rotinas",
    page_icon="🔄",
    layout="wide",
)

def initialize_form_data():
    """
    Inicializa o dicionário form_data no session_state com os valores padrão.
    """
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {}

    # Inicializa todas as chaves com valores padrão se não existirem
    st.session_state["form_data"].setdefault("nome", "")
    st.session_state["form_data"].setdefault("period", "Diária")
    st.session_state["form_data"].setdefault("start", "")
    st.session_state["form_data"].setdefault("descr", "")
    st.session_state["form_data"].setdefault("observ", "")

def cadastro_rotina():
    st.title("Cadastro de Rotinas")

    # Inicializa o form_data se não existir
    initialize_form_data()

    # Campos do formulário utilizando os valores do dicionário form_data
    nome = st.text_input("Nome da Rotina", value=st.session_state["form_data"]["nome"])

    # Corrige o index do selectbox
    period_options = ["Diária", "Semanal", "Mensal", "Anual"]
    default_index = period_options.index(st.session_state["form_data"]["period"]) if st.session_state["form_data"]["period"] in period_options else 0
    period = st.selectbox("Periodicidade", period_options, index=default_index)

    start = st.text_input("Gatilho", value=st.session_state["form_data"]["start"])
    descr = st.text_area("Descrição", value=st.session_state["form_data"]["descr"])
    observ = st.text_area("Observações", value=st.session_state["form_data"]["observ"])

    # Botão de envio dentro do formulário
    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            with get_session() as session:
                repo = PrcRotinaRepository(session)

                # Atualiza o dicionário form_data com os valores do formulário
                st.session_state["form_data"].update({
                    "nome": nome,
                    "period": period,
                    "start": start,
                    "descr": descr,
                    "observ": observ,
                })

                try:
                    # Cadastra a rotina usando os valores do dicionário form_data
                    nova_rotina = repo.create(Prc_Rotina(
                        PRC_ROTINA_NOME=st.session_state["form_data"]["nome"],
                        PRC_ROTINA_PERIOD=st.session_state["form_data"]["period"],
                        PRC_ROTINA_START=st.session_state["form_data"]["start"],
                        PRC_ROTINA_DESCR=st.session_state["form_data"]["descr"],
                        PRC_ROTINA_OBSERV=st.session_state["form_data"]["observ"],
                        PRC_ROTINA_DT_CRIACAO=datetime.now(),
                    ))
                    st.success(f"Rotina cadastrada com sucesso! (ID: {nova_rotina.PRC_ROTINA_ID})")

                    # Limpa o dicionário form_data após o cadastro
                    initialize_form_data()

                    # Reinicia o aplicativo para limpar o formulário
                    st.experimental_rerun()

                except ValueError as e:
                    st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_rotina()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
