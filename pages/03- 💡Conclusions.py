import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

# plotting functions files
from src import viz


st.header("What did we learn from all this? 🤔")
st.markdown("""
**1. The analysis shows that there doesn't seem to be any correlation between the YouTube views for the 10 travel channels and 
people's interest in the places mentioned by said channels according to Google Trends results.** 
- *What could be different*: on Google Trends I took into consideration the searches made throughout the entire world. 
If I had access via YouTube to the viewers's countries, I could limit the search to these specific places and have more accurate results. 
Also, as mentioned before, only having the data for total views on the day of the API request doesn't allow me to find a reliable correlation 
(or not). I had to compare Trends results for the week the video was posted, 
but it's likely that for a number of videos the views weren't high on the week they were posted.""")
'\n\n\n'
st.write("""
**2. Similarly, no correlation between YouTube views and number of tourist arrivals in the places mentioned in the videos was found.** 
The pandemic also played a pivotal role here. Even if one of the YouTubers was creating videos about a specific place that gathered many views, 
most people in the world couldn't simply go there. 
- *What could be different*: it could be interesting to explore this correlation since the first year in which the videos were published 
(2009) and see if anything's different, but the lack of consistency for the tourism data - for some countries it's international arrivals, 
for others it's arrivals in general - would make it hard to be rigorous. Besides, ideally I would have access to arrivals per month (or week) 
for every single year along with total views per month (or week). This way, I could check for a delayed correlation, maybe 3, 6 and 9 months 
(because someone that watches a video about India won't go to India on the same day), and analyse with more accuracy if it would exist or not. 
I also explored hotel occupancy rate data because it would definitely be interesting to compare it against everything else, 
but it was heavily incomplete for about half of the places analysed here.  
""")
'\n\n\n'

st.write("""**3. I believe the great challenge of this project was comparing a sample of around 10 thousand videos, 
each one gathering at most 50mi views in rare ocasions, against the biggest search engine in the world.** Given this, 
all the results were expected. There wasn't enough volume of people watching these videos to have an impact on Google Trends or on "real life", 
and most importantly, the aim of this project was never to prove causation, but simply investigate if there was any interesting 
connection between the 3 datasets.
- *What could be different*: a different strategy could be instead of limiting my sample to 10 travel channels, 
simply gathering videos that mentioned 'travel', 'trip', 'visit', etc, and repeating the analysis with them. 
This way, I could have a much larger number of videos (the sky would be the limit!) to analyse. 
Many other challenges would arise, such as the "relevant to my account" problem I mentioned at the beginning, 
but maybe the results would tell us a different story.
  
  
  
##### Thank you so much for reading and I hope you've enjoyed! Want to ask me a question or send me your suggestions? Let's connect on [LinkedIn](https://www.linkedin.com/in/mayara-almeida-souza/) then! 💻   
""")
col1, col2 = st.columns(2)

