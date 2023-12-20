import streamlit as st
import pandas as pd

# Initial data setup
people = ["Arvid", "Ellen", "Löfven", "Pernilla", "Felix"]
columns = ["Att köpa", "Att ta med", "Ansvar", "Att planera"]

def print_responsibilities():
        
    # Create an empty DataFrame
    df = pd.DataFrame(index=people, columns=columns)

    # Streamlit app layout
    st.write (" #### New Year's Eve Responsibilities")

    st.data_editor(df)


"""
st.session_state.persistent_df = ...  # contains the actual data so that it is not lost when the data_editor is edited.
df = st.session_state.persistent_df  # or subset of
edited_df = st.data_editor(df)  # try column_order= to hide additional columns, see: https://docs.streamlit.io/library/api-reference/data/st.data_editor
merge_df(st.session_state.persistent_df, edited_df)

def merge_df(st.session_state.persistent_df, edited_df):
    # merge the two dataframes
    st.experimental_rerun
"""