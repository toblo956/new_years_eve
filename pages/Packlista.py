import pandas as pd
import streamlit as st
from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state



def packlista():
    # Load the initial pack list
    
    st.session_state.pack_list, conn = setup_gsheets_connection("pack_list")
    st.session_state.pack_list = st.session_state.pack_list.dropna(axis=1, how='all')
    st.session_state.pack_list = st.session_state.pack_list.dropna(axis=0, how='all')
    
    pack_list = st.session_state.pack_list

    # Display the current pack list in a data editor
    st.data_editor(pack_list.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=("pack_list", conn),
                                                key="pack_list_changes",
                                                num_rows="dynamic")

setup_initial_session_state()
header = st.container()
header.title("Packlista (fyll på)" )
packlista()