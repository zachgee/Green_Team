# Green Team - Energy Dashboard

## Overview / Topic

After the devastating winter freeze last year, Texas' energy use & distribution was put under a microscope. Texas produces and consumes more electricity than any other state; in fact, it's the only state that runs a stand-alone independent electricity grid. Therefore, Texans demanded to know why the power grid suddenly failed us in such a dire time & what is being done to prevent future tragedies.

To determine what can be changed regarding our energy structure, we've compiled some data sets from the City of Austin. While analyzing this subset of the Texas power grid, we're hoping to answer: what is the current consumer demand & has it increased over the last few years? What energy sources are we using? What are green alternatives in the capital and how are those being developed and/or utilized?  

## Tech Stack:

### Resources 

The data source for the dashboard will be extract from the corporate report library available from the [Austin Energy portal](https://austinenergy.com/ae/about/reports-and-data-library/data-library/energy-efficiency-solar/energy-efficiency-solar). This data was be available from the 
offical city of Austin open data portal: [data.austintexas.gov] (https://data.austintexas.gov/).

### Database
The data will be centralize in a Amazon cloud service using a Postgre database. We decided use a relational database to analyze the connection between the datasets.

### Libraries / Packages
The dashboard will be designed based on the open source framework [streamlit] (https://streamlit.io/) which is based in python. 
Additionally we will use plotly for chart and visualization tools. The final release/deploy will be using the streamlit library. 


## Deliverable(s) and timeframe

## Successes metrics -

### Deliverable 1 

Topics complete: 
- Project scope : Official document with a full description about the project content.
- Home and Navigation : Layout of the Home screen including background images and animation. Navigation should display the two main section and the additional subdivisions. Logic will be available from the github repo.
- Database connection ready including all tables : All the tables (datasets) will be available from the Amazon cloud database. Multiple user credentials will be ready for all the team members. 
- Layout for Energy Summary and Green Development : First overview of the screen include the object distribution and the election of charts for the dataset. 

*Date : January 23rd*

### Deliverable 2 

Topics complete: 
- Energy Summary and all sections complete : Screens and database base connections will be fully functional including filter to refresh the views.  
- Green Development and all sections complete : Screens and database base connections will be fully functional including filter to refresh the views.  

*Date : January 30th*

### Deliverable 3 

Topics complete: 
- Review and additional adjustments " Adjust animations or database connection for filter (issues/bug review).
- Official deployment using streamlit library. 
- Document with conclusion and result analysis from the Energy dataset. 

*Date : February 2nd*

## Dashboard Sections

### Home View

This is the main screen of the project. It will display a reference from the ERCOT webapge with reference about the current capacity of energy in Texas.

### Navigation bar

Slide pop-up on the right side of the dashboard. This pop-up will provide easy access to the main section of the dashboard and the subdivision. 
Additional it will display the current day and time. 

### V1 Energy Summary

- Customer class
- Power Plants in Texas and Production Cost
- Renewable Resources and Power supply
- Residential Bill Average

### V2 Green Development 
- Commercial 
- Multifamily
- Single Family
- Green Building projects
- Electric Vehicles stations available.
- Estimate emmission (historic records)
