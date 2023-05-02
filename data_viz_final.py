# data enginerring
#import seaborn as sns
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
df = df.drop('fips', axis =1)

#df = df.groupby(by ='state', axis=0)

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date2'] = df['date']
df['month'] = df['date'].dt.month
df['day_of_month'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek
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

def assign_region(state):
    if state in ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']:
        return 'Northeast'
    elif state in ['New Jersey', 'New York', 'Pennsylvania']:
        return 'Mid-Atlantic'
    elif state in ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']:
        return 'Midwest'
    elif state in ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']:
        return 'Great Plains'
    elif state in ['Delaware', 'District of Columbia', 'Maryland', 'Virginia', 'West Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida']:
        return 'Southeast'
    elif state in ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee']:
        return 'South'
    elif state in ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas']:
        return 'Southwest'
    elif state in ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', "Washington"]:
        return 'West'
    else:
        return 'Unknown'

df['region'] = df['state'].apply(assign_region)
state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
df['state_abbrev'] = df['state'].map(state_abbrev)
df['cases_pop'] = df['cases']/df['population']
df['death_cas'] = df['deaths']/df['population']
df['region_population'] = df.groupby('region')['population'].transform('sum')
df['region_cases'] = df.groupby('region')['cases'].transform('sum')
df['region_deaths'] = df.groupby('region')['deaths'].transform('sum')
df['region_cases_pop'] = df['region_cases']/df['region_population']
df['region_death_cas'] = df['region_deaths']/df['region_population']

# graph 1
graph1 = px.choropleth(df, locations='state_abbrev', locationmode='USA-states',
                    color='cases_pop', scope='usa', title='US Covid Cases by State')

# graph 2
graph2 = px.choropleth(df, locations='state_abbrev', locationmode='USA-states',
                    color='cases_pop', scope='usa', title='US Covid Cases by State')

# graph 3
graph3 = px.choropleth(df, locations='state_abbrev', locationmode='USA-states',
                    color='region_cases_pop', scope='usa', title='US Covid Cases by State')

# graph 4
graph4 = px.choropleth(df, locations='state_abbrev', locationmode='USA-states',
                    color='region_death_cas', scope='usa', title='US Covid Deaths/Population')

# graph 5 
df2 = df[['date', 'population', 'cases', 'deaths', 'region', 'cases_pop']]
mask = df['date'].dt.year == 2022
df3 = df2[mask]
df_grouped = df3.groupby(['date', 'region']).sum().reset_index()
graph5 = alt.Chart(df_grouped).mark_line().encode(
    x='date:T',
    y='cases_pop:Q',
    color='region:N'
).properties(
    width=600,
    height=400,
    title='COVID-19 Cases/Population by Region in 2022'
)


# graph 6
df2 = df[['date', 'population', 'cases', 'deaths', 'region', 'death_cas']]
mask = df['date'].dt.year == 2022
df3 = df2[mask]
df_grouped = df3.groupby(['date', 'region']).sum().reset_index()
graph6 = alt.Chart(df_grouped).mark_line().encode(
    x='date:T',
    y='death_cas:Q',
    color='region:N'
).properties(
    width=600,
    height=400,
    title='COVID-19 deaths/Population by Region in 2022'
)


# graph 7
df2 = df[['date', 'population', 'cases', 'deaths', 'region', 'cases_pop']]
mask = df['date'].dt.year == 2022
df3 = df2[mask]
df_grouped = df3.groupby(['date', 'region']).sum().reset_index()
graph7 = alt.Chart(df_grouped).mark_bar().encode(
    x='region:N',
    y='cases_pop:Q',
    color='region:N'
).properties(
    width=600,
    height=400,
    title='COVID-19 Cases/Population by Region in 2022'
)


# graph 8
df2 = df[['date', 'population', 'cases', 'deaths', 'region', 'death_cas']]
mask = df['date'].dt.year == 2022
df3 = df2[mask]
df_grouped = df3.groupby(['date', 'region']).sum().reset_index()
graph8 = alt.Chart(df_grouped).mark_bar().encode(
    x='region:N',
    y='death_cas:Q',
    color='region:N'
).properties(
    width=600,
    height=400,
    title='COVID-19 deaths/Population by Region in 2022'
)
desc1 = "Description for graph 1 goes here"
desc2 = "Description for graph 2 goes here"
desc3 = "Description for graph 3 goes here"
desc4 = "Description for graph 4 goes here"
desc5 = "Description for graph 5 goes here"
desc6 = "Description for graph 6 goes here"
desc7 = "Description for graph 7 goes here"
desc8 = "Description for graph 8 goes here"

# Define the pages of your app
pages = {
    "Page 1 title": {
        "image": "image1.jpg",
        "description": "Enter your text here"
    },
    "Page 2 title": {
        "graphs": [st.pyplot(graph1), st.pyplot(graph2)],
        "descriptions": [desc1, desc2]
    },
    "Page 3 title": {
        "graphs": [st.pyplot(graph3), st.pyplot(graph4)],
        "descriptions": [desc3, desc4]
    },
    "Page 4 title": {
        "graphs": [st.pyplot(graph5), st.pyplot(graph6)],
        "descriptions": [desc5, desc6]
    },
    "Page 5 title": {
        "graphs": [st.pyplot(graph7), st.pyplot(graph8)],
        "descriptions": [desc7, desc8]
    }
}

# Define a function to display the current page
def display_page(page):
    if "image" in pages[page]:
        st.image(pages[page]["image"])
        st.text_input("Enter your text here")
    else:
        for i in range(len(pages[page]["graphs"])):
            st.subheader(f"Graph {i+1}")
            pages[page]["graphs"][i]
            st.write(pages[page]["descriptions"][i])

# Create the Streamlit app
st.set_page_config(page_title="My App", page_icon=":chart_with_upwards_trend:")
st.title("My App")

# Create a dropdown menu to navigate between pages
current_page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the current page
display_page(current_page)

# Create links to all other pages at the bottom of the app
st.sidebar.markdown("---")
for page in pages:
    if page != current_page:
        st.sidebar.markdown(f"[{page}](#{page.lower().replace(' ', '-')})")
