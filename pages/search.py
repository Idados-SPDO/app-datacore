# search_page.py

import streamlit as st
from data.links import data_links
from components.details import show_base_details
from utils.favorite_manager import load_favorites, add_favorite, remove_favorite

def search_page():
    st.title("Documentação das Bases de Dados")
    q = st.text_input("Pesquisar base por nome:")

    # Puxa sempre a lista atual de favoritos
    favorites = load_favorites()

    filtered = [
        db for db in data_links["data"]
        if q.lower() in db["name"].lower()
    ]

    for db in filtered:
        col, star_col = st.columns([7,1])
        with col:
            if st.button(db["name"], key=f"base_{db['tag']}"):
                show_base_details(db["tag"])
        with star_col:
            is_fav = db["tag"] in favorites
            icon = "★" if is_fav else "☆"
            if st.button(icon, key=f"fav_{db['tag']}",
                         on_click=(remove_favorite if is_fav else add_favorite),
                         args=(db["tag"],)):
                # força um rerun para recarregar load_favorites()
                st.rerun()
