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

pytrends_top_places_2018= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2018.pkl')
pytrends_top_places_2019= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2019.pkl')
pytrends_top_places_2020 = pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2020.pkl')
pytrends_top_places_2021= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2021.pkl')

# Loading previously extracted Hotel occupancy rate and international arrivals data

hotel_data = pd.read_pickle(r'Projects\Final project\data\hotel_data_edited.pkl')
number_of_tourist_arrivals = pd.read_pickle(r'Projects\Final project\data\international-tourism-number-of-arrivals.pkl')

# Loading dataframes to SQL

engine = sql_connection.connecting()

#channel_stats.to_sql('channel_stats', con=engine)
#videos_info.drop(columns = ['all_countries', 'all_cities', 'all_regions', 'everywhere']).to_sql('info_about_all_videos', con=engine)
#places_per_year_by_channel.to_sql('places_per_year_by_channel', con=engine) #to be debugged
#places_mentions_views.to_sql('places_mentions_views', con=engine)
#pytrends_top_places_2018.to_sql('pytrends_top_places_2018', con=engine)
#pytrends_top_places_2019.to_sql('pytrends_top_places_2019', con=engine)
#pytrends_top_places_2020.to_sql('pytrends_top_places_2020', con=engine)
#pytrends_top_places_2021.to_sql('pytrends_top_places_2021', con=engine)
#hotel_data.to_sql('hotel_occupancy_data', con=engine)
#number_of_tourist_arrivals.to_sql('number_of_tourist_arrivals', con=engine)

##################################################################

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

# Some places extracting were introducing a bias into the data, so here I am deleting these places.
# kara and nate: tennessee and nashville are in every description because it's their address
# kristen e siya: their address is on many descriptions and it's grimsby, ontario(2017, 2018, 2019); they do have videos talking about ontario though
# yes theory: ed, four and thomas are not places
# drew binsky: in some of his recent (2021, 2022) descriptions he links some of his most popular videos and one of them is "► Why is Everything Free in Pakistan?"

cleaning.deleting_biased_places(videos_info, ['Tennessee', 'Nashville'], 1, 'Kara and Nate', 0)
cleaning.deleting_biased_places(videos_info, ['Ontario', 'Grimsby'], 2, 'Kristen & Siya', 2017)
cleaning.deleting_biased_places(videos_info, ['Four', 'Ed', 'Thomas'], 1, 'Yes Theory', 0)
cleaning.deleting_biased_places(videos_info, ['Pakistan'], 2, 'Drew Binsky', 2021)

places_per_year = cleaning.counting_ocurrences_places(videos_info)
places_per_year_by_channel = cleaning.counting_ocurrences_places_by_channel(videos_info)

places_per_year = cleaning.get_views_per_top_place(videos_info, places_per_year)

for i in range(2010, 2022):
    
    aux2 = cleaning.organizing_places_views_df(places_per_year, i)
    places_per_year2 = pd.concat([places_per_year2, aux2]).reset_index(drop = True)
    places_per_year2

###############################################################

# Extracting google trends info
pytrends_top_places_2018 = api.getting_google_trends(places_per_year_filtered, 2018)
pytrends_top_places_2018

pytrends_top_places_2019 = api.getting_google_trends(places_per_year_filtered, 2019)
pytrends_top_places_2019

pytrends_top_places_2020 = api.getting_google_trends(places_per_year_filtered, 2020)
pytrends_top_places_2020

pytrends_top_places_2021 = api.getting_google_trends(places_per_year_filtered, 2021)
pytrends_top_places_2021
