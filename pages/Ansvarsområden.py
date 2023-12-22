
# Initial data setup
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from utils import on_data_edited, setup_gsheets_connection, setup_initial_session_state




def print_responsibilities():

    responsibilities, conn = setup_gsheets_connection("responsibilities")
    if "persisted_state" in st.session_state and "responsibilities" in st.session_state.persisted_state:
        responsibilities = st.session_state.persisted_state["responsibilities"]
    responsibilities["Person"] = pd.DataFrame(
        {
            "Person": [
                "https://storage.cloud.google.com/streamlit_images/arvid.jpeg",
                "https://storage.cloud.google.com/streamlit_images/ellen.jpeg",
                "https://storage.cloud.google.com/streamlit_images/tobias.jpeg",
                "https://storage.cloud.google.com/streamlit_images/pernilla.jpeg",
                "https://storage.cloud.google.com/streamlit_images/felix.jpeg",
                "https://storage.cloud.google.com/streamlit_images/alla.png",
            ],
        }
    )


    column_config={"Person": st.column_config.ImageColumn(width="medium") }


    st.data_editor(responsibilities.reset_index(drop=True), 
                                                use_container_width=True,
                                                on_change=on_data_edited,
                                                args=(responsibilities, "responsibilities", conn),
                                                key="responsibilities_changes",
                                                column_config=column_config,
                                                hide_index=True,)


setup_initial_session_state()
header = st.container()
header.title("Ansvarsområden")
print_responsibilities()