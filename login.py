# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path

from infra.configs.connection import DBConnectionHandler
from sqlalchemy import text

# Função para verificar as credenciais de login
def check_login(email, password):
    with DBConnectionHandler() as db_connection:
        session = db_connection.session
        user = session.execute(
            text("SELECT GER_USU_EMAIL, GER_USU_SENHA FROM GER_USUARIOS WHERE GER_USU_EMAIL = :email AND GER_USU_SENHA = :password"),
            {"email": email, "password": password}
        ).fetchone()

        return user is not None

# Estilo CSS personalizado
def set_css():
    st.markdown(
        """
        <style>
            body {
                background-image: url("C:/GestaoVersus/Suporte/Imagens/Imagem_Login.png"); /* Ajuste o caminho */
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                margin: 0;
            }
            .main {
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                max-width: 400px;
                margin: auto;
            }
            .stButton button {
                width: 100%;
                background-color: #1f77b4;
                color: white;
                font-weight: bold;
            }
            .stTextInput input {
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Função para exibir a página de login
def show_login_page():
    set_css()
    st.markdown(
        "<h2 style='text-align: center;'>Gestão Versus - Login</h2>",
        unsafe_allow_html=True,
    )
    email = st.text_input("E-mail")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        if check_login(email, password):
            st.session_state["logged_in"] = True
            st.experimental_rerun()
        else:
            st.error("E-mail ou senha inválidos!")

# Função para exibir a página principal
def show_main_page():
    exec(Path("c:/gestaoversus/main.py").read_text(encoding='utf-8'))

# Verificar se o usuário está logado
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    show_main_page()
else:
    show_login_page()
