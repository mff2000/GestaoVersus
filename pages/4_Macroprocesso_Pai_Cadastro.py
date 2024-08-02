import streamlit as st
from infra.repository.prc_macroprocesso_pai_repository import PrcMacroprocessoPaiRepository
from infra.configs.base import get_session
from infra.entities.Prc_Macropr_Pai import Prc_Macropr_Pai
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Cadastro de Macroprocessos Pai",
    page_icon="🔗",
    layout="wide",
)

def initialize_form_data():
    """
    Inicializa o dicionário form_data no session_state com os valores padrão.
    """
    if "form_data" not in st.session_state:
        st.session_state["form_data"] = {}

    # Inicializa todas as chaves com valores padrão se não existirem
    st.session_state["form_data"].setdefault("gerenc_id", "")
    st.session_state["form_data"].setdefault("missao", "")
    st.session_state["form_data"].setdefault("dono_id", "")
    st.session_state["form_data"].setdefault("exig_qual", "")
    st.session_state["form_data"].setdefault("avo_id", "")
    st.session_state["form_data"].setdefault("indicad_id", "")

def cadastro_macroprocesso_pai():
    st.title("Cadastro de Macroprocessos Pai")

    # Inicializa o form_data se não existir
    initialize_form_data()

    # Campos do formulário utilizando os valores do dicionário form_data
    gerenc_id = st.text_input("ID da Gerência", value=st.session_state["form_data"]["gerenc_id"])
    missao = st.text_input("Missão", value=st.session_state["form_data"]["missao"])
    dono_id = st.number_input("ID do Dono", min_value=0, value=int(st.session_state["form_data"]["dono_id"]) if st.session_state["form_data"]["dono_id"].isdigit() else 0)
    exig_qual = st.text_input("Exigências de Qualificação", value=st.session_state["form_data"]["exig_qual"])
    avo_id = st.number_input("ID do Avô", min_value=0, value=int(st.session_state["form_data"]["avo_id"]) if st.session_state["form_data"]["avo_id"].isdigit() else 0)
    indicad_id = st.text_input("ID dos Indicadores", value=st.session_state["form_data"]["indicad_id"])

    with st.form("cadastro_form"):
        if st.form_submit_button("Cadastrar"):
            with get_session() as session:
                repo = PrcMacroprocessoPaiRepository(session)

                # Atualiza o dicionário form_data com os valores do formulário
                st.session_state["form_data"].update({
                    "gerenc_id": gerenc_id,
                    "missao": missao,
                    "dono_id": dono_id,
                    "exig_qual": exig_qual,
                    "avo_id": avo_id,
                    "indicad_id": indicad_id,
                })

                try:
                    # Cadastra o macroprocesso pai usando os valores do dicionário form_data
                    novo_macroprocesso_pai = repo.create(Prc_Macropr_Pai(
                        PRC_MACROPR_PAI_GERENC_ID=st.session_state["form_data"]["gerenc_id"],
                        PRC_MACROPR_PAI_MISSAO=st.session_state["form_data"]["missao"],
                        PRC_MACROPR_PAI_DONO_ID=st.session_state["form_data"]["dono_id"],
                        PRC_MACROPR_PAI_EXIG_QUAL=st.session_state["form_data"]["exig_qual"],
                        PRC_MACROPR_AVO_ID=st.session_state["form_data"]["avo_id"],
                        PRC_MACROPR_INDICAD_ID=st.session_state["form_data"]["indicad_id"],
                        PRC_MACROPR_DT_CRIACAO=datetime.now(),
                    ))
                    st.success(f"Macroprocesso Pai cadastrado com sucesso! (ID: {novo_macroprocesso_pai.PRC_MACROPR_PAI_ID})")

                    # Limpa o dicionário form_data após o cadastro
                    initialize_form_data()

                    # Reinicia o aplicativo para limpar o formulário
                    st.experimental_rerun()

                except ValueError as e:
                    st.error(str(e))

# Lógica principal
if st.session_state.get("logged_in", False):
    cadastro_macroprocesso_pai()
else:
    st.warning("Você precisa fazer login para acessar esta página.")

