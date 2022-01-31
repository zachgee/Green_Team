import pandas as pd
import numpy as np
import os
import sys
import streamlit as st
import time
import requests
import requests
import psycopg2, psycopg2.extras

dir_test = os.getcwd() + '\\app'
dir_sys = (dir_test + '/docs/')
sys.path.insert(0, dir_sys)
import config

@st.cache
########################################################################
#Function: This function verify the animation exsit and still available.

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

########################################################################
#Function: This function perfomr scrapping instruction to bring data from ERCOT
#return a dictionary with multiple values

def scrapping_ERCOT():

    # Parse the HTML
    vStatus = "good"

    #Numeric values
    vReserve = "ok"
    
    #status    
    vCurrentDemand = 40
    vCommitCapacity = 50
    
    #description
    vLastUpdate = '01/30/2021 19:34:00'
    vCurrentDesc = 'Current capacity ok'
    vCommitCapacityDesc = 'Capacity according to limit is ok'
    
    #RETURN
    return {'status':vStatus,
            'reserve':vReserve,
            'current':vCurrentDemand,
            'capacity':vCommitCapacity,
            'updated':vLastUpdate,
            'current_desc':vCurrentDesc,
            'commit_desc':vCommitCapacityDesc}

################################################################################
#Function: This function stablish a database connection and execute a query.
#return a dataframe
def Execute_query(vQuery):
    connection = psycopg2.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS,                                        database=config.DB_NAME)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(vQuery)
    result = cursor.fetchall()  
    df = pd.DataFrame(result)
    connection.close()
    return df

################################################################################
#Functions : Reload the widget selection and calls other function (Execute query)
def Reload_Widgets(vYear,vFilter):
    
    if vFilter == 'Producer Type':
        vSQL = ('Select public."G_Emmision_US"."Producer_Type", public."G_Emmision_US"."CO2_Tons" as CO2,' +
                'public."G_Emmision_US"."SO2_Tons" as SO, public."G_Emmision_US"."NOx_Tons" as NOx from public."G_Emmision_US" WHERE ' + 
                ' public."G_Emmision_US"."Year" = ' + str(vYear) + ' and public."G_Emmision_US"."State" = ' + "'TX' AND " +
                ' public."G_Emmision_US"."Producer_Type" <> ' + "'Total Electric Power Industry' and " + 
                ' public."G_Emmision_US"."Energy_Source" = ' + " 'All Sources' order by " +
                ' public."G_Emmision_US"."Year",public."G_Emmision_US"."Producer_Type" ASC')
    else:
        #Energy Source
        vSQL = ('Select public."G_Emmision_US"."Energy_Source", public."G_Emmision_US"."CO2_Tons" as CO2,' +
                ' public."G_Emmision_US"."SO2_Tons" as SO, public."G_Emmision_US"."NOx_Tons" as NOx from public."G_Emmision_US" WHERE ' + 
                ' public."G_Emmision_US"."Year" = ' + str(vYear) + ' and public."G_Emmision_US"."State" = '+ "'TX' AND " +
                ' public."G_Emmision_US"."Producer_Type" = ' + " 'Total Electric Power Industry'and " + 
                ' public."G_Emmision_US"."Energy_Source" <> ' + "'All Sources' order by " +
                ' public."G_Emmision_US"."Year",public."G_Emmision_US"."Energy_Source" ASC ')
    
    df_raw = Execute_query(vSQL)
    
    if vFilter == 'Producer Type':
        df_raw.rename(columns={0: 'Producer Type',1:'CO2',2:'SO2',3:'NOX'}, inplace=True)
    else:
        df_raw.rename(columns={0: 'Energy Source',1:'CO2',2:'SO2',3:'NOX'}, inplace=True)
    
    return df_raw


################################################################################
#Functions : Reload the map widget based on previous selection
def Reload_Map(df,city_selected,zip_selected,category_selected):
    if city_selected == 'ALL':
        df = df[df['City'].notnull()]
    else:
        df = df[df['City']==city_selected]
        
    if zip_selected == 'ALL':
        df = df[df['Zip_Code'].notnull()]
    else:
        df.query('Zip_Code in @zip_selected')
        #df = df[df['Zip Code'].isin(zip_selected)]
    
    if category_selected == 'ALL':
         df = df[df['Category'].notnull()]
    else:
        df = df[df['Category']==category_selected]

    return df