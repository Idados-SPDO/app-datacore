# favorites_manager.py

import streamlit as st
from snowflake.snowpark import Session

@st.cache_resource
def get_session():
    return Session.builder.configs(st.secrets["snowflake"]).create()

def load_favorites():
    """Lê do banco e **atribui** em session_state['favorites']."""
    rows = get_session().sql(
        "SELECT TAG FROM BASES_SPDO.DB_APP_DATACORE.TB_DATACORE_FAVORITES"
    ).collect()
    tags = [r["TAG"] for r in rows]
    st.session_state.favorites = tags
    return tags

def add_favorite(tag: str):
    get_session().sql(f"""
        MERGE INTO BASES_SPDO.DB_APP_DATACORE.TB_DATACORE_FAVORITES AS tgt
        USING (SELECT '{tag}' AS TAG) AS src
          ON tgt.TAG = src.TAG
        WHEN MATCHED THEN UPDATE SET FAVORITED_AT = CURRENT_TIMESTAMP()
        WHEN NOT MATCHED THEN INSERT (TAG, FAVORITED_AT)
          VALUES (src.TAG, CURRENT_TIMESTAMP())
    """).collect()

def remove_favorite(tag: str):
    get_session().sql(f"""
        DELETE FROM BASES_SPDO.DB_APP_DATACORE.TB_DATACORE_FAVORITES
        WHERE TAG = '{tag}'
    """).collect()
