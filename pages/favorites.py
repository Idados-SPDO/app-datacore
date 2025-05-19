import streamlit as st
from data.links import data_links
from components.details import show_base_details
from utils.favorite_manager import load_favorites, remove_favorite

def favorite_page():
    st.title("Favoritos")
    favorites = load_favorites()
    if not favorites:
        st.warning("Nenhuma base foi favoritada.")
        return

    for db in [d for d in data_links["data"] if d["tag"] in favorites]:
        name_col, star_col = st.columns([7,1])
        with name_col:
            if st.button(db["name"], key=f"fav_base_{db['tag']}"):
                show_base_details(db["tag"])
        with star_col:
            if st.button("★", key=f"fav_un_{db['tag']}",
                         on_click=remove_favorite,
                         args=(db["tag"],)):
                st.rerun()
