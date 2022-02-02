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

###################################
#Database connection 
vSQL = 'Select * from public."EO_PowerSupply_Cost"'
df = gt_func.Execute_query(vSQL)
df.rename(columns={0: 'Fuel Type',1:'Fiscal Year',2:'Fuel Cost',3:'Fuel Cost Percentage'}, inplace=True)
vSQL1='Select * from public."EO_Power_Plants"'
df1 = gt_func.Execute_query(vSQL1)
df1.rename(columns={0: 'PowerPlant',1:'Unit',2:'Fuel',3:'Summer Rated Capacity(MW)',4:'Year Installed'}, inplace=True)


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
        


if pattern == 'Power Plants':
        st.dataframe(df1)