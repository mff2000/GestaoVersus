# -*- coding: utf-8 -*-
import streamlit as st
import sys

# Configuração da página
#st.set_page_config(layout="wide")

# Configurar a codificação padrão do sistema para UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


# Lista de itens do menu
menu_items_list_movimentos = [
    "01 - Dashboard de Indicadores de Processos",
    "02 - Gestao de Indicadores e Metas",
    "03 - Mapa de Processos",
    "04 - Processos - Cadastro de Processos",
    "05 - Processos - Cadastro de Atividades de Processos",
]

menu_items_list_cadastro = [
    "06 - Processos - Rotinas",
    "07 - Geral - Cadastro de Colaboradores",
    "08 - Geral - Cadastro de Indicadores e Metas",
    "09 - Processos - Conhecimento Tecnico / Gestao / Requisitos",
    "10 - Processos - Fornecedores | Insumos Consumidos",
    "11 - Processos - Estrutura Fisica",
    "12 - Processos - Estrutura Logica",
    "13 - Processos - Capacidade Operacional",
    "14 - Processos - Compliance",
    "15 - Processos - Auditoria",
    "16 - Processos - Modelagem",
    "99 - Sair"
]

# Adicionar CSS para definir o tamanho fixo dos botões e alinhar na parte superior
st.markdown("""
<style>
    .stApp {
    padding-top: 1rem; /* Adiciona um pequeno preenchimento para evitar que o título grude na barra lateral */
}
    .stApp { /* Alterado para a classe 'stApp' */
        display: flex;
        flex-direction: column; 
        align-items: flex-start; 
        min-height: 100vh; 
    }
    
    .stApp {
    margin-top: 0; /* Remove a margem superior padrão do contêiner principal */
    padding-top: 0; /* Remove o preenchimento superior padrão do contêiner principal */
}

.centered-title { /* Remove as margens e preenchimentos do título */
    margin: 0;
    padding: 0;
}

.css-18e3th9 { /* Remove o preenchimento superior de outro elemento */
    padding-top: 0;
}
    .stButton button {
        height: 150px;
        width: 175px;
    }
    .centered-title {
        text-align: center;
        margin-top: 0;
        padding-top: 0;
    }
    .css-18e3th9 {
        padding-top: 0px;
    }
    .vertical-text {
        writing-mode: vertical-rl;
        text-orientation: mixed;
        transform: rotate(180deg);
        margin-top: 50px;
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

# Título centralizado
col1, col2 = st.columns([1,6])
with col1:
    ''
with col2:
    st.markdown("<h1 class='centered-title'>Versus Gestao Corporativa</h1>", unsafe_allow_html=True)

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