import streamlit as st

from utils import setup_initial_session_state

setup_initial_session_state()
header = st.container()
header.title("Cocktails")


st.image('images/cocktail.png', width=500)