# app.py

import streamlit as st
import os
from login_page import login_page

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        os.system('streamlit run c:\\GestaoVersus\\main_2.py')
    else:
        login_page()

if __name__ == "__main__":
    main()
