import pandas as pd
import numpy as np
import os
import requests
import pickle

import isodate
from datetime import datetime
import time

from dotenv import load_dotenv 
load_dotenv()

# youtube api
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# pytrends api
from pytrends.request import TrendReq

##################################################################

def creating_info_df(youtube, channel_data):
    
    ''' Create a dataframe with video statistics from all channels'''

    video_df = pd.DataFrame()
    comments_df = pd.DataFrame()

    for c in channel_data['channelName'].unique():
        print("Getting video information from channel: " + c)
        playlist_id = channel_data.loc[channel_data['channelName']== c, 'playlistId'].iloc[0]
        video_ids = get_video_ids(youtube, playlist_id)

        # get video data
        video_data = get_video_details(youtube, video_ids)        

        # append video data together
        video_df = video_df.append(video_data, ignore_index=True)

    return video_df

##################################################################

def get_channel_stats(youtube, channel_ids):

    """
    Get channel stats
    
    Params:
    ------
    youtube: build object of Youtube API
    channel_ids: list of channel IDs
    
    Returns:
    ------
    dataframe with all channel stats for each channel ID
    
    """
    
    all_data = []
    
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    # loop through items
    for item in response['items']:
        data = {'channelName': item['snippet']['title'],
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'totalVideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
        }
        
        all_data.append(data)
        
    all_data = pd.DataFrame(all_data)
    
    numeric_cols = ['subscribers', 'views', 'totalVideos']
    all_data[numeric_cols] = all_data[numeric_cols].apply(pd.to_numeric, errors='coerce')
        
    return(all_data)

##################################################################

def get_video_ids(youtube, playlist_id):
    """
    Get list of video IDs of all videos in the given playlist
    Params:
    
    youtube: the build object from googleapiclient.discovery
    playlist_id: playlist ID of the channel
    
    Returns:
    List of video IDs of all videos in the playlist
    
    """
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids

##################################################################
    
def get_video_details(youtube, video_ids):
    
    """
    Get video statistics of all videos with given IDs
    Params:
    
    youtube: the build object from googleapiclient.discovery
    video_ids: list of video IDs
    
    Returns:
    Dataframe with statistics of videos, i.e.:
        'channelTitle', 'title', 'description', 'tags', 'publishedAt'
        'viewCount', 'likeCount', 'favoriteCount', 'commentCount'
        'duration', 'caption'(boolean)
    """
        
    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {
                             'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'commentCount'],
                             'contentDetails': ['duration', 'caption']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
            
    return pd.DataFrame(all_video_info)

##################################################################

# pytrends API

def getting_google_trends(places_df, year):
    
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = []
    
    for idx, row in places_df.iterrows():
        if row['year'] == year:
            
            for i in row['views_per_place']:

                kw_list.append(i[0])
               
            pytrends.build_payload(kw_list, timeframe=f'{year}-1-1 {year}-12-31')
                
    return pytrends.interest_over_time()

##################################################################

