import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

# plotting functions files
from src import viz


# merged/correlation data 
mergedthai = pd.read_pickle(r"C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\mergedthai.pkl")
mergedindia = pd.read_pickle(r"C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\mergedindia.pkl")

st.header("What did we learn from all this? 🤔")
st.markdown("Looking at all the graphs plotted we can make an educated guess and say there's no indication of a correlation between these particular videos and people's interest in the places mentioned.")
st.markdown("However, it is interesting to see this relationship numerically too. For the purposes of this presentation, I decided to plot the correlation heatmap for only te two places that were the most viewed more than one time between 2018 and 2021.")
st.markdown("For the heatmap, data from 2010 to 2021 was used.")
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(viz.correlation_heatmap(mergedthai, 'Thailand'), theme='streamlit')
with col2:
    st.plotly_chart(viz.correlation_heatmap(mergedindia, 'India'), theme='streamlit')

st.subheader("Final conclusions 🏁")
st.markdown("For Thailand there seems to be a correlation between Google Trends and tourist arrivals, but not between anything else. Now, for India, no correlation was found.")
st.markdown("The results will most likely be similar for the other places analysed since the data appears to behave similarly too. The next step would be checking this correlation numerically for all the places.")
