import pandas as pd
import streamlit as st

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state


def food_responsibilities():
    food_responsibilities, conn = setup_gsheets_connection("mat")
    if "persisted_state" in st.session_state and "food_responsibilities" in st.session_state.persisted_state:
        food_responsibilities = st.session_state.persisted_state["food_responsibilities"]

    st.data_editor(food_responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=("food_responsibilities", conn),
                                                key="food_responsibilities_changes",
                                                num_rows="dynamic"
                                                )


setup_initial_session_state()
header = st.container()
header.title("Mat (ändra o lägg till)")

st.image('images/mat.png', width=300)
food_responsibilities()