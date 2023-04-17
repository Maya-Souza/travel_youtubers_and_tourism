import pandas as pd

# cleaning libraries
from src import cleaning_and_nlp as cleaning

# youtube and pytrends apis
from src import api

# viz libraries
from src import viz
import matplotlib.pyplot as plt

# youtube api libraries
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


###### LOADING DATAFRAMES #######

### Loading previously extracted Youtube data

# channel_stats = pd.read_pickle(r'Projects\Final project\data\channel_stats.pkl')
# videos_info = pd.read_pickle(r'Projects\Final project\data\video_info.pkl')
# places_per_year_by_channel = pd.read_pickle(r'Projects\Final project\data\places_per_year_by_channel.pkl')
# places_per_year_filtered = pd.read_pickle(r'Projects\Final project\data\places_year_filtered_notuple.pkl')
# places_mentions_views = pd.read_pickle(r'Projects\Final project\data\all_places_views_per_year')

### Loading previously extracted Google trends data

# pytrends_concat = pd.read_pickle(r'./data/pytrends_concat.pkl')
# pytrends_related_concat = pd.read_pickle(r'./data/pytrends_related_concat.pkl')
# videos_trends_merged = pd.read_pickle(r'./data/videos_trends_merged.pkl')

### Loading previously downloaded international arrivals data

number_of_tourist_arrivals = pd.read_pickle('Projects\Final project\data\international-tourism-number-of-arrivals.pkl')

##########################################################################################################################


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

##################### YOUTUBE API AND NLP #######################

# Getting the info from Youtube
channel_stats = api.get_channel_stats(youtube, channel_ids)
videos_info = api.creating_info_df(youtube, channel_stats)

# Pre-processing of the Youtube data (cleaning and entity recognition)
cleaning.deleting_emojis(videos_info)
cleaning.cleaning_dfs(videos_info)
cleaning.extracting_places(videos_info)

# Creating a new dataframe with the count for how many times each place was mentioned in each year
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
    

################################ GOOGLE TRENDS API ###############################


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

# Creating 2 complete dataframes instead of 16 separate ones

pytrends_list = [pytrends_pakistan, pytrends_india, pytrends_thailand,
                 pytrends_california, pytrends_tabriz, pytrends_mexico, pytrends_arizona]

pytrends_related_list = [pytrends_thailand_related,pytrends_india_related, pytrends_pakistan_related,
                        pytrends_california_related,
                         pytrends_tabriz_related, pytrends_mexico_related, pytrends_arizona_related]
                 
pytrends_concat = pd.concat(pytrends_list, axis = 1)

pytrends_related_concat = pd.concat(pytrends_related_list, axis = 1)

pytrends_concat.reset_index(inplace=True)
pytrends_related_concat.reset_index(inplace=True)

################################ TOURISM DATA ###############################

# Complementing missing data

# The values for California are domestic plus international arrivals - instead of just international like the countries analyzed

new_rows = pd.DataFrame({'Entity' : ['California', 'California', 'California', 'California', 'Arizona', 'Arizona',
                        'Arizona', 'Arizona'],
           'Code' : ['USA-CA', 'USA-CA', 'USA-CA', 'USA-CA', 'USA-AZ', 'USA-AZ', 'USA-AZ', 'USA-AZ'],
            'Year': [2018, 2019, 2020, 2021, 2018, 2019, 2020, 2021],
            'International tourism, number of arrivals': [281400000, 286000000, 140600000, 213300000, 45400000, 46800000, 32100000, 
                                                          40900000]
           })

number_of_tourist_arrivals = pd.concat([new_rows, number_of_tourist_arrivals]).reset_index(drop=True)

new_rows = pd.DataFrame({'Entity' : ['Thailand', 'California', 'Mexico', 'India'],
           'Code' : ['THA', 'USA-CA', 'MEX', 'IND'],
            'Year': [2022, 2022, 2022, 2022],
            'International tourism, number of arrivals': [11500000, 259800000, 18400000, 6190000]
           })

