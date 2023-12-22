import streamlit as st

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state


def cocktail_responsibilities():

    cocktail_responsibilities, conn = setup_gsheets_connection("cocktails")
    if "persisted_state" in st.session_state and "cocktail_responsibilities" in st.session_state.persisted_state:
        cocktail_responsibilities = st.session_state.persisted_state["cocktail_responsibilities"]
    
    st.data_editor(cocktail_responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=(cocktail_responsibilities, "cocktail_responsibilities", conn),
                                                key="cocktail_responsibilities_changes",
                                                num_rows="dynamic"
                                                )
    
setup_initial_session_state()
header = st.container()
header.title("Cocktails (ändra o lägg till)")
st.image('images/cocktail.png', use_column_width=True)
cocktail_responsibilities()