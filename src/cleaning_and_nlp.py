import pandas as pd
import numpy as np
import os
import requests
import pickle

import isodate
from datetime import datetime
import time

# text recognition
import nltk
import spacy
import locationtagger
import re
import itertools

# different operators
from collections import Counter
from operator import itemgetter

def cleaning_dfs(video_df):
    
    # convert count columns to numeric
    numeric_cols = ['viewCount', 'likeCount', 'commentCount']
    video_df[numeric_cols] = video_df[numeric_cols].apply(pd.to_numeric, errors = 'coerce', axis = 1)

    # convert duration to minutes
    video_df['duration_minutes'] = video_df['duration'].apply(lambda x: isodate.parse_duration(x).seconds // 60)
    
    # convert date from ISO format and isolate year, month and day
    pd.to_datetime(video_df['publishedAt'])
    video_df['year_published'] = pd.DatetimeIndex(video_df['publishedAt']).year
    video_df['month_published'] = pd.DatetimeIndex(video_df['publishedAt']).month
    video_df['day_published'] = pd.DatetimeIndex(video_df['publishedAt']).day

#######################################################

def deleting_emojis(video_df):
    
    video_df['title'] = video_df['title'].str.replace('[^\w\s#@/:%.,_-]', '', regex=True, flags=re.UNICODE).str.replace('#', '',)
    video_df['title'] = video_df['title'].map(lambda x: x.lower() if isinstance(x,str) else x)
    
    video_df['description'] = video_df['description'].str.replace('[^\w\s#@/:%.,_-]', '', regex=True, flags=re.UNICODE).str.replace('#', '',)
    video_df['description'] = video_df['description'].map(lambda x: x.lower() if isinstance(x,str) else x)
    
    video_df['tags'] = video_df['tags'].astype(str).str.replace('[^\w\s#@/:%.,_-]', '', regex=True, flags=re.UNICODE).str.replace('#', '',)
    video_df['tags'] = video_df['tags'].map(lambda x: x.lower() if isinstance(x,str) else x)

#######################################################

def extracting_places(video_df):
    
    places_title = []
    places_tags = []
    places_description = []
    all_countries = []
    all_cities = []
    all_regions = []
    
    for index, row in video_df.iterrows():
        
        # extracting entities
        if row['title']:
            place_entity_title = locationtagger.find_locations(text = str(row['title']))
            
        else:
            place_entity_title = locationtagger.find_locations(text = 'none')


        if row['tags']:
            place_entity_tags = locationtagger.find_locations(text = str(row['tags']))
            
        else:
            place_entity_tags = locationtagger.find_locations(text = 'none')
          
        if row['description']:
            place_entity_description = locationtagger.find_locations(text = str(row['description']))
        
        else:
            place_entity_description = locationtagger.find_locations(text = 'none')

#         getting all countries, states and/or cities
#         places_title.append({'countries': place_entity_title.countries,
#                         'states': place_entity_title.regions,
#                         'cities': place_entity_title.cities})
        
#         places_tags.append({'countries': place_entity_tags.countries,
#                         'states': place_entity_tags.regions,
#                         'cities': place_entity_tags.cities})
        
#         places_description.append({'countries': place_entity_description.countries,
#                         'states': place_entity_description.regions,
#                         'cities': place_entity_description.cities})
            
        all_countries.append([place_entity_title.countries, place_entity_tags.countries, place_entity_description.countries])
        all_cities.append([place_entity_title.cities, place_entity_tags.cities, place_entity_description.cities])
        all_regions.append([place_entity_title.regions, place_entity_tags.regions, place_entity_description.regions])
        
        print(index)
        
#     video_df['places_title'] = places_title
#     video_df['places_tags'] = places_tags
#     video_df['places_description'] = places_description
    
    for i in range(len(all_countries)):
        
        all_countries[i] = list(set(itertools.chain(*all_countries[i])))  
        all_cities[i] = list(set(itertools.chain(*all_cities[i])))
        all_regions[i] = list(set(itertools.chain(*all_regions[i])))
        
    video_df['all_countries'] = all_countries
    video_df['all_cities'] = all_cities
    video_df['all_regions'] = all_regions
    
    video_df['everywhere'] = (video_df['all_countries'] + video_df['all_cities'] + video_df['all_regions'])
    video_df['everywhere'] = video_df['everywhere'].apply(lambda x: list(pd.Series(x).str.capitalize().unique()) if x else None)

#######################################################

def deleting_biased_places(videos_info, to_delete, query, channel_title, year_):
    
    if query == 1:
        
        for idx, row in videos_info.iterrows():
            
            if ((row['channelTitle'] == channel_title) & (row['everywhere'] != None)):
                
                for i in to_delete:
                    
                    if (i in row['everywhere']):

                        row['everywhere'].remove(i)
    
    else:
        for idx, row in videos_info.iterrows():
            
            if ((row['channelTitle'] == channel_title) & (row['year_published'] >= year_) & (row['everywhere'] != None)):
                
                for i in to_delete:
                    
                    if (i in row['everywhere']):

                        row['everywhere'].remove(i)

#######################################################

def counting_ocurrences_places(video_df):

    # I didn't get only the top 3 or 4 places automatically because the entitity recognition library is not very
    # precise and I needed to select by hand which places are real places and which are a possible mistake from the 
    # locationtagger library
    
    everywhere = []
    all_countries = []
    all_cities = []
    all_regions = []
    places_per_year = pd.DataFrame()

    cities = []
    everywhere_ = []
    countries = []
    regions = []
    year = []

    for i in range(video_df['year_published'].min(), video_df['year_published'].max()+1):

        vd = video_df.loc[video_df['year_published']==i]

        for j in range(len(vd["everywhere"])):

            if vd["everywhere"].iloc[j]:
                everywhere += vd["everywhere"].iloc[j] 

            if vd["all_countries"].iloc[j]:
                all_countries += vd["all_countries"].iloc[j]

            if vd["all_cities"].iloc[j]:
                all_cities += vd["all_cities"].iloc[j]

            if vd["all_regions"].iloc[j]:
                all_regions += vd["all_regions"].iloc[j]
        
        year.append(i)
        countries.append(Counter(all_countries).most_common())
        cities.append(Counter(all_cities).most_common())
        regions.append(Counter(all_regions).most_common())
        everywhere_.append(Counter(everywhere).most_common())
        
        everywhere = []
        all_countries = []
        all_cities = []
        all_regions = []
        
    places_per_year['year'] = year
    places_per_year['countries'] = countries
    places_per_year['cities'] = cities
    places_per_year['regions'] = regions
    places_per_year['everywhere'] = everywhere_

        
    return places_per_year

#######################################################

def counting_ocurrences_places_by_channel(video_df):

    # I didn't get only the top 3 or 4 places automatically because the entitity recognition library is not very
    # precise and I needed to select by hand which places are real places and which are a possible mistake from the 
    # locationtagger library
    
    everywhere = []
    all_countries = []
    all_cities = []
    all_regions = []
    places_per_year = pd.DataFrame()

    cities = []
    everywhere_ = []
    countries = []
    regions = []
    year = []
    channel = []

    for c in video_df['channelTitle'].unique():
        df = video_df.loc[video_df['channelTitle']==c]
        
        for i in range(df['year_published'].min(), df['year_published'].max()+1):

            vd = df.loc[df['year_published']==i]

            for j in range(len(vd["everywhere"])):

                if vd["everywhere"].iloc[j]:
                    everywhere += vd["everywhere"].iloc[j] 

                if vd["all_countries"].iloc[j]:
                    all_countries += vd["all_countries"].iloc[j]

                if vd["all_cities"].iloc[j]:
                    all_cities += vd["all_cities"].iloc[j]

                if vd["all_regions"].iloc[j]:
                    all_regions += vd["all_regions"].iloc[j]

            
            channel.append(c)
            year.append(i)
            countries.append(Counter(all_countries).most_common())
            cities.append(Counter(all_cities).most_common())
            regions.append(Counter(all_regions).most_common())
            everywhere_.append(Counter(everywhere).most_common())
            
            everywhere = []
            all_countries = []
            all_cities = []
            all_regions = []
        
    places_per_year['channel'] = channel
    places_per_year['year'] = year
    places_per_year['countries'] = countries
    places_per_year['cities'] = cities
    places_per_year['regions'] = regions
    places_per_year['everywhere'] = everywhere_

        
    return places_per_year
#######################################################

def organizing_places_per_channel_df(places_per_year_by_channel):

    places1 = []
    mentions = []
    channel = []
    year = []
    aux = pd.DataFrame()

    for idx, row in places_per_year_by_channel.iterrows():
        
        for c in row['channel'].unique():
            
            for i in row['top_places']:

                channel.append(c)
                year.append(row['year'])
                places1.append(i[0])
                mentions.append(i[1])

        for j in row['views_per_place']:
            if row['year'] == year:

                places2.append(j[0])
                n_views.append(j[1])
                
    aux['top_places_'] = places1
    aux['mentions'] = mentions
    aux['total_number_of_views'] = n_views
    aux['year'] = year
    aux
    
    return aux.sort_values(by = ['total_number_of_views'], ascending=False)

#######################################################

def get_views_per_top_place(video_df, places_df):
    
    views = 0
    total_views_per_place = []
    total_views_per_place2 = []
  
    for idx, row in places_df.iterrows():
        for place in row['top_places']:

            for idx2, row2 in video_df.iterrows():

                if row2['year_published'] == row['year']:

                    if (row2['everywhere'] != None):
                        if (place[0] in row2['everywhere']):
                            views += row2['viewCount']

            total_views_per_place.append((place[0], views))
            views = 0


        total_views_per_place2.append(total_views_per_place)
        total_views_per_place = []

    places_df['views_per_place'] = total_views_per_place2
        
    return places_df

#######################################################

def organizing_places_views_df(places_per_year_filtered, year):

    places1 = []
    mentions = []
    places2 = []
    n_views = []
    aux = pd.DataFrame()

    for idx, row in places_per_year_filtered.iterrows():
        for i in row['top_places']:
            if row['year'] == year:

                places1.append(i[0])
                mentions.append(i[1])

        for j in row['views_per_place']:
            if row['year'] == year:

                places2.append(j[0])
                n_views.append(j[1])
                
    aux['top_places_'] = places1
    aux['mentions'] = mentions
    aux['total_number_of_views'] = n_views
    aux['year'] = year
    
    return aux.sort_values(by = ['total_number_of_views'], ascending=False)

#######################################################

