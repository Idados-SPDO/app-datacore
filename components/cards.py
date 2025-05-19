# components/cards.py
import streamlit as st

def multiple_cards_component(cards, columns=3):
    rows = (len(cards) + columns - 1) // columns
    tile_index = 0
    for _ in range(rows):
        cols = st.columns(columns)
        for col in cols:
            if tile_index < len(cards):
                tile_data = cards[tile_index]
                tile = col.container(height=450)
                tag_style = "display:inline-block; background-color:#e1e1eb; padding:4px 8px; border-radius:8px; margin:2px;"
                tags_html = f'<span style="{tag_style}">{tile_data["tag"].capitalize()}</span>'
                tile.markdown(tags_html, unsafe_allow_html=True)
                tile.write(tile_data["titulo"])
                tile.write(tile_data["descricao"])
                tile.link_button("Clique aqui", tile_data["link"], type="primary")
                tile_index += 1