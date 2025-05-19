import streamlit as st
from data.links import data_links
from data.solutions import data_solutions
from components.cards import multiple_cards_component
from components.report import render_report, render_summary
from utils.download import download_pdf

@st.dialog("Detalhes da Base", width="large")
def show_base_details(base_tag):
    base_data = next((db for db in data_links["data"] if db["tag"] == base_tag), None)
    if not base_data:
        st.error("Base de dados não encontrada.")
        return

    st.title(f"Base: {base_data['name']}")
    tabs = st.tabs(["Relatório", "Resumo", "Soluções", "Downloads"])

    with tabs[0]:
        render_report(base_tag)
    with tabs[1]:
        render_summary(base_tag)
    with tabs[2]:
        sols = [sol for sol in data_solutions if sol["tag"] == base_tag]
        if sols:
            st.subheader("Soluções para esta Base")
            multiple_cards_component(sols, columns=3)
        else:
            st.info("Nenhuma solução encontrada para esta base.")
    with tabs[3]:
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "Baixar Metadados",
                data=download_pdf(),
                file_name=base_data["links"][0]["sublinks"][0]["file_name"],
                mime="application/pdf"
            )
        with col2:
            st.download_button(
                "Baixar Dicionário de Variáveis",
                data=download_pdf(),
                file_name=base_data["links"][1]["sublinks"][0]["file_name"],
                mime="application/pdf"
            )
