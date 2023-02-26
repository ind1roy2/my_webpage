import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib import image
import plotly.express as px
df = sns.load_dataset('tips')
st.title("TIPS DASHBOARD")
st.image("https://health.clevelandclinic.org/wp-content/uploads/sites/3/2018/07/GettyImages-824302050.jpg")
st.dataframe(df)

sm = st.selectbox("Select as smoker or non smoker:",df['smoker'].unique())


fig1 = px.histogram(df[df['smoker']==sm],x='day')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(df[df['smoker']==sm],x='time')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(df[df['smoker']==sm],x='sex')
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.line(df[df['smoker']==sm],y='total_bill')
st.plotly_chart(fig4, use_container_width=True)


