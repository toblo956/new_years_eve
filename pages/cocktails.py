import streamlit as st

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state


def cocktail_responsibilities():
    st.session_state.cocktail_responsibilities, conn = setup_gsheets_connection("cocktails")
    st.session_state.cocktail_responsibilities["Cocktail"] = st.session_state.cocktail_responsibilities["Cocktail"].astype(str)
    column_config={"Cocktail": st.column_config.TextColumn(width="medium") }
    st.data_editor(st.session_state.cocktail_responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=("cocktail_responsibilities", conn),
                                                key="cocktail_responsibilities_changes",
                                                column_config=column_config,
                                                num_rows="dynamic"
                                                )
    
setup_initial_session_state()
header = st.container()
header.title("Cocktails (ändra o lägg till)")
st.image('images/cocktail.png', width=500)
cocktail_responsibilities()