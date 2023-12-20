from constants import INITIAL_SESSION_STATE
import streamlit as st
import pandas as pd


def load_data(file_path):
    # Function to load data from a CSV file
    return pd.read_csv(file_path)

def save_data(df, file_path):
    # Function to save data to a CSV file
    df.to_csv(file_path, index=False, encoding='utf-8-sig')


def packlista():
    # Load the initial pack list
    pack_list = load_data('data/pack_list.csv')

    # Display the current pack list in a data editor
    st.data_editor(pack_list.reset_index(drop=True), width=300)

    text_placeholder, _ = st.columns([10, 2])
    new_item = text_placeholder.text_input("Lägg till nytt föremål")

    add, remove = st.columns(2)
    with add:
        if st.button(f"Lägg till {new_item} i listan"):
            if new_item:  # Check if the input is not empty
                # Append the new item to the pack list and update the session state
                updated_pack_list = pd.concat([pack_list, pd.DataFrame({"Grejer": [new_item]})])
                st.session_state.packlist = updated_pack_list

                # Save the updated pack list to CSV
                save_data(updated_pack_list, 'data/pack_list.csv')
                #st.experimental_rerun()
    with remove:
        if st.button(f"Ta bort {new_item} från listan"):
            if new_item:
                # Remove the item from the pack list and update the session state
                updated_pack_list = pack_list[pack_list["Grejer"] != new_item]
                st.session_state.packlist = updated_pack_list

                # Save the updated pack list to CSV
                save_data(updated_pack_list, 'data/pack_list.csv')
                #st.experimental_rerun()



def setup_initial_session_state(forceClear=False):
    
    for key, value in INITIAL_SESSION_STATE.items():
        st.session_state[key] = value