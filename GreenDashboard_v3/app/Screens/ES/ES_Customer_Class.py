import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as db_connect
import os
import sys

dir_test = os.getcwd() + '\\app'
dir_sys = (dir_test + '/Resources/Animations/')
sys.path.insert(0, dir_sys)
import Animations

dir_test = os.getcwd() + '\\app'
dir_sys = (dir_test + '/Functions/')
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func

query = 'SELECT * FROM public.' + '"EO_Customer_Class" '
df_raw = gt_func.Execute_query(query)


st.write(query)

df_raw.rename(columns={0: 'Year',1:'Residential',2:'Commerical',3:'Industrial',4:'Other', 5:'Total'}, inplace=True)

st.title("Customer Class data")

st.table(df_raw)

#convert_dict = {'Residential':int,
#                'Commerical': int,
#                'Industrial': int,
#                'Other': int,
#                'Total':int}

#df_raw=df_raw.astype(convert_dict)


data_ = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019],
        'Residential':[345197,352574,363217,368700, 372329,376614,383257, 391410,401556,411366, 421752, 433411,443792],
        'Commerical': [41825,	42585,	43049,	43489,	43815,	44006,	44847,	45436,	46253,	47352,	48285,	48966,	49587],
        'Industrial':[75,	78,	81,	80,	81,	82,	138, 151,	127,	110,	104	,112,	114],
        'Other': [1523,	1553,	1579,	1601,	1640,	1668,	2340,	2406,	2507,	2515,	2560,	2715,	2765]


    }




df=pd.DataFrame(data_).set_index('Year')

st.bar_chart(df)


