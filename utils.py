from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd


def load_data(file_path):
    # Function to load data from a CSV file
    return pd.read_csv(file_path)

def save_data(df, file_path):
    # Function to save data to a CSV file
    df.to_csv(file_path, index=False, encoding='utf-8-sig')

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

    if changes['deleted_rows']:
        # delete all updated rows
        for index in changes['deleted_rows']:
            st.session_state.pack_list = st.session_state.pack_list.drop(index)
    

def on_data_edited(pack_list, file_path):
    update_dataframe(st.session_state.pack_list_changes)
    save_data(st.session_state.pack_list, file_path)
# Function to add an item to the data
def add_item(data, item, column_name):
    if item:  # Check if the input is not empty
        return pd.concat([data, pd.DataFrame({column_name: [item]})])
    return data

# Function to remove an item from the data
def remove_item(data, item, column_name):
    if item:
        return data[data[column_name] != item]
    return data

def setup_initial_session_state(forceClear=False):
    
    for key, value in INITIAL_SESSION_STATE.items():
        st.session_state[key] = value