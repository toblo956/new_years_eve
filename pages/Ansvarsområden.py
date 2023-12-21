
# Initial data setup
import pandas as pd
import streamlit as st

from utils import setup_initial_session_state


people = ["Arvid", "Ellen", "Löfven", "Pernilla", "Felix"]
columns = ["Att köpa", "Att ta med", "Ansvar", "Att planera"]

def print_responsibilities():
    df = pd.DataFrame(index=people, columns=columns)
    st.data_editor(df)


setup_initial_session_state()
header = st.container()
header.title("Ansvarsområden")
print_responsibilities()