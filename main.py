# -*- coding: utf-8 -*-
import streamlit as st
import sys

# Configuração da página (apenas uma vez)
st.set_page_config(page_title="My App", page_icon=":key:", layout="wide", initial_sidebar_state="expanded")

# Configurar a codificação padrão do sistema para UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def custom_header(title):
    st.markdown(
        f"""
        <style>
            header {{
                background-color: #243F8E;
                padding: 4px;
                text-align: center;
                width: 100%; /* Garante que o cabeçalho ocupe toda a largura da tela */
                box-sizing: border-box; /* Inclui padding e border no cálculo da largura */
            }}
            header h1 {{
                margin: 0;
                color: white;
                font-family: Arial, sans-serif;
                font-size: 16px;
                word-wrap: break-word; /* Permite que o texto quebre em várias linhas */
            }}
            .stApp {{ /* Estiliza o container principal do Streamlit */
                max-width: 100%; /* Evita que o conteúdo ultrapasse a largura da tela */
                margin: 0 auto; /* Centraliza o conteúdo horizontalmente */
            }}
        </style>
        <header>
            <h1>{title}</h1>
        </header>
        """,
        unsafe_allow_html=True,
    )

custom_header("Versus Gestão Corporativa - Estruturação Empresarial")

# Lista de itens do menu
menu_items_list_movimentos = [
    "01 - Dashboard de Indicadores de Processos",
    "02 - Gestão de Indicadores e Metas",
    "03 - Mapa de Processos",
    "04 - Processos - Cadastro de Processos",
    "05 - Processos - Cadastro de Atividades de Processos",
]

menu_items_list_cadastro = [
    "06 - Processos - Rotinas",
    "07 - Geral - Cadastro de Colaboradores",
    "08 - Geral - Cadastro de Indicadores e Metas",
    "09 - Processos - Conhecimento Técnico / Gestão / Requisitos",
    "10 - Processos - Fornecedores | Insumos Consumidos",
    "11 - Processos - Estrutura Física",
    "12 - Processos - Estrutura Lógica",
    "13 - Processos - Capacidade Operacional",
    "14 - Processos - Compliance",
    "15 - Processos - Auditoria",
    "16 - Processos - Modelagem",
    "99 - Sair"
]

# Adicionar CSS para definir o tamanho fixo dos botões e alinhar na parte superior
st.markdown("""
<style>
    .css-18e3th9 { /* Remove o preenchimento superior de outro elemento */
        padding-top: 0;
    }
    .stButton button {
        height: 100px;
        width: 175px;
    }

    .vertical-text {
        writing-mode: vertical-rl;
        text-orientation: mixed;
        transform: rotate(180deg);
        margin-top: 10px;
        font-size: 20px;
        align-items: center;
    }
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 6fr;
        gap: 10px;
    }
    .grid-title {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# Função para criar botões em grade
def create_button_grid(items, title, cols=6):
    rows = len(items) // cols + (1 if len(items) % cols else 0)
    index = 0
    st.markdown(f"<div class='grid-title'>{title}</div>", unsafe_allow_html=True)
    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            if index < len(items):
                item = items[index]
                if item:
                    columns[col].button(item, key=item)
                index += 1

# Divisão da tela em duas partes
col1, col2 = st.columns([1, 6])
with col1:
    st.markdown("<div class='vertical-text'>Movimentos</div>", unsafe_allow_html=True)
with col2:
    create_button_grid(menu_items_list_movimentos,'')

# Adiciona uma linha horizontal
st.markdown("<hr>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])
with col1:
    st.markdown("<div class='vertical-text'>Cadastro</div>", unsafe_allow_html=True)
with col2:
    create_button_grid(menu_items_list_cadastro, '')
