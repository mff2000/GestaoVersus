import streamlit as st
from utils import check_login
from ui_utils import add_bg_from_local

# Configuração da página
st.set_page_config(
    page_title="Gestão Versus", layout="wide", page_icon="assets/Icone_Versus.jpg"
)
add_bg_from_local("assets\Logo_Versus_Clara.png")

# Estilos CSS personalizados
st.markdown(
    """
<style>
    .reportview-container {
        background: transparent;
    }
    .main {
        background-color: rgba(255,255,255,0.7);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #003366;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: rgba(0,51,102,0.8);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)


# Função para página de login
def login_page():
    st.markdown(
        "<h1 style='text-align: center; color: #003366;'>Gestão Versus - Login</h1>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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


# Função para página principal após o login
def home_page():
    st.markdown(
        "<h1 style='text-align: center; color: #003366;'>Versus Gestão Corporativa</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center;'>Bem-vindo ao Nosso Sistema de Gestão de Processos</h3>",
        unsafe_allow_html=True,
    )
    st.write("Nosso objetivo é transformar sua empresa na:")
    st.markdown(
        "<h2 style='text-align: center; color: #003366;'>Melhor Versão De Si Mesma!</h2>",
        unsafe_allow_html=True,
    )
    st.write("Use o menu lateral para navegar entre as diferentes funcionalidades do sistema.")

    # Linha divisória
    st.markdown("---")

    st.markdown(
        "<h2 style='text-align: center; color: green;'>Acompanhamento de Atividades</h2>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("**Título da Atividade**")

    with col2:
        st.write("Responsável")

    with col3:
        st.write("Prazo")

    with col4:
        st.write("Processo / Projeto")

    with col5:
        st.write("Status")


# Verifica se o usuário está logado
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Lógica principal da aplicação
def app():
    if not st.session_state["logged_in"]:
        login_page()
    else:
        home_page()

        # Configuração do sidebar (dentro do bloco if para mostrar apenas quando logado)
        with st.sidebar:
            with st.expander("Gerenc. Processos"):
                st.link_button("Cadastro de Processos", "Cadastro_Processos")

            # Adicione aqui os itens do menu

            st.markdown(
                "<div style='position: fixed; bottom: 0; left: 0; padding: 10px; color: black;'>Selecione uma página acima.</div>",
                unsafe_allow_html=True,
            )

        # Botão de logout
        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()

# Executa a aplicação
if __name__ == "__main__":
    app()
