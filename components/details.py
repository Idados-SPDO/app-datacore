import streamlit as st
from config import get_session 
from data.links import data_links
from data.solutions import data_solutions
from components.cards import multiple_cards_component
from components.report import render_report, render_summary
from components.download_pdf_buttons import render_buttons

@st.dialog("Detalhes da Base", width="large")
def show_base_details(base_tag):
    base_data = next((db for db in data_links["data"] if db["tag"] == base_tag), None)
    if not base_data:
        st.error("Base de dados não encontrada.")
        return

    st.title(f"Base: {base_data['name']}")
    tabs = st.tabs(["Resumo", "Relatório", "Soluções", "Downloads"])

    with tabs[0]:
        render_summary(base_tag)
    with tabs[1]:
        render_report(base_tag)
    with tabs[2]:
        sols = [sol for sol in data_solutions if sol["tag"] == base_tag]
        if sols:
            st.subheader("Soluções para esta Base")
            multiple_cards_component(sols, columns=3)
        else:
            st.info("Nenhuma solução encontrada para esta base.")

    with tabs[3]:
        render_buttons(base_tag)
