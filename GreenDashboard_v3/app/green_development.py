import streamlit as st
import pandas as pd
import numpy as np
import os

dir_test = os.getcwd() + '\\app'

#st.title('ENERGY GREEN DEVELOPMENT')
st.markdown("<h1 style='text-align: center; color: green; font-size: 100px'>ENERGY GREEN DEVELOPMENT</h1>", unsafe_allow_html=True)

pages = {
        "Overview":dir_test + '\Screens\GD/GD_Home.py',
        "Green Buildings": dir_test + '\Screens\GD/GD_Green_Buildings.py',
        "Electrical Vehicles charging stations": dir_test + '\Screens\GD/GD_Electric_Vehicles_Stations.py',
        "Emmisions": dir_test + '\Screens\GD/GD_Emmisions.py'
    }

pages_list = list(pages)
option = st.sidebar.radio("Select the additional views for Green Development:",pages_list)
#st.text(option)

fname_to_run = pages[option]
#if option != "Overview":
with open(fname_to_run, encoding="utf8") as f:
    filebody = f.read()
    exec(filebody,globals())