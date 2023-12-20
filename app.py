import streamlit as st
from utils import setup_initial_session_state

setup_initial_session_state()

# Streamlit app layout
header = st.container()
header.title("Välkommen till Orsa! ")

first_column, second_column = st.columns(2)
first_column.image('images/moreus.jpeg', use_column_width=True)
second_column.image('images/ful_bild.png', width=300)
