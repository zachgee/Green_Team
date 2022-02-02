import streamlit as st
import pandas as pd
import numpy as np
import psycopg2, psycopg2.extras
import sys 
import os

dir_sys = os.path.join(os.getcwd(), "app", "Resources","Animations")
sys.path.insert(0, dir_sys)
import Animations

dir_sys = os.path.join(os.getcwd(), "app", "Resources","Functions")
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func


vSQL = 'Select * from public."EO_Fuel_Cost_AVG"'
df = gt_func.Execute_query(vSQL)
df.rename(columns={0: 'Fiscal Year',1:'System annual average fuel cost (cents/kWh)'}, inplace=True)

st.title('Renewable Resources')

st.subheader('Dataset sample')

st.dataframe(df)