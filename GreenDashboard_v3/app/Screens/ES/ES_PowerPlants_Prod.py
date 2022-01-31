import streamlit as st
import pandas as pd
import numpy as np
import psycopg2, psycopg2.extras
import sys 
import os

dir_test = os.getcwd() + '\\app'
dir_sys = (dir_test + '/Resources/Animations/')
sys.path.insert(0, dir_sys)
import Animations

dir_sys = (dir_test + '/Functions/')
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func

###################################
#Database connection 
query = ('SELECT public."EO_PowerSupply_Cost"."Fuel_Type", public."EO_PowerSupply_Cost"."Fiscal_Year", public."EO_PowerSupply_Cost"."Fuel_Cost", public."EO_PowerSupply_Cost"."Fuel_Cost_Per"' +
        'FROM public."EO_PowerSupply_Cost"')
df = gt_func.Execute_query(query)
df.rename(columns={0: 'Fuel Type',1:'Fiscal Year',2:'Fuel Cost',3:'Fuel Cost Percentage'}, inplace=True)

####################################
#Streamlit screen layout


st.title('Power Plants and Production Cost')

st.subheader('Dataset sample')


option = st.sidebar.selectbox("Which Dashboard?", ('Power Supply Cost', 'Power Plants',), )

pattern = st.selectbox(
        "Which Option?",
        ("Power Supply Cost", "Power Plants"))

if pattern == 'Power Supply Cost':
        st.dataframe(df)