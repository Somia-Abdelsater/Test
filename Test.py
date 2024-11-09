# importing Libraries
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# 
st.set_page_config(page_title="Sales Dashboard",page_icon=None,layout="wide",initial_sidebar_state="auto")
# loading Data
data =pd.read_csv("Superstore.csv",encoding='windows-1252')
# Make sure the 'date' column is of datetime type
data['Order Date'] = pd.to_datetime(data['Order Date'])

# sidebar
st.sidebar.header("Sales Dashboard")
st.sidebar.image("Sales.jpg")
st.sidebar.write("This is Sales dashboard for superstore")
st.sidebar.write("")
st.sidebar.markdown("Made By :chart_with_upwards_trend:"
                     +"[Somia Abdelsater](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)")
st.sidebar.write("")
st.sidebar.write("Filter You Data")
city=st.sidebar.selectbox("City:",data['City'].drop_duplicates())
year=st.sidebar.selectbox("Year:",data['Order Date'].dt.year.drop_duplicates())

#Body
# row 1
c1,c2,c3,c4=st.columns(4)

c1.metric("Total Sales(K)",(data['Sales'].sum()/1000).round())
c2.metric("Total Profit(K)",(data['Profit'].sum()/1000).round())
c3.metric("Total Quantity(K)",(data['Quantity'].sum()/1000).round())
c4.metric("Profit Margin(%)",(data['Profit'].sum()/data['Sales'].sum()*100).round())

#row 2
c21,c22=st.columns(2)
fig=px.bar(data_frame=data[(data['City'] == city)& (data['Order Date'].dt.year == year)], x='Segment' ,y ='Sales')
c21.plotly_chart(fig,use_container_width=True)
fig=px.bar(data_frame=data[(data['City'] == city)& (data['Order Date'].dt.year == year)], x='City' ,y ='Sales')
c22.plotly_chart(fig,use_container_width=True)

#row 3
fig=px.scatter(data_frame=data[(data['City'] == city)& (data['Order Date'].dt.year == year)], x='Sales' ,y ='Profit',color='Segment',size='Quantity')
st.plotly_chart(fig,use_container_width=True)

# Row 4
c41,c42=st.columns(2)
with c41:
    st.text("Sales by Region")
    fig=px.pie(data_frame=data[(data['City'] == city)& (data['Order Date'].dt.year == year)],names='Region',values='Sales')
    st.plotly_chart(fig,use_container_width=True)
with c42:
    st.text("Sales by Category")
    fig=px.pie(data_frame=data[(data['City'] == city)& (data['Order Date'].dt.year == year)],names='Category',values='Sales',hole=.4)
    st.plotly_chart(fig,use_container_width=True)
