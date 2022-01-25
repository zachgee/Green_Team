import streamlit as st
import pandas as pd
import numpy as np
import psycopg2, psycopg2.extras
import config
import plotly.graph_objects as go
import plotly.express as px

connection = psycopg2.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS, database=config.DB_NAME)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

st.title("Green Development in Austin")

st.header("is a header needed?")

st.subheader("The comparison in green energy use between multifamily, single family, and commercial structures")

st.write("info info info")

option = st.sidebar.selectbox("Which Dashboard?", ('Single Family', 'Multifamily', 'Commercial'), )


if option == 'Commercial':
    pattern = st.sidebar.selectbox(
        "Which Option?",
        ("Single Family", "Multifamily", "Commercial")
    )

if pattern == "Commercial":
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year", public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Energy_Savings_MBTU", public."G_Building_Project_Agg"."Elecitrc_Savings_MWH", public."G_Building_Project_Agg"."Gas_Saving"' +
        'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Commercial'")
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    df = pd.DataFrame(result) 
    st.dataframe(df )

    line_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['single family', 'multifamily', 'commercial'])

    st.line_chart(line_data)

if option == 'Multifamily':
    pattern = st.sidebar.selectbox(
        "Which Option?",
        ("Single Family", "Multifamily", "Commercial")
    )

if pattern == "Multifamily":
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year", public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Energy_Savings_MBTU", public."G_Building_Project_Agg"."Elecitrc_Savings_MWH", public."G_Building_Project_Agg"."Gas_Saving"' +
        'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Multifamily'")
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    df = pd.DataFrame(result) 
    st.dataframe(df )

if option == 'Single Family':
    pattern = st.sidebar.selectbox(
        "Which Option?",
        ("Single Family", "Multifamily", "Commercial")
    )

if pattern == "Single Family":
    query = ('SELECT public."G_Building_Project_Agg"."Class", public."G_Building_Project_Agg"."Fiscal_Year", public."G_Building_Project_Agg"."Project_sq", public."G_Building_Project_Agg"."Elecitrc_Savings_MWH"' +
        'FROM public."G_Building_Project_Agg" where public."G_Building_Project_Agg"."Class" =' + "'Single Family'")
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    df = pd.DataFrame(result) 
    st.dataframe(df )