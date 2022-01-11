import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as db_connect

st.title("US Emmission analysis")

host_name="dataviz.cgq2ewzuuqs1.us-east-2.rds.amazonaws.com"
db_user="postgres"
db_password="ElPeruano_2021"
db_name="postgres"
db_port = 5432
connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name, port=db_port)
 
cursor = connection.cursor()

query = 'SELECT * FROM public."' + 'G_Emmision_US" where public."G_Emmision_US"."State" =' +  "'TX'"
cursor.execute(query)
data = cursor.fetchall()
connection.close()
df = pd.DataFrame(data)

st.dataframe(df )

st.table(df )