import pandas as pd
#import sklearn
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st
#import numpy as np




df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

st.set_page_config(page_title='Quinns web page', layout='wide', initial_sidebar_state='collapsed')

col1, col2, col3 = st.columns(3)

df.sample(5)

#if df['Survived'] == 1:

grouped = df.groupby("Pclass")["Survived"].mean()


plt.bar(grouped.index, grouped.values)

plt.title('Survival Rate by Class')
plt.xlabel('Classs')
plt.ylabel('Survival Rate')
fig = plt.show()
st.pyplot(fig)
