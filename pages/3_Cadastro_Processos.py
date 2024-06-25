import streamlit as st
from utils import create_process

st.set_page_config(page_title="Cadastro de Processos", layout="wide")

def cadastro_page():
    st.title("Cadastro de Processos")

    # Form
    with st.form("cad_proc_form", clear_on_submit=False):
        # First row with three columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            prc_codigo = st.text_input("Código", max_chars=256)
        
        with col2:
            macroprocesso_pai = st.selectbox("Macroprocesso Pai", ["Opção 1", "Opção 2"])  # Adjust options as needed
        
        with col3:
            nivel = st.number_input("Nível", min_value=0, max_value=999)
        
        # Second row with two columns
        col4, col5 = st.columns(2)
        
        with col4:
            prc_nome = st.text_input("Nome", max_chars=256)
        
        with col5:
            prc_tipo = st.text_input("Tipo de Processo", max_chars=256)
        
        # Third row with single column
        prc_objetivo = st.text_area("Objetivo do Processo", max_chars=256)

        # Tabs for bottom sections
        tabs = st.tabs(["Conhecimento", "Estrutura", "Dono/Times", "Gestão", "Atividades/POPs"])

        with tabs[0]:
            st.subheader("Conhecimento")
            conhecimento_tecnico = st.number_input("Conhecimento Técnico Nota", min_value=0, max_value=999)
            conhecimento_gestao = st.number_input("Conhecimento de Gestão Nota", min_value=0, max_value=999)
            conhecimento_relacionamento = st.number_input("Conhecimento de Relacionamento Nota", min_value=0, max_value=999)
            conhecimento_desc = st.text_area("Conhecimento Descrição e Observações")
        
        with tabs[1]:
            st.subheader("Estrutura")
            estrutura_fisica = st.number_input("Estrutura Física Nota", min_value=0, max_value=999)
            estrutura_fisica_desc = st.text_input("Estrutura Física Descrição", max_chars=256)
            estrutura_logica = st.number_input("Estrutura Lógica Nota", min_value=0, max_value=999)
            estrutura_logica_desc = st.text_input("Estrutura Lógica Descrição", max_chars=256)
        
        with tabs[2]:
            st.subheader("Dono/Times")
            dono = st.selectbox("Dono", ["Opção 1", "Opção 2"])  # Adjust options as needed
            time = st.selectbox("Time", ["Opção 1", "Opção 2"])  # Adjust options as needed
        
        with tabs[3]:
            st.subheader("Gestão")
            rotina = st.selectbox("Rotina", ["Opção 1", "Opção 2"])  # Adjust options as needed
            indicador = st.multiselect("Indicador", ["Opção 1", "Opção 2"])  # Adjust options as needed
            modelagem = st.selectbox("Modelagem", ["Opção 1", "Opção 2"])  # Adjust options as needed
            recurso = st.selectbox("Recurso Utilizado", ["Opção 1", "Opção 2"])  # Adjust options as needed
            fornecedores = st.text_area("Fornecedores e Itens Consumidos")
            compliance = st.multiselect("Compliance", ["Opção 1", "Opção 2"])  # Adjust options as needed
            auditoria = st.multiselect("Auditoria", ["Opção 1", "Opção 2"])  # Adjust options as needed

        with tabs[4]:
            st.subheader("Atividades/POPs")
            atividade = st.selectbox("Atividade", ["Opção 1", "Opção 2"])  # Adjust options as needed
            pop_da_atividade = st.text_area("Pop da Atividade")

        # Form submission buttons
        if st.form_submit_button("Salvar"):
            if create_process(prc_tipo, prc_nome):
                st.success("Processo cadastrado com sucesso!")
            else:
                st.error("Erro ao cadastrar processo.")

        if st.form_submit_button("Limpar"):
            st.experimental_rerun()

if st.session_state.get("logged_in", False):
    cadastro_page()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
