import streamlit as st

st.title('Hello, this is demo ENERGY Dashboard - Green team ')

col1, col2 = st.beta_columns((1,1))
name = col1.text_input("What's your name?")

if name:
    st.header("Good morning " + name + " - " + "Buenos dias " + name + " - " + "Bon dia " + name)