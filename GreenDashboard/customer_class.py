import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as db_connect
import altair as alt


host_name = "dataviz.cgq2ewzuuqs1.us-east-2.rds.amazonaws.com"
db_user = "postgres"
db_password = "ElPeruano_2021"
db_name = "postgres"
db_port = 5432
connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name,port=db_port)

cursor = connection.cursor()

query = 'SELECT * FROM public.' + '"EO_Customer_Class" '

#query = ('Select ' +
#'TO_CHAR( ' + 
#    'TO_DATE (Extract(Month from public."EO_Residential_Avg_Bill"."Date")::text, '+ " 'MM' " +'),' + " 'Mon' " + 
#    ') AS "month_name", ' + 
#'Extract(Year from public."EO_Residential_Avg_Bill"."Date") as year_Num,' + 
#' "Average_kWH", "Fuel_Charge_cents_kWH", "Average_Bill" ' +
#' from public."EO_Residential_Avg_Bill"' + 
#' ORDER BY "month_name","year_num" ' )

cursor.execute(query)
data = cursor.fetchall()
connection.close()

df = pd.DataFrame(data)


df.rename(columns={0: 'Year',1:'Residential',2:'Commerical',3:'Industrial',4:'Other', 5:'Total'}, inplace=True)

convert_dict = {'Residential':int,
                'Commerical': int,
                'Industrial': int,
                'Other': int,
                'Total':int}
                
df=df.astype(convert_dict)

data_ = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019],
        'Residential':[345197,352574,363217,368700, 372329,376614,383257, 391410,401556,411366, 421752, 433411,443792],
        'Commerical': [41825,	42585,	43049,	43489,	43815,	44006,	44847,	45436,	46253,	47352,	48285,	48966,	49587],
        'Industrial':[75,	78,	81,	80,	81,	82,	138, 151,	127,	110,	104	,112,	114],
        'Other': [1523,	1553,	1579,	1601,	1640,	1668,	2340,	2406,	2507,	2515,	2560,	2715,	2765]
        

    }
df=pd.DataFrame(data_).set_index('Year')
df

st.bar_chart(df)


# FYI: YOU CANNOT SPLIT FY OUT OF THE YEAR BECAUSE THE FORMNAT IS NOT THE SAME ACROSS THE YEARS
# had to create it into a new dataframe ^ called data_
# df=df["Year"].str.split(" ", n=0, expand = True)
