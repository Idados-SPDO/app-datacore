import streamlit as st
from data.solutions import data_solutions

def solutions_page():
    st.title('Soluções')
    def multiple_cards_component_solutions(cards, columns=3):
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
                    if "tipos" in tile_data and isinstance(tile_data["tipos"], list):
                        type_tag_style = "display:inline-block; background-color:#f0f0f5; padding:4px 8px; border-radius:8px; margin:2px;"
                        type_tags_html = " ".join([f'<span style="{type_tag_style}">{t}</span>' for t in tile_data["tipos"]])
                        tile.markdown(type_tags_html, unsafe_allow_html=True)
                    tile.link_button("Clique aqui", tile_data["link"], type="primary")
                    tile_index += 1
    multiple_cards_component_solutions(data_solutions, columns=3)

