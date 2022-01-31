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
    df.rename(columns={0: 'Category',1:'Fiscal Year',2:'Project Square Footage',3:'Energy Savings',4:'Electric Savings',5:'Gas Savings'}, inplace=True)
    st.dataframe(df )


    pro_sq_data = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'single family':[1869786,1927860,1248848,1315484,988650,603204,1146171, 1981188,1764677,1740048, 2164187, 1555919,1909337,2259780,708559],
        'multifamily': [1590010,1877331,2069179,1550817,407991,721401,1648527,2359673,3305387,3061867,1653233,3139624,1795745,4252634,2893444],
        'commercial':[720137,2328639,2637973,2295234,1417141,1410984,1525054,3040720,2938440,3000045,2113280,5404363,4642408,4220531,5830685],
    }
    line_data = pd.DataFrame(
        pro_sq_data,
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
    df.rename(columns={0: 'Category',1:'Fiscal Year',2:'Project Square Footage',3:'Energy Savings',4:'Electric Savings',5:'Gas Savings'}, inplace=True)
    st.dataframe(df )

########## GRAPHS ############
# project square feet over the years
    pro_sq_data_1 = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020],
        'single family':[1869786,1927860,1248848,1315484,988650,603204,1146171, 1981188,1764677,1740048, 2164187, 1555919,1909337,2259780],
        'multifamily': [1590010,1877331,2069179,1550817,407991,721401,1648527,2359673,3305387,3061867,1653233,3139624,1795745,4252634],
        'commercial':[720137,2328639,2637973,2295234,1417141,1410984,1525054,3040720,2938440,3000045,2113280,5404363,4642408,4220531],
    }
    line_data_1 = pd.DataFrame(
        pro_sq_data_1,
        columns=['single family', 'multifamily', 'commercial'])

    st.line_chart(line_data_1)

# demand savings data
    demand_sav_data = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'single family':[817,850,593,601,341,207,362, 481,513,532, 504, 531,661,493,283],
        'multifamily': [801,1301,950,504,90,191,1176,1053,1724,1420,1068,1460,474,1509,969],
        'commercial':[1514,4774,4813,1650,1729,1382,3019,3450,4046,2677,2746,5040,2674,5743,3988],
    }
    demand_line_data = pd.DataFrame(
        demand_sav_data,
        columns=['single family', 'multifamily', 'commercial'])

    st.line_chart(demand_line_data)

# electric savings data
    elec_sav_data = {'Year': [2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'single family':[1067,1082,200,121,211,944,928,799,816,846,1056,812,439],
        'multifamily': [1812,641,208,1813,3751,4788,6135,4073,2731,5078,1322,3887,3151],
        'commercial':[11934,5299,7503,1747,10428,9419,11783,9396,11388,10762,6566,13315,9927],
    }
    elec_line_data = pd.DataFrame(
        elec_sav_data,
        columns=['single family', 'multifamily', 'commercial'])

    st.line_chart(elec_line_data)

# single family data
    single_data = {'Year': [2007, 2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'projects':[981,1021,712,722,585,347,616,729,701,628,649,669,785,700,359],
        'demand savings': [817,850,593,601,341,207,362, 481,513,532, 504, 531,661,493,283],
        'electric savings':[1470,1529,1067,1082,200,121,211,944,928,799,816,846,1056,812,439],
    }
    single_line_data = pd.DataFrame(
        single_data,
        columns=['projects', 'demand savings', 'electric savings'])

    st.line_chart(single_line_data)

# multifamily family data
    multifamily_data = {'Year': [2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'projects':[8,7,5,5,12,13,14,11,11,14,12,15,14],
        'demand savings': [950,504,90,191,1176,1053,1724,1420,1068,1460,474,1509,969],
        'electric savings':[1812,641,208,1813,3751,4788,6135,4073,2731,5078,1322,3887,3151],
    }
    multifamily_line_data = pd.DataFrame(
        multifamily_data,
        columns=['projects', 'demand savings', 'electric savings'])

    st.line_chart(multifamily_line_data)

# commercial data
    commercial_data = {'Year': [2007,2008, 2009, 2010, 2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
        'projects':[16,17,27,19,20,12,14,19,19,14,25,26,27,21,27],
        'demand savings': [1514,4774,4813,1650,1729,1382,3019,3450,4046,2677,2746,5040,2674,5743,3988],
        'energy savings': [27158,72976,42665,19419,25629,8009,53590,62485,50023,59672,43856,81540,55565,56901,30441],
        'electric savings':[3716,13377,11934,5299,7503,1747,10428,9419,11783,9396,11388,10762,6566,13315,9927],
    }
    commercial_line_data = pd.DataFrame(
        commercial_data,
        columns=['projects', 'demand savings', 'energy savings', 'electric savings'])

    st.line_chart(commercial_line_data)

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
    df.rename(columns={0: 'Category',1:'Fiscal Year',2:'Project Square Footage',3:'Electric Savings'}, inplace=True)
    st.dataframe(df )