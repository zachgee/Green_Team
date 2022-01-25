import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

dir_test = os.getcwd()
dir_sys = (dir_test + '/Resources/Animations/')
sys.path.insert(0, dir_sys)
import Animations

dir_test = os.getcwd()
dir_sys = (dir_test + '/Functions/')
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func

##query = 'SELECT * FROM public.' + '"EO_Customer_Class" '
query = ('Select ' +
'TO_CHAR( ' + 
    'TO_DATE (Extract(Month from public."EO_Residential_Avg_Bill"."Date")::text, '+ " 'MM' " +'),' + " 'Mon' " + 
    ') AS "month_name", ' + 
'Extract(Year from public."EO_Residential_Avg_Bill"."Date") as year_Num,' + 
' "Average_kWH", "Fuel_Charge_cents_kWH", "Average_Bill" ' +
' from public."EO_Residential_Avg_Bill"' + 
' ORDER BY "month_name","year_num" ' )

df = gt_func.Execute_query(query)

df.rename(columns={0: 'Month',1:'Year',2:'Average_kWH',3:'Fuel_Charge_Cents_kWH',4:'Average Bill'}, inplace=True)

convert_dict = {'Year': int}

df=df.astype(convert_dict)

st.title("Residential Averga Bill - data")

st.dataframe(df)