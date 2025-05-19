from snowflake.snowpark import Session
import streamlit as st

connection_parameters = st.secrets["snowflake"]

@st.cache_resource
def get_session():
    return Session.builder.configs(connection_parameters).create()
