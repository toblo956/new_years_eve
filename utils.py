from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd


def load_data(file_path):
    # Function to load data from a CSV file
    return pd.read_csv(file_path)

def save_data(df, file_path):
    # Function to save data to a CSV file
    st.write("Saving data...")
    st.write(df)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')


def on_data_edited(pack_list, file_path):
    st.write("Data edited!")
    st.write(st.session_state.pack_list)
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