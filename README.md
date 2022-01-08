# Green Team - Energy Dashboard

## Overview / Topic

Energy distribution and forecast have become a major topic during the last year in the state of Texas. The last polar vortex in February of 2021 caused an unxpected impact on the city and raised the question about how prepared is Texas for similar events in the future. 
Texas consumes and produces more electricity than any other state; in fact, it is the only state that runs a stand-alone independent electricity grid. So why did we had a such terrible experience with electricity last year? Before jumping to any conclusions, it is important to understand and analyze Texas power grid in order to answer these kind of questions: what is the regular consumer demand? How has it increased over the last years? What are the green alternatives in the capital?
The purpose of this project is to answer those questions by analyzing the energy data for the city of Austin. We will provide a web-based dashboard with data visualization object to extract, transform and display the historic raw data accumulated by Austin Energy and the local governmnet in Austin.   


##Proposal Requirements -
- Have ONE person create your repo, make a .md file with the following.
- Pin the link to the repo to your groups channel.

## Tech Stack:

### Resources 

The data source for the dashboard will be extract from the corporate report library available from the [Austin Energy portal](https://austinenergy.com/ae/about/reports-and-data-library/data-library/energy-efficiency-solar/energy-efficiency-solar). This data was be available from the 
offical city of Austin open data portal: [data.austintexas.gov] (https://data.austintexas.gov/).

### Database
The data will be centralize in a Amazon cloud service using a Postgre database. We decided use a relational database to analyze the connection between the datasets.

### Libraries / Packages
The dashboard will be designed based on the open source framework [streamlit] (https://streamlit.io/) which is based in pythong. 
Additionally we will use plotly for chart and visualization tools. 


## Deliverable(s) and timeframe
- smaller actions/steps to be taken. Make sure these can be broken down into issues.
- What the final  project will be (website, dashboard, analysis, etc).

## Successes metrics -

### Deliverable 1 

Topics complete: 
    - Project scope
    - Home and Navigation
    - Database connection ready including all tables 
    - Layout for Energy Summary and Green Development

Date : January 23rd

### Deliverable 2 

Topics complete: 
    - Energy Summary and all sections complete.
    - Green Development and all sections complete.

Date : January 30th

### Deliverable 3 

Topics complete: 
    - Review and additional adjustments
    - Official deploy

Date : February 2nd

## Dashboard Sections

### Home View

This is the main screen of the project. It will display a reference from the ERCOT webapge with reference about the current capacity of energy in Texas.

### Navigation bar

Slide pop-up on the right side of the dashboard. This pop-up will provide easy access to the mnain section of the dashboard and the subdivision. 
Additional it will display the current day and time. 

### V1 Energy Summary

- Residential Average Monthly 
- Saving
- Peak Demand
- Programs Expenditures
- Weatherization Assistance program

### V2 Green Development 
- Commercial 
- Multifamily
- Single Family
- Green Building projects
- Electric Vehicles stations available.

