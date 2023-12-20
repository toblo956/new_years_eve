import pandas as pd
import streamlit as st
from utils import add_item, load_data, on_data_edited, remove_item, save_data


def packlista():
    # Load the initial pack list
    file_path = 'data/pack_list.csv'
    pack_list = load_data(file_path=file_path)

    # Display the current pack list in a data editor
    st.session_state.pack_list = st.data_editor(pack_list.reset_index(drop=True), use_container_width=True, on_change=on_data_edited, args=(pack_list, file_path))

    text_placeholder, _ = st.columns([10, 2])
    new_item = text_placeholder.text_input("Lägg till nytt föremål")

    add, remove = st.columns(2)
    with add:
        if st.button(f"Lägg till {new_item} i listan"):
            updated_pack_list = add_item(pack_list, new_item, "Grejer")
            save_data(updated_pack_list, 'data/pack_list.csv')
            st.experimental_rerun()
    with remove:
        if st.button(f"Ta bort {new_item} från listan"):
            updated_pack_list = remove_item(pack_list, new_item, "Grejer")
            save_data(updated_pack_list, 'data/pack_list.csv')
            st.experimental_rerun()
    


header = st.container()
header.title("Packlista (fyll på)" )
packlista()