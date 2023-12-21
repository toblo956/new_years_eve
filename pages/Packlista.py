import pandas as pd
import streamlit as st
from utils import add_item, load_data, on_data_edited, remove_item, save_data, setup_initial_session_state


def packlista():
    # Load the initial pack list
    file_path = 'data/pack_list.csv'
    st.session_state.pack_list = load_data(file_path=file_path)
    pack_list = st.session_state.pack_list

    # Display the current pack list in a data editor
    st.data_editor(pack_list.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=(pack_list, file_path),
                                                key="pack_list_changes",
                                                num_rows="dynamic")

    

setup_initial_session_state()
header = st.container()
header.title("Packlista (fyll på)" )
packlista()