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
        st.error("Failed to save data to Google Sheets")

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
            if index in df.index:
                df = df.drop(index)

    return df

def on_data_edited(df_to_update, df_to_uptdate_str, sheets_connection):

    if df_to_uptdate_str == "pack_list":
        st.session_state.pack_list = update_dataframe(df_to_update, st.session_state.pack_list_changes)
        st.session_state['persisted_state']['pack_list'] = st.session_state.pack_list
        save_data(st.session_state.pack_list, sheets_connection, worksheet="pack_list")
    elif df_to_uptdate_str == "responsibilities":
        st.session_state.responsibilities = update_dataframe(df_to_update, st.session_state.responsibilities_changes)
        st.session_state['persisted_state']['responsibilities'] = st.session_state.responsibilities
        save_data(st.session_state.responsibilities, sheets_connection, worksheet="responsibilities")
    elif df_to_uptdate_str == "food_responsibilities":
        st.session_state.food_responsibilities = update_dataframe(df_to_update, st.session_state.food_responsibilities_changes)
        st.session_state['persisted_state']['food_responsibilities'] = st.session_state.food_responsibilities
        save_data(st.session_state.food_responsibilities, sheets_connection, worksheet="mat")
    elif df_to_uptdate_str == "cocktail_responsibilities":
        st.session_state.cocktail_responsibilities = update_dataframe(df_to_update, st.session_state.cocktail_responsibilities_changes)
        st.session_state['persisted_state']['cocktail_responsibilities'] = st.session_state.cocktail_responsibilities
        save_data(st.session_state.cocktail_responsibilities, sheets_connection, worksheet="cocktails")


#This could be used for widgets that are conditionally rendered or perhaps rendered outside of viewport (?)
#sessions state might not survive reruns thus need to be persisted and reread
def set_persisted_state_on_change(*args, **kwargs):
    key=kwargs.get('key')
    if key is not None and key in st.session_state:
        st.session_state['persisted_state'][key] = st.session_state[key]
    else: 
        st.warn('None or not initialized session_state key provided to set_persisted_state_on_change')

def setup_initial_session_state():

    if 'persisted_state' not in st.session_state:
        st.session_state['persisted_state'] = {}
    
    peristed_state = st.session_state.persisted_state
    for key in INITIAL_SESSION_STATE.keys():
        
        if key not in st.session_state:
            # if persisted - use it
            if key in peristed_state:
                st.session_state[key] = peristed_state[key]
            else:
                set_state_from_initial_value(key)

def set_state_from_initial_value(key):
    initial_value = INITIAL_SESSION_STATE.get(key)
    if isinstance(initial_value, pd.DataFrame) or isinstance(initial_value, pd.Series):
        initial_value = initial_value.copy()
    st.session_state[key] = initial_value

def setup_gsheets_connection(worksheet="pack_list"):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet=worksheet)

    # Remove empty columns and rows
    columns_to_drop = [col for col in df.columns if col == '' or pd.isna(col) or 'Unnamed' in col]
    df.drop(columns=columns_to_drop, inplace=True)
    df = df.dropna(axis=0, how='all')

    return df, conn
