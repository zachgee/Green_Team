import streamlit as st
import pandas as pd
import numpy as np
import psycopg2, psycopg2.extras


st.title('Power Plants and Production Cost')

st.subheader('Dataset sample')


df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['x','y'])
st.line_chart(df)


DB_HOST = 'dataviz.cgq2ewzuuqs1.us-east-2.rds.amazonaws.com'
DB_USER = 'postgres'
DB_PASS = 'ElPeruano_2021'
DB_NAME = 'postgres'
DB_PORT = 5432
connection = psycopg2.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME, port=DB_PORT)

cursor =  connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

query = ('SELECT public."EO_PowerSupply_Cost"."Fuel_Type", public."EO_PowerSupply_Cost"."Fiscal_Year", public."EO_PowerSupply_Cost"."Fuel_Cost", public."EO_PowerSupply_Cost"."Fuel_Cost_Per"' +
        'FROM public."EO_PowerSupply_Cost"')

cursor.execute(query)
result = cursor.fetchall()
connection.close()
df = pd.DataFrame(result) 
st.dataframe(df )




