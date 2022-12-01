from src.sql_loading_and_queries import sql_connection
import pandas as pd

# Youtube data

channel_stats = pd.read_pickle(r'Projects\Final project\data\channel_stats.pkl')
videos_info = pd.read_pickle(r'Projects\Final project\data\video_info.pkl')
places_per_year_by_channel = pd.read_pickle(r'Projects\Final project\data\places_per_year_by_channel.pkl')
places_per_year_filtered = pd.read_pickle(r'Projects\Final project\data\places_year_filtered_notuple.pkl')
places_mentions_views = pd.read_pickle(r'Projects\Final project\data\all_places_views_per_year')

# Google trends data

pytrends_top_places_2018= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2018.pkl')
pytrends_top_places_2019= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2019.pkl')
pytrends_top_places_2020 = pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2020.pkl')
pytrends_top_places_2021= pd.read_pickle(r'Projects\Final project\data\pytrends_top_places_2021.pkl')

# Hotel occupancy rate and international arrivals data

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