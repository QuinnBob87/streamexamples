# data enginerring
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
df = df.drop('fips', axis =1)

states_grouped_data = df.groupby(by ='state')

states_grouped_data.head()

# graph 1
plt.plot(df['date'], df['cases'])
plt.title('Date and cases')
plt.xlabel('Date')
plt.ylabel('Values')
plt.xlim([min(df['date']), max(df['date'])])
plt.ylim([min(df['cases']), max(df['cases'])])

graph_1 = plt
plt.show()

# streamlit
tab1 = st.tabs(["GEO"])

with tab1:
   st.header("geo data")
   st.altair_chart(graph_1)
