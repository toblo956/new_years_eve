from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def load_data(file_path):
    # Function to load data from a CSV file
    return pd.read_csv(file_path)

def save_data(df, sheets_connection, worksheet="pack_list"):

    try:
        sheets_connection.update(data=df, worksheet=worksheet)
    except:
        st.write("Failed to save data to Google Sheets")

def update_dataframe(df, changes):

    # Update edited rows
    for index, edits in changes['edited_rows'].items():
        for col, val in edits.items():
            df.at[index, col] = val

    # Append new rows
    if changes['added_rows']:
        if changes['added_rows'][-1] == {}:
            pass
        else:
            df = pd.concat([df, pd.DataFrame(changes['added_rows'])])

    # Delete rows
    if changes['deleted_rows']:
        # delete all updated rows
        for index in changes['deleted_rows']:
            df.drop(index, inplace=True)

    return df

def on_data_edited(df_to_update, sheets_connection):

    if df_to_update == "pack_list":
        st.session_state.pack_list = update_dataframe(st.session_state.pack_list, st.session_state.pack_list_changes)
        save_data(st.session_state.pack_list, sheets_connection, worksheet="pack_list")
    elif df_to_update == "responsibilities":
        st.session_state.responsibilities = update_dataframe(st.session_state.responsibilities, st.session_state.responsibilities_changes)
        save_data(st.session_state.responsibilities, sheets_connection, worksheet="responsibilities")
    elif df_to_update == "food_responsibilities":
        st.session_state.food_responsibilities = update_dataframe(st.session_state.food_responsibilities, st.session_state.food_responsibilities_changes)
        save_data(st.session_state.food_responsibilities, sheets_connection, worksheet="mat")
    elif df_to_update == "cocktail_responsibilities":
        st.session_state.cocktail_responsibilities = update_dataframe(st.session_state.cocktail_responsibilities, st.session_state.cocktail_responsibilities_changes)
        save_data(st.session_state.cocktail_responsibilities, sheets_connection, worksheet="cocktails")


def setup_initial_session_state(forceClear=False):
    
    for key, value in INITIAL_SESSION_STATE.items():
        st.session_state[key] = value

def setup_gsheets_connection(worksheet="pack_list"):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)

    # Remove empty columns and rows
    columns_to_drop = [col for col in df.columns if col == '' or pd.isna(col) or 'Unnamed' in col]
    df.drop(columns=columns_to_drop, inplace=True)
    df = df.dropna(axis=0, how='all')

    return df, conn
