import streamlit as st
import base64

@st.cache_data  # Adiciona o cache para a função
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
            background-color: rgba(255, 255, 255, 0.7); 
            padding: 20px;
            border-radius: 10px;
        }}
        h1, h2, h3 {{
            color: #003366; 
        }}
        .stButton button {{
            background-color: #007BFF; 
            color: white;
            border: none;
        }}
        .stTextInput input {{
            border: 1px solid #CED4DA; 
            border-radius: 5px;
        }}
        .stTextArea textarea {{
            border: 1px solid #CED4DA;
            border-radius: 5px;
        }}
        .stTabs [data-baseweb="tab-list"] button {{
            background-color: #E9ECEF; 
        }}
        .stTabs [data-baseweb="tab-list"] button:hover {{
            background-color: #DEE2E6; 
        }}
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
            background-color: #007BFF; 
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
