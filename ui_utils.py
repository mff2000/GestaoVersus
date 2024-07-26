import streamlit as st
import base64


def add_bg_from_local(image_file):
    """Adiciona uma imagem de fundo a partir de um arquivo local."""
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: 50% auto;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main {{
            background-color: rgba(255, 255, 255, 0.7); /* Cor de fundo do container principal */
            padding: 20px;
            border-radius: 10px;
        }}
        h1, h2, h3 {{
            color: #003366; /* Cor dos títulos */
        }}
        .stButton button {{
            background-color: #007BFF; /* Cor de fundo do botão (azul) */
            color: white;
            border: none;
        }}
        .stTextInput input {{
            border: 1px solid #CED4DA; /* Borda cinza suave */
            border-radius: 5px;
        }}
        .stTextArea textarea {{
            border: 1px solid #CED4DA;
            border-radius: 5px;
        }}
        .stTabs [data-baseweb="tab-list"] button {{
            background-color: #E9ECEF; /* Cor de fundo das abas (cinza claro) */
        }}
        .stTabs [data-baseweb="tab-list"] button:hover {{
            background-color: #DEE2E6; /* Cor de fundo das abas ao passar o mouse */
        }}
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
            background-color: #007BFF; /* Cor de fundo da aba selecionada (azul) */
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
