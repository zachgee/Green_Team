import streamlit as st
import pandas as pd
import numpy as np

st.title('Green Commercial Buidling projects')

data_address = 'C:\\Users\joelf\Documents\Bootcamp\Data_Analytics\Project\Green_Team\StreamlitDemo\Resources/test.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(data_address, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(4)

st.write(data)