# pages/database.py

import streamlit as st
from config import get_session
from snowflake.snowpark.functions import col, lower

@st.cache_resource
def session() -> "snowpark.Session":
    return get_session()

def database_page():
    st.title("Pesquisa")
    st.markdown(
        """
        Aqui você pode pesquisar em tabelas de dados disponíveis no Snowflake.
        O resultado da pesquisa será exibido em uma tabela.
        """
    )

    # 1) Seus bancos
    db_options = {
        "Pastorinho": "BASES_SPDO.DB_ADD_PASTORINHO",
        "Horus":    "BASES_SPDO.DB_ADD_HORUS",
        "Receita":     "BASES_IBRE.DB_GOVERNAMENTAIS",
    }
    selected_db = st.selectbox("Selecione o Banco de Dados", list(db_options.keys()))
    if not selected_db:
        return
    db_fullname = db_options[selected_db]

    # 2) Lista as tabelas
    with st.spinner(f"Listando tabelas em {db_fullname}..."):
        tables = session().sql(f"SHOW TABLES IN {db_fullname}").collect()
        table_names = [t["name"] for t in tables]
    selected_table = st.selectbox("Selecione a tabela", table_names)
    if not selected_table:
        return

    # 3) Caixa de busca (usa value para garantir que pegue o estado)
    search_term = st.text_input(
        "🔍 Pesquise pelo que deseja",
        placeholder="Digite um termo e pressione Enter",
        key="db_search_term",
        value=st.session_state.get("db_search_term", "")
    )
    if not search_term:
        st.info("Digite algo para iniciar a busca.")
        return

    # 4) Monta e executa o filtro com Snowpark (case-insensitive)
    with st.spinner("Preparando busca..."):
        desc = session().sql(f"DESCRIBE TABLE {db_fullname}.{selected_table}").collect()
        cols = [row["name"] for row in desc]
        tbl = session().table(f"{db_fullname}.{selected_table}")

        termo = search_term.lower()
        expr = None
        for c in cols:
            pred = lower(col(c)).like(f"%{termo}%")
            expr = pred if expr is None else expr | pred

        df = tbl.filter(expr).limit(2000).to_pandas()

    st.success(f"{len(df)} registro(s) encontrados")
    st.dataframe(df, use_container_width=True)

    # 5) Botões Limpar + Baixar na mesma linha
    def _clear():
        # atribui string vazia e forçar rerun antes de renderizar tudo de novo
        st.session_state["db_search_term"] = ""
        st.rerun()

    c1, c2 = st.columns([1,1])
    with c1:
        st.button("🧹 Limpar busca", on_click=_clear)
    with c2:
        if not df.empty:
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "📥 Baixar resultados",
                data=csv,
                file_name=f"{selected_table}_resultados.csv",
                mime="text/csv"
            )
