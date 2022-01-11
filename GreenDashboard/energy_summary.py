import streamlit as st
import pandas as pd
import numpy as np

st.title('ENERGY SUMMARY ')

ES_pages = {
        "Overview":'energy_summary.py',
        "Customer Class": 'ES_Customer_Class.py',
        "Power Plants and Production cost":'ES_PowerPlants_Prod.py',
        "Renewable Resources and Power Supply": 'ES_Renewable_Res.py',
        "Residential Bill Average": 'ES_Res_avg_bill.py',
    }

ES_pages_list = list(ES_pages)
ES_option = st.sidebar.radio("Select the additional views for Energy summary:",ES_pages_list)
st.text(ES_option)

ES_fname_to_run = ES_pages[ES_option]
if ES_option != "Overview":
    with open(ES_fname_to_run, encoding="utf8") as f:
        ES_filebody = f.read()
        exec(ES_filebody,globals())

