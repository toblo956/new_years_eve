
# Initial data setup
import pandas as pd
import streamlit as st

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state




def print_responsibilities():
    # Load the initial pack list
    st.session_state.responsibilities, conn = setup_gsheets_connection("responsibilities")


    # Display the current pack list in a data editor
    st.data_editor(st.session_state.responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=("responsibilities", conn),
                                                key="responsibilities_changes",
                                                num_rows="dynamic",)


setup_initial_session_state()
header = st.container()
header.title("Ansvarsområden")
print_responsibilities()