# data enginerring
import seaborn as sns
import pandas as pd
import numpy as np
import altair as alt
#import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
df = df.drop('fips', axis =1)

states_grouped_data = df.groupby(by ='state')

states_grouped_data.head()


# graph 1
sns.lineplot(x = df['date'], y = df['cases'], data = df)
sns.despine()
graph_1 = sns

for index, row in df.iterrows():
    state = row["state"]
    if state == "Alabama":
        df.at[index, "population"] = 5024279
    elif state == "Alaska":
        df.at[index, "population"] = 733391
    elif state == "Arizona":
        df.at[index, "population"] = 7151502
    elif state == "Arkansas":
        df.at[index, "population"] = 3011524
    elif state == "California":
        df.at[index, "population"] = 39538223
    elif state == "Colorado":
        df.at[index, "population"] = 5773714
    elif state == "Connecticut":
        df.at[index, "population"] = 3605944
    elif state == "Delaware":
        df.at[index, "population"] = 989948
    elif state == "Florida":
        df.at[index, "population"] = 21538187
    elif state == "Georgia":
        df.at[index, "population"] = 10711908
    elif state == "Hawaii":
        df.at[index, "population"] = 1455271
    elif state == "Idaho":
        df.at[index, "population"] = 1839106
    elif state == "Illinois":
        df.at[index, "population"] = 12812508
    elif state == "Indiana":
        df.at[index, "population"] = 6785528
    elif state == "Iowa":
        df.at[index, "population"] = 3192406
    elif state == "Kansas":
        df.at[index, "population"] = 2937880
    elif state == "Kentucky":
        df.at[index, "population"] = 4505836
    elif state == "Louisiana":
        df.at[index, "population"] = 4648794
    elif state == "Maine":
        df.at[index, "population"] = 1362359
    elif state == "Maryland":
        df.at[index, "population"] = 6177224
    elif state == "Massachusetts":
        df.at[index, "population"] = 7029917
    elif state == "Michigan":
        df.at[index, "population"] = 10077331
    elif state == "Minnesota":
        df.at[index, "population"] = 5706494
    elif state == "Mississippi":
        df.at[index, "population"] = 2961279
    elif state == "Missouri":
        df.at[index, "population"] = 6160281
    elif state == "Montana":
        df.at[index, "population"] = 1084225
    elif state == "Nebraska":
        df.at[index, "population"] = 1961504
    elif state == "Nevada":
        df.at[index, "population"] = 3104614
    elif state == "New Hampshire":
        df.at[index, "population"] = 1377529
    elif state == "New Jersey":
        df.at[index, "population"] = 9288994
    elif state == "New Mexico":
        df.at[index, "population"] = 2117522
    elif state == "New York":
        df.at[index, "population"] = 20215751
    elif state == "North Carolina":
        df.at[index, "population"] = 10600823
    elif state == "North Dakota":
        df.at[index, "population"] = 779094
    elif state == "Ohio":
        df.at[index, "population"] = 11799448
    elif state == "Oklahoma":
        df.at[index, "population"] = 39538223
    elif state == "Oregon":
        df.at[index, "population"] = 4217737
    elif state == "Pennsylvania":
        df.at[index, "population"] = 13011844
    elif state == "Rhode Island":
        df.at[index, "population"] = 1097379
    elif state == "South Carolina":
        df.at[index, "population"] = 5210095
    elif state == "South Dakota":
        df.at[index, "population"] = 886667
    elif state == "Tennessee":
        df.at[index, "population"] = 6897576
    elif state == "Texas":
        df.at[index, "population"] = 29145505
    elif state == "Utah":
        df.at[index, "population"] = 3271616
    elif state == "Vermont":
        df.at[index, "population"] = 643503
    elif state == "Virginia":
        df.at[index, "population"] = 8626207
    elif state == "Washington":
        df.at[index, "population"] = 7693612
    elif state == "West Virginia":
        df.at[index, "population"] = 1793716
    elif state == "Wisconsin":
        df.at[index, "population"] = 5851754
    elif state == "Wyoming":
        df.at[index, "population"] = 577719
    else:
        df = df.drop(index, axis=0)


# streamlit

tab1 = st.tabs(["GEO"])

with tab1:
   st.header("geo data")
   st.altair_chart(graph_1)