number_of_tourist_arrivals = pd.concat([new_rows, number_of_tourist_arrivals]).reset_index(drop=True)

# Changing the values for Mexico to international tourists only. The data from world bank was not correct according to 
# the Mexico government's website
number_of_tourist_arrivals.at[2988,'International tourism, number of arrivals'] = 24284000
number_of_tourist_arrivals.at[41,'International tourism, number of arrivals'] = 31860000
number_of_tourist_arrivals.at[2,'International tourism, number of arrivals'] = 34070000
number_of_tourist_arrivals.at[2987,'International tourism, number of arrivals'] = 45000000
number_of_tourist_arrivals.at[2986,'International tourism, number of arrivals'] = 41300000

#Since there was only one value for Tabriz (in 2020) the scale of the plot was very weird, so I manually added
# the value 0 for the years in which there were no videos posted in order to fix the plot.

new_rows = pd.DataFrame({'places' : ['Tabriz', 'Tabriz'],
            'year': [2018, 2019],
            'mentions': [0, 0],
            'total_number_of_views': [0,0]
           })

places_mentions_views = pd.concat([new_rows, places_mentions_views]).reset_index(drop=True)


################################ VISUALIZATIONS ###############################

# Manipulations for merging dataframes before being able to plot the graphs

# Extracting the week, month and year from the dates so I can merge the trends with videos_info.
# Using the week so I don't lose too much info by having to calculate the average of an entire month.
# Also, there weren't videos posted in every single week and month of the year, so this will allow me to find only
# the intersection so that later I can check for correlation.

pytrends_concat['week'] = pytrends_concat['date'].dt.isocalendar().week
pytrends_concat['month'] = pytrends_concat['date'].dt.month
pytrends_concat['year'] = pytrends_concat['date'].dt.year
pytrends_concat.drop('isPartial', axis=1, inplace=True)
#pytrends_concat.columns = pytrends_concat.columns.str.lower()

pytrends_related_concat['week'] = pytrends_related_concat['date'].dt.isocalendar().week
pytrends_related_concat['month'] = pytrends_related_concat['date'].dt.month
pytrends_related_concat['year'] = pytrends_related_concat['date'].dt.year
pytrends_related_concat.drop('isPartial', axis=1, inplace=True)

trends_to_merge = pytrends_concat.groupby(['year','month','week']).mean()
trends_related_to_merge = pytrends_related_concat.groupby(['year','month','week']).mean()

# Creating a week column in my videos_info df too
videos_info['publishedAt'] = pd.to_datetime(videos_info['publishedAt'])
videos_info['week_published'] = videos_info['publishedAt'].dt.isocalendar().week

# Creating a new filtered df with only the videos mentioning the top 3 most viewed places in the last 5 years
searchfor = '|'.join(trends_to_merge.columns)

videos_to_merge = videos_info[videos_info['everywhere_string'].str.contains(searchfor)].copy() 

# Many videos mentioned more than one place. Here I'm creating a new column with only
# the place that is the object of my analysis (one of the 3 most viewed in each year).
# I'm doing this so it becomes easier to group the info by place and compare it with the trends results
# as well as to plot the correlation heatmap.
import re

the_place = []

for i, row in videos_to_merge.iterrows():
    try:
        result = re.search(searchfor, row['everywhere_string'])
        the_place.append(result.group(0))
    
    except:
        the_place.append(None)
    
videos_to_merge['the_place'] = the_place

# Grouping by week and place and calculating the total of views.
videos_to_merge = pd.DataFrame(videos_to_merge.groupby(
                  ['year_published','month_published','week_published', 'the_place'])['viewCount'].sum()).reset_index()

# Merging the videos df and the google trends df.
videos_trends_merged = pd.merge(pd.merge(
                       videos_to_merge, trends_to_merge, 
                       left_on = ["year_published", "month_published", "week_published"],
                       right_on = ["year", "month", "week"]), 
                       trends_related_to_merge, 
                       left_on = ["year_published", "month_published", "week_published"],
                       right_on = ["year", "month", "week"])

