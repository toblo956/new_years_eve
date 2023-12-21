
# Initial data setup
import pandas as pd
import streamlit as st

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state




def print_responsibilities():
    # Load the initial pack list
    st.session_state.responsibilities, conn = setup_gsheets_connection("responsibilities")
    st.image("images/arvid.jpeg", width=300)
    st.image("static/arvid.jpeg", width=300)
    
    st.session_state.responsibilities["Person"] = pd.DataFrame(
        {
            "Person": [
                "app/static/arvid.jpeg",
                "app/static/ellen.jpeg",
                "app/static/tobias.jpeg",
                "app/static/pernilla.jpeg",
                "app/static/felix.jpeg",
                "app/static/alla.png",
            ],
        }
    )

    column_config={"Person": st.column_config.ImageColumn() }

    # Display the current pack list in a data editor
    st.data_editor(st.session_state.responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=("responsibilities", conn),
                                                key="responsibilities_changes",
                                                column_config=column_config,
                                                hide_index=True)


setup_initial_session_state()
header = st.container()
header.title("Ansvarsområden")
print_responsibilities()