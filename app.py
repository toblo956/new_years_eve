import streamlit as st
import pandas as pd
import altair as alt
from responsibilities import print_responsibilities
# Sample data: Replace this with your actual data
data = {
    "Person": ["Alice", "Bob", "Charlie", "Diana"],
    "Responsibility": ["Decorations", "Food", "Music", "Games"],
    "Completion": [50, 80, 30, 90]  # This can represent percentage completion
}

df = pd.DataFrame(data)

# Streamlit app layout
st.write("## Välkommen till Orsa! ")
st.image('images/moreus.jpeg', width=500)

# Display the DataFrame
st.write("## Ansvarsområden ")
print_responsibilities()

st.write("## Den spontanta delen")