import pandas as pd
import numpy as np
import os
import sys
import streamlit as st
import time
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import psycopg2, psycopg2.extras

dir_test = os.getcwd()
dir_sys = (dir_test + '/docs/')
sys.path.insert(0, dir_sys)
import config

@st.cache
########################################################################
#Function: This function verufy the animation exsit and still available.

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

########################################################################
#Function: This function perfomr scrapping instruction to bring data from ERCOT
#return a dictionary with multiple values

def scrapping_ERCOT():
    vStatus = ""
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.ercot.com//' 
    browser.visit(url)

    # Parse the HTML
    html = browser.html
    html_soup = soup(html, 'html.parser')

    #Numeric values
    tag_box = html_soup.find_all('div', class_='condition')
    counter = 0 
    for tag in tag_box:
        counter += 1
        if counter == 1:
            vReserve = tag.text
        if counter == 2:
            vCurrentDemand = tag.text
        if counter == 3:
            vCommitCapacity = tag.text

    #status    
    tag_box = html_soup.find_all('div', class_='status')
    for tag in tag_box:
        word = tag.text
        vStatus = vStatus + " " + word

    #description
    tag_box = html_soup.find_all('div', class_='desc')
    counter = 0
    for tag in tag_box:
        counter += 1
        if counter == 1:
            vLastUpdate = tag.text
        if counter == 2:
            vCurrentDesc = tag.text
        if counter == 3:
            vCommitCapacityDesc = tag.text
    
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
