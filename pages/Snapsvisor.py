import streamlit as st

from utils import setup_initial_session_state
#create streamlit link to https://sjung.rebeccalofgren.se/


setup_initial_session_state()
header = st.container()
header.title("Snapsvisor")
st.markdown("### [Löfgrens snapsvisor!](https://sjung.rebeccalofgren.se/)")
