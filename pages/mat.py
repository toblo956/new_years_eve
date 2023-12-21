import streamlit as st

from utils import setup_initial_session_state

setup_initial_session_state()
header = st.container()
header.title("Mat")

st.write("Frukost: Gröt med sylt")
st.write("Varmrätt: Köttbullar med potatismos och lingonsylt")
st.write("Efterrätt: Kladdkaka med grädde")