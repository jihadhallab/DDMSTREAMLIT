import pandas as pd
import numpy as np 
import streamlit as st 
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import pickle
from sklearn.linear_model import LinearRegression
st.set_page_config(
    page_title="Snapchat Marketing Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)
image = Image.open('Snapchatlogo.png')
image2 = Image.open('Engage.png')

col4,col5 = st.beta_columns(2)
with col4:
    st.image(image,width=100, use_column_width=50)
with col5:
    st.image(image2,width=120, use_column_width=50)

st.header('Digital Marketing Performance Dataset')
snapchat = pd.read_csv("snapchat.csv")

df = snapchat.groupby(["Start Time","Age"]).sum()["Amount Spent"].reset_index()
df2 = snapchat.groupby(["Gender"]).sum()["Purchases Value"].reset_index()
df3 = snapchat.groupby(["Age"]).sum()["Purchases Value"].reset_index()
df4 = snapchat.groupby(["Start Time", "Campaign Name"]).sum()["Purchases Value"].reset_index()
df5 = snapchat.groupby(["Start Time", "Category"]).sum()["Purchases Value"].reset_index()
df6 = snapchat.groupby(["Start Time", "Sub Category"]).sum()["Purchases Value"].reset_index()
df7 = snapchat.groupby(["Start Time", "Age"]).sum()["Purchases Value"].reset_index()
df8 = snapchat.groupby(["Start Time", "Gender"]).sum()["Purchases Value"].reset_index()
df9 = snapchat.groupby(["Gender"]).sum()["Paid Impressions"].reset_index()
df10 = snapchat.groupby(["Age"]).sum()["Paid Impressions"].reset_index()
df11 = snapchat.groupby(["lat","lng"]).sum()["Purchases Value"].reset_index()
#Amount spent Vs Purchases Value
header = st.beta_container()
dataset = st.beta_container()
sorted(df, reverse=False)


with header:
	st.title('Social Media Marketing Performance Dashboard')
	st.markdown('This dashboard allow marketers to monitor their performance through continuous follow ups on key metrics and KPIs. Visibility into the status of current activities allows for course corrections and incremental improvements that add up over time')


submenu = st.sidebar.selectbox("Submenu",["Exploratory Data Analysis","Time Series Analysis","Map","Machine Learning"])
if submenu == "Exploratory Data Analysis":
    st.subheader("Exploratory Data Analysis")
    st.dataframe(snapchat.head())

    c1,c2 = st.beta_columns(2)
    col1,col2 = st.beta_columns(2)
    with col1:
        with st.beta_expander("Paid Impressions per Gender"):
            st.write("Snapchat Campaign Paid Impressions Performance Across Different Genders")
            fig3 = px.pie(df9,names=df9["Gender"] ,values=df9["Paid Impressions"],color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig3,use_container_width=True)
            st.write(" The Snapchat media campaigns took a higher reception from the paid impressions by Females in KSA ")
        with st.beta_expander("Paid Impressions per Age Group"):
            st.write("Snapchat Campaign Paid Impressions Performance Across Different Age Groups")
            fig4 = px.pie(df10,names=df10["Age"],values=df10["Paid Impressions"],color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig4,use_container_width=True)
            st.write("The Snapchat media campaigns took a higher reception from the paid impressions by the newly working young age group of 25 to 35 years old")


    with col2:
        with st.beta_expander("Purchases Value per Gender"):
            st.write("Snapchat Campaign Purchases Proportion Across Different Genders")
            fig1 = px.bar(df2,x=df2["Gender"] ,y=df2["Purchases Value"],color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig1,use_container_width=True)
            st.write(" We can observe that the Paid impressions have a positive relationship affect on the Purchases in dollars as reflected in the barchart as also its the females that purchased the most and this might be the cause of the type of product/segment being advertised ")
        with st.beta_expander("Purchases Value per Age Group"):
            st.write("Snapchat Campaign Purchases Proportion Across Different Age Groups")
            fig2 = px.bar(df3,x=df3["Age"],y=df3["Purchases Value"],color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig2,use_container_width=True)
            st.write(" We can observe that the Paid impressions have a positive relationship affect on the Purchases in dollars as reflected in the barchart as also its the age group of 25-35 that purchased the most and this might be the cause of the type of product/segment being advertised that might relate to this target age group")
elif submenu == "Time Series Analysis":
    st.subheader("Time Series Analysis")
        
    with st.beta_expander("Purchases Value by Campaign Name Over 6 Months"):
        fig5 = px.line(df4, x="Start Time", y="Purchases Value", color='Campaign Name')
        st.plotly_chart(fig5,use_container_width=True)
        st.write("The top campaign that actually got the highest revenue from advertising are both the Happy Ramadan Campaign, & the Ramadan 2020 Campaign which could be caused by the type of campaign which is displayed below")
    with st.beta_expander("Purchases Value by Campaign Sub Category Over 6 Months"):
        fig7 = px.line(df6,x="Start Time", y="Purchases Value", color='Sub Category')
        st.plotly_chart(fig7,use_container_width=True)
        st.write("The top performing Sub Categories were the Engaging Content & the Clickable Flyer which reflect on the function of each type of category campaign that triggers the target audience to become a lead to the company")
    with st.beta_expander("Purchases Value by Age Group Over 6 Months"):
        fig9 = px.line(df7,x="Start Time", y="Purchases Value", color='Age')
        st.plotly_chart(fig9,use_container_width=True)
        st.write("As displayed in the Exploratory Data Analysis section, the age group of 25-35 contributed to the highest share of purchases and that is mainly due to the type of advertising message & product that directly relates to them which shows that the target audience are of millenials and this is vital in order to adapt future media campaign messages to this age group")
    with st.beta_expander("Purchases Value by Gender Group Over 6 Months"):
        fig10 = px.line(df8,x="Start Time", y="Purchases Value", color='Gender')
        st.plotly_chart(fig10,use_container_width=True) 
        st.write("As displayed in the Exploratory Data Analysis section, Female contributed to the highest share of purchases and that is mainly due to the type of advertising message & product that directly relates to them ")
elif submenu == "Map":
    st.subheader("Distribution of Purchases on KSA Map")
    with st.beta_expander("Distribution of Purchases on KSA Map"):
        fig = px.scatter_mapbox(df11, lat="lat", lon="lng", size = df11["Purchases Value"], hover_data=["Purchases Value"],
        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig,use_container_width=True) 
        st.write("The map above displays the distrubtion of purchases across KSA based on 7 media campaigns using snapchat as the digital media platform, the map shows that Riyadh & Jeddah contributed to the highest share of purchases, $134,000 & $102,000 respectively, which reflect on where demographically target customers of xyz company and based on the Exploratory Data Analysis & the Time Series Analysism the age group of 25-35 and the Female audience would probably mostly live around those two big cities since its a hub for business in the KSA ")
elif submenu == "Machine Learning" :
    Budget = st.text_input('The Budget you want to allocate for snapchat media campaign ', value=0)
    Budget_num = (float(Budget) - 67.723764) / 160.080263
    Gender = st.selectbox('Choose Gender Type:', ['Female', 'Male'])

    Gender_Female = 0
    Gender_Male = 0

    if Gender == 'Female':
        Gender_Female = 1
    elif Gender == 'Male':
        Gender_Male = 1

    Category = st.selectbox('Choose Category Type:', ["M&B","Omnichannel","PL"])

    Category_MandB = 0
    Category_Omnichannel = 0
    Category_PL = 0

    if Category == 'M&B':
        Category_MandB = 1
    elif Category == 'Omnichannel':
        Category_Omnichannel = 1
    elif Category == 'PL':
        Category_PL = 1

    model = pickle.load(open('model.sav', 'rb'))

    predicted_val = model.predict([[Budget_num, Gender_Female,Gender_Male,Category_MandB,Category_Omnichannel,Category_PL]])
    st.write(f'Revenue = {predicted_val[0]}')