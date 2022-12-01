import pandas as pd

# viz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# streamlit
import streamlit as st
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parent.parent))

# plotting functions files
from src import viz


# youtube data
videos_info = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\video_info.pkl')
places_mentions_views = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\all_places_views_per_year')

# google trends data
pytrends_top_places_2018= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2018.pkl')
pytrends_top_places_2019= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2019.pkl')
pytrends_top_places_2020 = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2020.pkl')
pytrends_top_places_2021= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2021.pkl')

# tourist arrivals data
number_of_tourist_arrivals = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\international-tourism-number-of-arrivals.pkl')

st.write()

#col1, col2 = st.columns(2)

#with col1:

#with col2:

st.markdown("### Our first piece of information is the places that were mentioned in each video throughout the years 🗺️")
st.markdown("Below you can see graphs showing the top 5 most mentioned places, the number of mentions and the total number of views of all the videos that mentioned each place.")

option = st.selectbox("Select the year:", 
                    (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 'From 2018 to 2021'))

if option == 'From 2018 to 2021':

    top_5_places_views_mentions_2018 = viz.general_data(2018,places_mentions_views)
    st.write(top_5_places_views_mentions_2018)

    top_5_places_views_mentions_2019 = viz.general_data(2019,places_mentions_views)
    st.write(top_5_places_views_mentions_2019)

    top_5_places_views_mentions_2020 = viz.general_data(2020,places_mentions_views)
    st.write(top_5_places_views_mentions_2020)

    top_5_places_views_mentions_2021 = viz.general_data(2021,places_mentions_views, 1)
    st.write(top_5_places_views_mentions_2021)

else:
    top_5_places_views_mentions_x = viz.general_data(option,places_mentions_views)
    st.write(top_5_places_views_mentions_x)