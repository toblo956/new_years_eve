from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd


def load_data(file_path):
    # Function to load data from a CSV file
    return pd.read_csv(file_path)

def save_data(df, sheets_connection):
    # Function to save data to a CSV file
    sheets_connection.update(data=df, worksheet='pack_list')

def update_dataframe(changes):
    # Update edited rows
    for index, edits in changes['edited_rows'].items():
        for col, val in edits.items():
            st.session_state.pack_list.at[index, col] = val

    # Append new rows
    if changes['added_rows']:
        if changes['added_rows'][-1] == {}:
            pass
        else:
            st.session_state.pack_list = pd.concat([st.session_state.pack_list, pd.DataFrame(changes['added_rows'])])

    # Delete rows
    if changes['deleted_rows']:
        # delete all updated rows
        for index in changes['deleted_rows']:
            st.session_state.pack_list = st.session_state.pack_list.drop(index)
    

def on_data_edited(pack_list, sheets_connection):
    update_dataframe(st.session_state.pack_list_changes)
    save_data(st.session_state.pack_list, sheets_connection)


def setup_initial_session_state(forceClear=False):
    
    for key, value in INITIAL_SESSION_STATE.items():
        st.session_state[key] = value