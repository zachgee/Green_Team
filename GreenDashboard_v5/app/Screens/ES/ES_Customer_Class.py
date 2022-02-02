import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as db_connect
import os
import sys

dir_sys = os.path.join(os.getcwd(), "app", "Resources","Animations")
sys.path.insert(0, dir_sys)
import Animations

dir_sys = os.path.join(os.getcwd(), "app", "Resources","Functions")
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func

query = 'SELECT * FROM public.' + '"EO_Customer_Class" '
df_raw = gt_func.Execute_query(query)

df_raw.rename(columns={0: 'Year',1:'Residential',2:'Commerical',3:'Industrial',4:'Other', 5:'Total'}, inplace=True)

st.title("Customer Class data")
st.header(" Austin Energy has four main customer classes: residential, commercial, industrial and other. The next views will show how the number of each of these groups increased since 2007.")

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.info('Residential Customers')
    st.write(
        """    Live in single-family dwellings, mobile homes, townhouses, or individually metered apartment units. """)
    
with col2:
    st.info('Commercial Customers')
    st.write(
        """    Small to large businesses that fall under Austin Energy’s secondary level of service. This means Austin Energy owns, operates, and maintains the equipment (wires, transformers, etc.) supplying power to those facilities". """)

with col3:
    st.info('Industrial')
    st.write(
        """   (Primary) customers take service at high voltage (12,500 volts or higher) and own, operate and maintain their own equipment. Consequently, Austin Energy experiences lower overall system losses and it costs less to serve these customers. """)

with col4:
    st.info('Other')
    st.write(
        """   The final class, other, typically refers to street lighting and facilities such as ballparks. """)

st.table(df_raw)


df_raw = df_raw.set_index('Year')
st.bar_chart(df_raw)


