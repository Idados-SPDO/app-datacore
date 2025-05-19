# pages/database.py

import streamlit as st
from config import get_session
from snowflake.snowpark.functions import col, lower

@st.cache_resource
def session() -> "snowpark.Session":
    return get_session()

def database_page():
    st.title("Banco de Dados")

    # 1) Escolha do schema/base
    db_options = {
        "Pastorinho": "BASES_SPDO.DB_ADD_PASTORINHO",
        "Receita":    "BASES_IBRE.DB_GOVERNAMENTAIS",
    }
    selected_db = st.selectbox("Selecione o Banco de Dados", list(db_options.keys()))
    if not selected_db:
        return
    db_fullname = db_options[selected_db]

    # 2) Campo de busca
    search_term = st.text_input(
        "🔍 Pesquise pelo que deseja",
        placeholder="Digite um termo e pressione Enter",
        key="db_search_term",
        value=st.session_state.get("db_search_term", "")
    )
    if not search_term:
        st.info("Digite algo para iniciar a busca.")
        return

    # 3) Botão para limpar
    def _clear():
        st.session_state["db_search_term"] = ""
        st.rerun()

    st.button("🧹 Limpar busca", on_click=_clear)

    # 4) Obtém lista de tabelas
    with st.spinner(f"Listando tabelas em {db_fullname}..."):
        tables = session().sql(f"SHOW TABLES IN {db_fullname}").collect()
        table_names = [t["name"] for t in tables]

    n_tables = len(table_names)
    progress_bar = st.progress(0)
    status_text = st.empty()

    any_results = False
    termo = search_term.lower()

    # 5) Percorre cada tabela, atualiza progresso e exibe resultados
    for idx, tbl_name in enumerate(table_names, start=1):
        status_text.text(f"🔎 Buscando em `{tbl_name}` ({idx}/{n_tables})")
        progress_bar.progress(idx / n_tables)

        # pega colunas
        desc = session().sql(f"DESCRIBE TABLE {db_fullname}.{tbl_name}").collect()
        cols = [row["name"] for row in desc]
        tbl = session().table(f"{db_fullname}.{tbl_name}")

        # monta expressão case‐insensitive
        expr = None
        for c in cols:
            pred = lower(col(c)).like(f"%{termo}%")
            expr = pred if expr is None else expr | pred

        # executa e converte
        df = tbl.filter(expr).limit(2000).to_pandas()

        if not df.empty:
            any_results = True
            with st.expander(f"📄 {tbl_name} ({len(df)} registros)", expanded=False):
                st.dataframe(df, use_container_width=True)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "📥 Baixar resultados",
                    data=csv,
                    file_name=f"{tbl_name}_resultados.csv",
                    mime="text/csv"
                )

    # 6) Mensagem final
    if not any_results:
        st.warning("Nenhum registro encontrado em nenhuma tabela.")

    # 7) Limpa status e barra
    progress_bar.empty()
    status_text.empty()
