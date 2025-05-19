import streamlit as st

def home_page():
    st.markdown("<h1 style='text-align: center; font-size:100px;'>Datacore</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>CENTRAL DE GERENCIAMENTO DE DADOS</h1>", unsafe_allow_html=True)
    st.markdown("""
        <h1 style='text-align: justify; font-size:18px; font-weight:lighter;'>
        O <strong>Datacore</strong> é um ponto central para o gerenciamento e processamento de dados, garantindo a funcionalidade eficiente de sistemas e redes de informação. 
        Ele proporciona um ambiente estruturado para armazenar, organizar e compartilhar dados de forma otimizada, promovendo colaboração e tomada de decisões embasadas.
        </h1>
    """, unsafe_allow_html=True)
