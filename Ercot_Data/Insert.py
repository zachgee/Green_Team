import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as db_connect
import time
import requests
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


df = ""
vtest = 0
vtest2 = 0
saving = 'stop'
show = 'hide'
st.write("insert rows")

###############################################################
def execute_sql(vSQL,vType):
    host_name="dataviz.cgq2ewzuuqs1.us-east-2.rds.amazonaws.com"
    db_user="postgres"
    db_password="ElPeruano_2021"
    db_name="postgres"
    db_port = 5432
    connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name, port=db_port) 
    cursor = connection.cursor()
    cursor.execute(vSQL)
    
    if vType == 0 :
        result = cursor.fetchall()
        df = pd.DataFrame(result)
    else:
        connection.commit()
        df=""
    
    connection.close()
    return df

#############################################################
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
            vReserve = tag.text.lstrip()
        if counter == 2:
            vCurrentDemand = tag.text.lstrip()
        if counter == 3:
            vCommitCapacity = tag.text.lstrip()

    #status    
    tag_box = html_soup.find_all('div', class_='status')
    counter = 0
    for tag in tag_box:
        word = tag.text.lstrip()
        if counter == 1:
            vStatus = vStatus + " " + word
        else:
            vStatus = word
            counter += 1

    #description
    tag_box = html_soup.find_all('div', class_='desc')
    counter = 0
    for tag in tag_box:
        counter += 1
        if counter == 1:
            vLastUpdate = tag.text.lstrip()
        if counter == 2:
            vCurrentDesc = tag.text.lstrip()
        if counter == 3:
            vCommitCapacityDesc = tag.text.lstrip()
    
    #RETURN
    return {'status':vStatus,
            'reserve':vReserve,
            'current':vCurrentDemand,
            'capacity':vCommitCapacity,
            'updated':vLastUpdate,
            'current_desc':vCurrentDesc,
            'commit_desc':vCommitCapacityDesc}


saving = st.radio('Start saving data',('start','stop'))

while saving=='start':
    #try:
    #vtest = vtest + 10
    #vtest2 = vtest + 20
    #vSQL = ('INSERT INTO public."EO_Ercot" VALUES(' + "'ok'," + str(vtest) + ",'test'," +  str(vtest2) + ",30)")
    ERCOT = scrapping_ERCOT()
    ts = time.time()
    vSQL = ('INSERT INTO public."EO_Ercot" VALUES(' + "'" + ERCOT.get('status') + "','" + str(ERCOT.get('reserve')) + "','" + str(ERCOT.get('current')) + "','" +  str(ERCOT.get('capacity')) + "','" + ERCOT.get('updated') + "'," +  
            str(ts)+")")
    
    st.write(vSQL)
    no = execute_sql(vSQL,1)
      
    time.sleep(60)

###############
show = st.radio('Start saving data',('load','hide'))

if show == 'load':
    vSQL = 'Select * from public."EO_Ercot"'
    df = execute_sql(vSQL,0)
    st.dataframe(df)