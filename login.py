# -*- coding: utf-8 -*-
import streamlit as st
from pathlib import Path
import sys

# Configuração da página
st.set_page_config(page_icon=":key:", layout="wide")

# Carregue a imagem
#with open('C:\GestaoVersus\Suporte\Imagens\Imagem_Login.png', 'rb') as f:
#    image_data = f.read()

    # Exibe a imagem na tela
#st.image(image_data, caption='Imagem de Exemplo', width=400)

# Cria a barra lateral
#with st.sidebar:
#    st.checkbox()

sys.path.append(str(Path('c:/gestaoversus/bd').resolve()))
from conexao_bd import connect_db

# Função para verificar as credenciais de login
def check_login(email, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT GER_USU_EMAIL, GER_USU_SENHA FROM GER_USUARIOS WHERE GER_USU_EMAIL=%s AND GER_USU_SENHA=%s", (email, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result is not None

# Estilo CSS personalizado
def set_css():
    st.markdown("""
        <style>
            body {
                background-image: url("C:/GestaoVersus/Suporte/Imagens/Imagem_Login.png");  /* Adjust path if necessary */
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
    """, unsafe_allow_html=True)

# Função para exibir a página de login
def show_login_page():
    st.markdown("<h2 style='text-align: center;'>Gestão Versus - Login</h2>", unsafe_allow_html=True)
    email = st.text_input("E-mail")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        if check_login(email, password):
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error("E-mail ou senha inválidos!")

# Função para exibir a página principal
def show_main_page():
    # Remove o CSS específico da página de login antes de carregar a página principal
    st.markdown("""
        <style>
            .main {
                max-width: none;
                margin: 0;
            }
        </style>
    """, unsafe_allow_html=True)
    exec(Path("c:/gestaoversus/main.py").read_text())

# Aplicar CSS personalizado
set_css()

# Verificar se o usuário está logado
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    show_main_page()
else:
    show_login_page()
