import streamlit as st
from config import get_session
from pages.home import home_page
from pages.search import search_page
from pages.favorites import favorite_page
from pages.solutions import solutions_page
from pages.database import database_page

st.set_page_config(
    page_title="SPDO DataCore",
    page_icon="fgv_logo.png",
    layout="wide",
)

# cria sessão Snowflake
session = get_session()

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# menu de navegação
pg = st.navigation([
    st.Page(home_page, title="Home", icon=":material/home:"), 
    #st.Page(database_page, title="Pesquisa", icon=":material/search:"),
    st.Page(search_page, title="Documentação", icon=":material/description:"),
    st.Page(favorite_page, title="Favoritos", icon=":material/star:"), 
    st.Page(solutions_page, title="Soluções", icon=":material/dashboard:"),
])
st.logo('ibre_logo.png')

pg.run()
