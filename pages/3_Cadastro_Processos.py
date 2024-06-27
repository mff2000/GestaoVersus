import streamlit as st
from utils import create_process
from ui_utils import add_bg_from_local, set_styles

# Configuração da página
st.set_page_config(page_title="Outra Página", layout="wide", page_icon="assets/Icone_Versus.jpg")
add_bg_from_local('assets\Logo_Versus_Clara.png')  # Use a mesma imagem ou outra
set_styles()

def cadastro_page():
    st.title("Cadastro de Processos")

    # Form
    with st.form("cad_proc_form", clear_on_submit=False):
        # First row with three columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            prc_codigo = st.text_input("Código", max_chars=19)
        
        with col2:
            macroprocesso_pai = st.selectbox("Macroprocesso Pai", ["Opção 1", "Opção 2"])  # Adjust options as needed
        
        with col3:
            nivel = st.number_input("Nível", min_value=0, max_value=999)
        
        # Second row with two columns
        col4, = st.columns(1)
        
        with col4:
            prc_nome = st.text_input("Nome", max_chars=256)
        
        # Third row with single column
        prc_objetivo = st.text_area("Objetivo do Processo", max_chars=512)

        # Tabs for bottom sections
        tabs = st.tabs(["Conhecimento", "Estrutura", "Times/Rotinas", "Outros", "Conformidade", "Atividades/POPs"])

        with tabs[0]:
            st.subheader("Conhecimento")
            conhecimento_tecnico = st.number_input("Conhecimento Técnico Nota", min_value=0, max_value=999)
            conhecimento_gestao = st.number_input("Conhecimento de Gestão Nota", min_value=0, max_value=999)
            conhecimento_relacionamento = st.number_input("Conhecimento de Relacionamento Nota", min_value=0, max_value=999)
            conhecimento_desc = st.text_area("Conhecimento Descrição e Observações")
        
        with tabs[1]:
            st.subheader("Estrutura")
            estrutura_fisica = st.number_input("Estrutura Física Nota", min_value=0, max_value=999)
            estrutura_fisica_desc = st.text_area("Estrutura Física Descrição", max_chars=256)
            estrutura_logica = st.number_input("Estrutura Lógica Nota", min_value=0, max_value=999)
            estrutura_logica_desc = st.text_area("Estrutura Lógica Descrição", max_chars=256)
        
        with tabs[2]:
            st.subheader("Times/Rotinas")
            times = st.multiselect("Times", ["Opção 1", "Opção 2", "Opção 3", "Opção 4"])  # Ajuste as opções conforme necessário
            rotina = st.selectbox("Rotina", ["Opção 1", "Opção 2"])  # Adjust options as needed
        
        with tabs[3]:
            st.subheader("Outros")
            modelagem = st.selectbox("Modelagem", ["Opção 1", "Opção 2"])  # Adjust options as needed
            recurso = st.multiselect("Recurso Utilizado", ["Opção 1", "Opção 2", "Opcao 3"])  # Adjust options as needed
            fornecedores = st.text_area("Fornecedores e Itens Consumidos")

        with tabs[4]:
            st.subheader("Conformidade")
            compliance = st.multiselect("Compliance", ["Opção 1", "Opção 2"])  # Adjust options as needed
            auditoria = st.multiselect("Auditoria", ["Opção 1", "Opção 2"])  # Adjust options as needed

        with tabs[5]:
            st.subheader("Atividades/POPs")
            atividade = st.selectbox("Atividade", ["Opção 1", "Opção 2"])  # Adjust options as needed
            pop_da_atividade = st.text_area("Pop da Atividade")

        # Form submission buttons
        if st.form_submit_button("Salvar"):
            if create_process(prc_codigo, prc_nome):
                st.success("Processo cadastrado com sucesso!")
            else:
                st.error("Erro ao cadastrar processo.")

        if st.form_submit_button("Limpar"):
            st.experimental_rerun()

if st.session_state.get("logged_in", False):
    cadastro_page()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
