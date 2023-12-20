import streamlit as st
import pandas as pd
import altair as alt
from utils import packlista, print_responsibilities, packlista


# Streamlit app layout
st.write("## Välkommen till Orsa! ")
first_column, second_column = st.columns(2)
first_column.image('images/moreus.jpeg', use_column_width=True)
second_column.image('images/ful_bild.png', width=300)

# Display the DataFrame
st.write("## Ansvarsområden ")
print_responsibilities()

st.write("## Packlista ")
packlista()