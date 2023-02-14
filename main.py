from src.sql_loading_and_queries import sql_connection
from src import cleaning_and_nlp as cleaning
from src import api

import pandas as pd

# youtube api
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Youtube data

channel_stats = pd.read_pickle(r'Projects\Final project\data\channel_stats.pkl')
videos_info = pd.read_pickle(r'Projects\Final project\data\video_info.pkl')
places_per_year_by_channel = pd.read_pickle(r'Projects\Final project\data\places_per_year_by_channel.pkl')
places_per_year_filtered = pd.read_pickle(r'Projects\Final project\data\places_year_filtered_notuple.pkl')
places_mentions_views = pd.read_pickle(r'Projects\Final project\data\all_places_views_per_year')

# Loading previously extracted Google trends data

pytrends_concat = pd.read_pickle(r'./data/pytrends_concat.pkl')
pytrends_related_concat = pd.read_pickle(r'./data/pytrends_related_concat.pkl')
videos_trends_merged = pd.read_pickle(r'./data/videos_trends_merged.pkl')

# Loading previously extracted Hotel occupancy rate and international arrivals data

number_of_tourist_arrivals = pd.read_pickle(r'Projects\Final project\data\international-tourism-number-of-arrivals.pkl')


# Google credentials to use the Youtube API

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = os.getenv('yt_key')

youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey = DEVELOPER_KEY)

##################################################################

# Channel ids chosen

channel_ids = ['UCnTsUMBOA8E-OHJE-UrFOnA', #samuel and audrey
               'UC4ijq8Cg-8zQKx8OH12dUSw', #kara and nate
               'UCyEd6QBSgat5kkC6svyjudA', #mark weins
               'UCvK4bOhULCpmLabd2pDMtnA', #yes theory
               'UCFr3sz2t3bDp6Cux08B93KQ', #wolters world
               'UC0Ize0RLIbGdH5x4wI45G-A', #drew binsky
               'UC_DmOS_FBvO4H27U7X0OtRg', #fearless and far
               'UCBo9TLJiZ5HI5CXFsCxOhmA', #gone with the wymns
               'UCt_NLJ4McJlCyYM-dSPRo7Q', #lost leblanc
               'UC0Tf8LUUtL3E24Dr28vXkbA' #hopscotchtheglobe
              ]

##################################################################

# Getting the info from Youtube
channel_stats = api.get_channel_stats(youtube, channel_ids)
videos_info = api.creating_info_df(youtube, channel_stats)

# Pre-processing of the Youtube data (cleaning and entity recognition)
cleaning.deleting_emojis(videos_info)
cleaning.cleaning_dfs(videos_info)
cleaning.extracting_places(videos_info)

# Creating a new dataframe with the number a count for how many times each place was mentioned in each year
places_per_year = cleaning.counting_ocurrences_places(videos_info)

# Doing the same as before, but in this dataframe I can see how many times each place was mentioned by each channel
places_per_year_by_channel = cleaning.counting_ocurrences_places_by_channel(videos_info)


# Deleting the biased places
cleaning.deleting_biased_places(videos_info, ['Tennessee', 'Nashville'], 1, 'Kara and Nate', 0)
cleaning.deleting_biased_places(videos_info, ['Ontario', 'Grimsby'], 2, 'Kristen & Siya', 2017)
cleaning.deleting_biased_places(videos_info, ['Four', 'Ed', 'Thomas'], 1, 'Yes Theory', 0)
cleaning.deleting_biased_places(videos_info, ['Pakistan'], 2, 'Drew Binsky', 2021)

# Adding up all the views gathered throughout all the videos that were mentioning each place in a certain year (from 2009 to 2022)
places_per_year = cleaning.get_views_per_top_place(videos_info, places_per_year)

# Getting rid of the list of tuples
places_per_year_views = cleaning.organizing_places_views_df(places_per_year)
    

###############################################################

# Extracting google trends info for places
pytrends_thailand = api.getting_google_trends(['Thailand'])
pytrends_india = api.getting_google_trends(['India'])
pytrends_pakistan = api.getting_google_trends(['Pakistan'])
pytrends_california = api.getting_google_trends(['California'])
pytrends_tabriz = api.getting_google_trends(['Tabriz'])
pytrends_mexico = api.getting_google_trends(['Mexico'])
pytrends_arizona = api.getting_google_trends(['Arizona'])

# Extracting google trends info for the searches "travel place" and "flight place"
pytrends_thailand_related = api.getting_google_trends(['travel thailand', 'flight thailand'])
pytrends_india_related = api.getting_google_trends(['travel india', 'flight india']) 
pytrends_pakistan_related = api.getting_google_trends(['travel pakistan', 'flight pakistan']) 
pytrends_california_related = api.getting_google_trends(['travel california', 'flight california'])
pytrends_tabriz_related = api.getting_google_trends(['travel tabriz', 'flight tabriz'])
pytrends_mexico_related = api.getting_google_trends(['travel mexico', 'flight mexico'])
pytrends_arizona_related = api.getting_google_trends(['travel arizona', 'flight arizona'])

