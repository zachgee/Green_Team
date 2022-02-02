import streamlit as st
import pandas as pd
import numpy as np
import psycopg2, psycopg2.extras

st.title('Renewable Resources')

st.subheader('Dataset sample')

DB_HOST = 'dataviz.cgq2ewzuuqs1.us-east-2.rds.amazonaws.com'
DB_USER = 'postgres'
DB_PASS = 'ElPeruano_2021'
DB_NAME = 'postgres'
DB_PORT = 5432
connection = psycopg2.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME, port=DB_PORT)

cursor =  connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

vSQL = 'Select * from public."EO_Fuel_Cost_AVG"'

cursor.execute(vSQL)
result = cursor.fetchall()

df = pd.DataFrame(result)
df.rename(columns={0: 'Fiscal Year',1:'System annual average fuel cost (cents/kWh)'}, inplace=True)

query = vSQL

cursor.execute(query)
result = cursor.fetchall()
st.dataframe(df)