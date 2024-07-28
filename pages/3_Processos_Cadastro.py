import streamlit as st
from infra.repository.prc_cad_repository import PrcCadRepository
from infra.configs.base import get_session
from ui_utils import add_bg_from_local
from infra.entities.Prc_Cad import Prc_Cad

# Configuração da página
st.set_page_config(
    page_title="Processos Cadastro", layout="wide", page_icon="assets/Icone_Versus.jpg"
)
add_bg_from_local("assets\Logo_Versus_Clara.png")  # Use a mesma imagem ou outra


# --- FUNÇÕES ---


def create_process(prc_cad_repo, process_data):
    """Cria um novo processo usando o repositório."""
    try:
        new_process = prc_cad_repo.create(process_data)  # Passa o objeto Prc_Cad
        return new_process
    except ValueError as e:
        st.error(str(e))
        return None


def cadastro_page():
    st.title("Cadastro de Processos")

    # Form
    with st.form("cad_proc_form", clear_on_submit=True):
        # First row with three columns
        col1, col2, col3 = st.columns(3)

        with col1:
            prc_codigo = st.text_input("Código", max_chars=19)

        with col2:
            macroprocesso_pai = st.selectbox(
                "Macroprocesso Pai", ["Opção 1", "Opção 2"]
            )  # Adjust options as needed

        with col3:
            nivel = st.number_input("Nível", min_value=0, max_value=999)

        # Second row with two columns
        col4, col5 = st.columns(2)

        with col4:
            prc_nome = st.text_input("Nome", max_chars=256)

        with col5:
            modelagem_status = st.selectbox("Modelagem Status", ["Opção 1", "Opção 2"])

        # Third row with single column
        prc_objetivo = st.text_area("Objetivo do Processo", max_chars=512)

        # Tabs for bottom sections
        tabs = st.tabs(
            [
                "Conhecimento",
                "Estrutura",
                "Times/Rotinas",
                "Recursos e Fornecedores",
                "Conformidade",
                "Fluxo/POP",
            ]
        )

        with tabs[0]:
            st.subheader("Conhecimento")
            conhecimento_tecnico = st.number_input(
                "Conhecimento Técnico Nota", min_value=0, max_value=999
            )
            conhecimento_gestao = st.number_input(
                "Conhecimento de Gestão Nota", min_value=0, max_value=999
            )
            conhecimento_relacionamento = st.number_input(
                "Conhecimento de Relacionamento Nota", min_value=0, max_value=999
            )
            conhecimento_desc = st.text_area("Conhecimento Descrição e Observações")

        with tabs[1]:
            st.subheader("Estrutura")
            estrutura_fisica = st.number_input(
                "Estrutura Física Nota", min_value=0, max_value=999
            )
            estrutura_fisica_desc = st.text_area(
                "Estrutura Física Descrição", max_chars=256
            )
            estrutura_logica = st.number_input(
                "Estrutura Lógica Nota", min_value=0, max_value=999
            )
            estrutura_logica_desc = st.text_area(
                "Estrutura Lógica Descrição", max_chars=256
            )

        with tabs[2]:
            st.subheader("Times/Rotinas")
            times = st.multiselect(
                "Times", ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
            )
            rotina = st.selectbox("Rotina", ["Opção 1", "Opção 2"])

        with tabs[3]:
            st.subheader("Recursos e Fornecedores")
            recurso = st.multiselect(
                "Recurso Utilizado", ["Opção 1", "Opção 2", "Opcao 3"]
            )
            fornecedores = st.text_area("Fornecedores e Itens Consumidos")

        with tabs[4]:
            st.subheader("Conformidade")
            compliance = st.multiselect("Compliance", ["Opção 1", "Opção 2"])
            auditoria = st.multiselect("Auditoria", ["Opção 1", "Opção 2"])

        with tabs[5]:
            st.subheader("Fluxo/POP")
            fluxo = st.text_input("Fluxo", max_chars=256)
            pop = st.text_input("POP", max_chars=256)

        col6, col7 = st.columns(2)

        # Form submission buttons
        with col6:
            if st.form_submit_button("Salvar"):
                # Obter os dados do formulário
                process_data = {
                    "PRC_CODIGO": prc_codigo,
                    "PRC_MP_PAI": macroprocesso_pai,
                    "PRC_NIVEL": nivel,
                    "PRC_NOME": prc_nome,
                    "PRC_MODELAGEM_STATUS": modelagem_status,
                    "PRC_OBJETIVO": prc_objetivo,
                    "PRC_CONHEC_TEC_NOTA": conhecimento_tecnico,
                    "PRC_CONHEC_GEST_NOTA": conhecimento_gestao,
                    "PRC_CONHEC_RELAC_NOTA": conhecimento_relacionamento,
                    "PRC_CONHEC_DESC_OBS": conhecimento_desc,
                    "PRC_ESTR_FISICA_NOTA": estrutura_fisica,
                    "PRC_ESTR_FISICA_DESCR": estrutura_fisica_desc,
                    "PRC_ESTR_LOGICA_NOTA": estrutura_logica,
                    "PRC_ESTR_LOGICA_DESCR": estrutura_logica_desc,
                    # ... (outros campos do formulário)
                }
                process_data = Prc_Cad(**process_data)  # Cria um objeto Prc_Cad

                # Obtenha a sessão do banco de dados (correção usando contextmanager)
                with get_session() as db_session:
                    prc_cad_repo = PrcCadRepository(db_session)

                    if prc_codigo:  # Editar processo existente
                        prc_cad_repo.update(prc_codigo, process_data)
                        st.success("Processo atualizado com sucesso!")
                    else:  # Criar novo processo
                        new_process = create_process(prc_cad_repo, process_data)
                        if new_process:
                            st.success("Processo cadastrado com sucesso!")
                        else:
                            # A mensagem de erro já foi exibida em create_process
                            pass

        with col7:
            if st.form_submit_button("Limpar"):
                st.experimental_rerun()

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()


# --- LÓGICA PRINCIPAL ---

if st.session_state.get("logged_in", False):
    cadastro_page()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
