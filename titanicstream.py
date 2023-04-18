import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st


df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

st.set_page_config(page_title='Quinns web page', layout='wide', initial_sidebar_state='collapsed')

col1 = st.columns(1)

df.sample(5)

grouped = df.groupby("Pclass")["Survived"].mean()

plt.bar(grouped.index, grouped.values)

plt.title('Survival Rate by Class')
plt.xlabel('Classs')
plt.ylabel('Survival Rate')
fig = plt.show()
st.pyplot(fig)
