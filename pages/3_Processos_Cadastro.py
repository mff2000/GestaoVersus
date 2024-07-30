import streamlit as st
from infra.repository.prc_cad_repository import PrcCadRepository
from infra.configs.base import get_session
from ui_utils import add_bg_from_local
from infra.entities.Prc_Cad import Prc_Cad
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Processos Cadastro", layout="wide", page_icon="assets/Icone_Versus.jpg"
)
add_bg_from_local("assets/Logo_Versus_Clara.png")  # Use a mesma imagem ou outra

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
            modelagem_status = st.selectbox("Modelagem Status", ["Fora do Radar", "Modelando", "Implant./Instavel", "Estabil./Entregue Audit"])

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
                "Times", ["1", "2", "3", "4"]
            )
            rotina = st.number_input(
                "Rotina", min_value=0, max_value=999
            )

        with tabs[3]:
            st.subheader("Recursos e Fornecedores")
            recurso = st.multiselect(
                "Recurso Utilizado", ["1", "2", "3"]
            )
            fornecedores = st.text_area("Fornecedores e Itens Consumidos")

        with tabs[4]:
            st.subheader("Conformidade")
            compliance = st.multiselect("Compliance", ["1", "2"])
            auditoria = st.multiselect("Auditoria", ["1", "2"])

        with tabs[5]:
            st.subheader("Fluxo/POP")
            fluxo = st.text_input("Fluxo", max_chars=256)
            pop = st.text_input("POP", max_chars=256)

        col6, col7 = st.columns(2)

        # Map string options to integer values
        macroprocesso_pai_mapping = {"Opção 1": 1, "Opção 2": 2}
        modelagem_status_mapping = {
            "Fora do Radar": "Fora do Radar",
            "Modelando": "Modelando",
            "Implant./Instavel": "Implant./Instavel",
            "Estabil./Entregue Audit": "Estalid./Engregue Audi"
        }

        # Form submission buttons
        with col6:
            if st.form_submit_button("Salvar"):
                # Obter os dados do formulário como um objeto Prc_Cad
                process_data = Prc_Cad(
                    PRC_CODIGO=prc_codigo,
                    PRC_MP_PAI=macroprocesso_pai_mapping[macroprocesso_pai],
                    PRC_NIVEL=nivel,
                    PRC_NOME=prc_nome,
                    PRC_MODELAGEM_STATUS=modelagem_status_mapping[modelagem_status],
                    PRC_OBJETIVO=prc_objetivo,
                    PRC_CONHEC_TEC_NOTA=conhecimento_tecnico,
                    PRC_CONHEC_GEST_NOTA=conhecimento_gestao,
                    PRC_CONHEC_RELAC_NOTA=conhecimento_relacionamento,
                    PRC_CONHEC_DESC_OBS=conhecimento_desc,
                    PRC_ESTR_FISICA_NOTA=estrutura_fisica,
                    PRC_ESTR_FISICA_DESCR=estrutura_fisica_desc,
                    PRC_ESTR_LOGICA_NOTA=estrutura_logica,
                    PRC_ESTR_LOGICA_DESCR=estrutura_logica_desc,
                    PRC_RECURSOS_UTILIZ_ID=None,  # ajustar conforme necessário
                    PRC_FORNE_ITENS_CONS=fornecedores,
                    PRC_FLUXO_PROC=fluxo,
                    PRC_POP_PROCESSO=pop,
                    PRC_COMPLIANCE_ID=None,  # ajustar conforme necessário
                    PRC_AUDITORIA_ID=None,  # ajustar conforme necessário
                    PRC_TIME_ID=times,
                    PRC_ROTINA_ID=rotina,
                    PRC_DT_CADASTRO=datetime.now(),  # Adiciona a data atual para DT_CADASTRO
                    PRC_DT_ALTERACAO=None,
                    PRC_DT_EXCLUSAO=None,
                )

                with get_session() as db_session:
                    prc_cad_repo = PrcCadRepository(db_session)

                    existing_process = prc_cad_repo.get_by_codigo(prc_codigo)

                    if existing_process:
                        st.error("Já existe um processo com esse código. Por favor, use um código diferente.")
                    else:
                        new_process = prc_cad_repo.create(process_data)
                        if new_process:
                            st.success("Processo cadastrado com sucesso!")
                        else:
                            st.error("Erro ao cadastrar o processo. Verifique os dados e tente novamente.")  # Mensagem de erro genérica

        with col7:
            if st.form_submit_button("Limpar"):
                st.rerun()

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()


# --- LÓGICA PRINCIPAL ---

if st.session_state.get("logged_in", False):
    cadastro_page()
else:
    st.warning("Você precisa fazer login para acessar esta página.")

