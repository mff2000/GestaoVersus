import streamlit as st
from utils import check_login, get_all_processes

st.set_page_config(page_title="Página Principal", layout="wide")

def main_page():
    st.title("Página Principal")
    st.write("Bem-vindo à página principal!")

    # Exibir os processos cadastrados
    st.subheader("Processos Cadastrados")
    processes = get_all_processes()
    for process in processes:
        st.write(process)

if st.session_state.get("logged_in", False):
    main_page()
else:
    st.warning("Você precisa fazer login para acessar esta página.")
