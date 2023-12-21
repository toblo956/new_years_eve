import pandas as pd
import streamlit as st
from utils import add_item, load_data, on_data_edited, setup_initial_session_state
from streamlit_gsheets import GSheetsConnection


def packlista():
    # Load the initial pack list
    conn = st.connection("gsheets", type=GSheetsConnection)
    st.session_state.pack_list = conn.read()
    st.session_state.pack_list = st.session_state.pack_list.dropna(axis=1, how='all')
    st.session_state.pack_list = st.session_state.pack_list.dropna(axis=0, how='all')
    
    pack_list = st.session_state.pack_list

    # Display the current pack list in a data editor
    st.data_editor(pack_list.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=(pack_list, conn),
                                                key="pack_list_changes",
                                                num_rows="dynamic")

setup_initial_session_state()
header = st.container()
header.title("Packlista (fyll på)" )
packlista()