import streamlit as st
from utils import check_login

st.set_page_config(page_title="Gestão Versus", layout="wide")

def login_page():
    st.title("Gestão Versus - Login")
    email = st.text_input("E-mail")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        if check_login(email, password):
            st.session_state["logged_in"] = True
            st.success("Login realizado com sucesso!")
            st.info("Agora você pode acessar as outras páginas do sistema.")
            st.experimental_rerun()
        else:
            st.error("E-mail ou senha inválidos!")

def home_page():
    st.write("# Bem-vindo ao Sistema de Gestão de Processos da Versus Gestão Corporativa")
    st.write("Nosso objetivo é transformar sua empresa na MELHOR VERSÃO DELA MESMA!")
    st.write("Use o menu lateral para navegar entre as diferentes funcionalidades do sistema.")
    st.warning("Usuário: Fulano de tal")
    st.warning("Atividades Pendentes")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    home_page()

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

st.sidebar.success("Selecione uma página acima.")
