from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

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
    

def on_data_edited(df_to_update, sheets_connection):
    if df_to_update == "pack_list":
        update_dataframe(st.session_state.pack_list_changes)
        save_data(st.session_state.pack_list, sheets_connection)
    elif df_to_update == "responsibilities":
        update_dataframe(st.session_state.responsibilities_changes)
        save_data(st.session_state.responsibilities_changes, sheets_connection)


def setup_initial_session_state(forceClear=False):
    
    for key, value in INITIAL_SESSION_STATE.items():
        st.session_state[key] = value

def setup_gsheets_connection(worksheet="pack_list"):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=1)
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, how='all')
    st.write("Df" , df)

    return df, conn