videos_trends_merged.rename(columns={'viewCount': 'total_weekly_views'}, inplace=True)

# Capitalizing the columns
videos_trends_merged.columns = videos_trends_merged.columns.str.title()

# Most mentioned x most viewed places
top_5_places_views_mentions_2018 = viz.general_data(2018,places_mentions_views)
top_5_places_views_mentions_2018.show()

top_5_places_views_mentions_2019 = viz.general_data(2019,places_mentions_views)
top_5_places_views_mentions_2019.show()

top_5_places_views_mentions_2020 = viz.general_data(2020, places_mentions_views)
top_5_places_views_mentions_2020.show()

top_5_places_views_mentions_2021 = viz.general_data(2021, places_mentions_views)
top_5_places_views_mentions_2021.show()

top_5_places_views_mentions_2022 = viz.general_data(2022, places_mentions_views)
top_5_places_views_mentions_2022.show()

# Views x google trends results

thai = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'Thailand')
thai.write_image(r".\images\graphs\thai.png")
thai.show()

pakistan = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'Pakistan')
pakistan.write_image(r".\images\graphs\pakistan.png")
pakistan.show()

tabriz = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'Tabriz')
tabriz.write_image(r".\images\graphs\tabriz.png")
tabriz.show()

mexico = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'Mexico')
mexico.write_image(r".\images\graphs\mexico.png")
mexico.show()

india = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'India')
india.write_image(r".\images\graphs\india.png")
india.show()

california = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'California')
california.write_image(r".\images\graphs\california.png")
california.show()

arizona = viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, 'Arizona')
arizona.write_image(r".\images\graphs\arizona.png")
arizona.show()


# Correlation heatmap of views and google trends results

viz.sns_correlation_heatmap(videos_trends_merged, "Pakistan")
plt.savefig(r".\images\graphs\pakistan_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Pakistan", years = [2018, 2019])
plt.savefig(r".\images\graphs\pakistan_specific_years_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Arizona")
plt.savefig(r".\images\graphs\arizona_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Arizona", years = [2021])
plt.savefig(r".\images\graphs\arizona_specific_years_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Thailand")
plt.savefig(r".\images\graphs\thailand_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Mexico")
plt.savefig(r".\images\graphs\mexico_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "Mexico", years = [2018, 2022])
plt.savefig(r".\images\graphs\mexico_specific_years_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "India")
plt.savefig(r".\images\graphs\india_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "India", years = [2019, 2020, 2022])
plt.savefig(r".\images\graphs\india_specific_years_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "California")
plt.savefig(r".\images\graphs\california_heatmap.png", bbox_inches="tight")

viz.sns_correlation_heatmap(videos_trends_merged, "California", years = [2021])
plt.savefig(r".\images\graphs\california_specific_years_heatmap.png", bbox_inches="tight")

# Views x tourist arrivals

thai_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'Thailand')
thai_tourism.write_image(r".\images\graphs\thai_tourism.png")
thai_tourism.show()

pakistan_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'Pakistan')
pakistan_tourism.write_image(r".\images\graphs\pakistan_tourism.png")
pakistan_tourism.show()

india_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'India')
india_tourism.write_image(r".\images\graphs\india_tourism.png")
india_tourism.show()

mexico_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'Mexico')
mexico_tourism.write_image(r".\images\graphs\mexico_tourism.png")
mexico_tourism.show()

california_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'California')
california_tourism.write_image(r".\images\graphs\california_tourism.png")
california_tourism.show()

arizona_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'Arizona')
arizona_tourism.write_image(r".\images\graphs\arizona_tourism.png")
arizona_tourism.show()

tabriz_tourism = viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, 'Tabriz')
tabriz_tourism.write_image(r".\images\graphs\tabriz_tourism.png")
tabriz_tourism.show()

