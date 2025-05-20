from pathlib import Path
import streamlit as st

PDF_DIR = Path("./assets/pdfs")

@st.cache_data
def list_pdfs(base_tag: str):
    """Retorna todos os arquivos .pdf em assets/pdfs cujo nome contenha base_tag."""
    if not PDF_DIR.exists():
        return []
    return [
        p for p in PDF_DIR.glob("*.pdf")
        if base_tag in p.name
    ]

def render_buttons(base_tag: str):
    st.write("### Download PDF")
    pdfs = list_pdfs(base_tag)
    
    if not pdfs:
        st.info(f"Não há PDFs contendo '{base_tag}'.")
        return

    col1, col2 = st.columns(2)
    for pdf_path in pdfs:
        name = pdf_path.name.lower()
        # define coluna e rótulo conforme o tipo
        if "metadados" in name:
            target_col = col1
            label = "Download Ficha de Metadados"
        elif "dicionario" in name:
            target_col = col2
            label = "Download Dicionário de Variáveis"
        else:
            # ignora outros arquivos
            continue

        # cria o botão dentro da coluna apropriada
        with target_col:
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label=label,
                    data=f,
                    file_name=pdf_path.name,
                    mime="application/pdf"
                )
