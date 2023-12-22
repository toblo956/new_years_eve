import pandas as pd
import streamlit as st
from utils import setup_initial_session_state

setup_initial_session_state()

header = st.container()
header.title("Välkommen till Orsa! ")

first_column, second_column = st.columns([8,2])
first_column.image('images/moreus.jpeg', use_column_width=True)
second_column.image('images/ful_bild.png', use_column_width=True)

text = f"""
Orsas djupa historiska rötter, som sträcker sig från urgamla tider genom vikingaepoken till den moderna eran, utgör en fascinerande bakgrund som sammanför fem stockholmare över nyår. Denna pittoreska ort erbjuder en resa genom tiden och en chans för dessa individer att fördjupa sina kunskaper om Sveriges kulturarv. Genom att delta i det lokala nyårsfirandet finner de en gemensam grund i firandet av landets rika historia och kultur. Denna unika upplevelse i Orsa skapar inte bara oförglömliga minnen, utan också en starkare känsla av nationell tillhörighet och samhörighet, vilket är särskilt betydelsefullt vid övergången till det nya året. """

st.write(text)

st.write("### Årets lineup: (bästa lineupen någonsin)")

a,b,c,d,e = st.columns(5)

with a:
    a.caption("Arvid")
    a.image('images/arvid.jpeg', use_column_width=True)

with b:
    b.caption("Ellen")
    b.image('images/ellen.jpeg', use_column_width=True)

with c:
    c.caption("Tobias")
    c.image('images/tobias.jpeg', use_column_width=True)

with d:
    d.caption("Pernilla")
    d.image('images/pernilla.jpeg', use_column_width=True)

with e:
    e.caption("Felix")
    e.image('images/felix.jpeg', use_column_width=True)

