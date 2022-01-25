import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import plotly.graph_objects as go
import plotly.express as px
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


dir_test = os.getcwd()
dir_sys = (dir_test + '/Resources/Animations/')
sys.path.insert(0, dir_sys)
import Animations

dir_test = os.getcwd()
dir_sys = (dir_test + '/Functions/')
sys.path.insert(0, dir_sys)
import GT_Functions as gt_func

query = ""

st.title("Green Development in Austin")

st.subheader("The comparison in green energy use between multifamily, single family, and commercial structures")

st.write("info info info")

line_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['single family', 'multifamily', 'commercial'])
st.line_chart(line_data)

with st.expander("Single Family"):
    st.write("""
         This section display the data for the Single Family green building development.
     """)
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year",' +                         'public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Elecitrc_Savings_MWH"' +
            'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Single Family'")
    
    
    df = gt_func.Execute_query(query)
    
    lottie_img_SF = gt_func.load_lottieurl(Animations.GD_SF)
    col1,col2 = st.columns(2)
    with col1:
        st_lottie(lottie_img_SF, key="img1")
    with col2:
        st.dataframe(df)

with st.expander("Multi Family"):
    st.write("""
         This section display the data for the Multi Family green building development.
     """)
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year",' +                         'public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Energy_Savings_MBTU",'+                     'public."G_Building_Project_Agg"."Elecitrc_Savings_MWH", public."G_Building_Project_Agg"."Gas_Saving"' +
            'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Multifamily'")
    
    df = gt_func.Execute_query(query)
    
    df.rename(columns={0: 'Category',1:'Fiscal Year',2:'Project Square Footage',3:'Energy Savings',4:'Electric Savings',5:'Gas Savings'}, inplace=True)
    lottie_img_MF = gt_func.load_lottieurl(Animations.GD_MF)
    col3,col4 = st.columns(2)
    with col3:
        st_lottie(lottie_img_MF, key="img2")
    with col4:
        st.dataframe(df)
    
    
with st.expander("Commercial"):
    st.write("""
         This section display the data for the Commercial green building development.
     """)
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year",'+                         'public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Energy_Savings_MBTU",'+                     'public."G_Building_Project_Agg"."Elecitrc_Savings_MWH", public."G_Building_Project_Agg"."Gas_Saving"' +
            'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Commercial'")
    
    df = gt_func.Execute_query(query)
    
    df.rename(columns={0: 'Category',1:'Fiscal Year',2:'Project Square Footage',3:'Energy Savings',4:'Electric Savings',5:'Gas Savings'}, inplace=True)

    lottie_img_CO = gt_func.load_lottieurl(Animations.GD_CO)
    col5,col6 = st.columns(2)
    with col5:
        st_lottie(lottie_img_CO, key="img3")
    with col6:
        st.dataframe(df)
    

    