import pandas as pd
import numpy as np

# viz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

###########################################

# Most mentioned places X Most views per place

def general_data(year, places):

    '''
    Function that returns a plot (bar and line) showing the number of mentions and the total views
    for the top 5 most mentioned places in the videos.

    :params:
        year(int) = the video publication year to be analysed
        places(df) = a dataframe with all the places mentioned accross all the videos analysed

    :returns:
        a fig 
    '''
    
    top_views = places[places['year'] == year][:5]    
    
    trace3 = go.Scatter(
                    mode="lines",
                    x = top_views['places'],
                    y = top_views['mentions'],
                    name='Number of mentions',
                    marker = dict(color = 'black')
                    
    )
    
    trace4 = go.Bar(
                    x = top_views['places'],
                    y = top_views['total_number_of_views'],
                    name='Number of views',
                    marker = dict(color = '#cf5c49')
                    
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(trace3, secondary_y=True,)
    fig.add_trace(trace4)
    
    fig['layout'].update(height = 600, width = 1000, 
                         title = f"{year}'s top 5 places in number of views <br><sup>Ranking order is not necessarily the same for mentions</sup>",
                         xaxis=dict(tickangle=0),
                         xaxis_title="Top 5 places",
                         yaxis_title="Total number of views",
                         yaxis2_title="Number of mentions",
                         plot_bgcolor='rgba(240, 242, 247, 0.8)')


    return fig

    ##################################################


def plotting_trends_videos(trends, trends_related, videos_info, place):

    '''
    Function that plots all the videos mentioning a certain place in a given year and
    the Google trends interest over time results for the same place in the same year.

    :params:
        trends (df) = google trends df
        trends_related (df) = google trends df with the "travel place" and "flight place" results
        videos_info (df) = a df created using the yt API with all the info about all the videos analysed (year published, view count, etc)
        place (str) = the place to be plotted

    :returns:
        a fig
    '''
    
    # selecting only the videos that mention the place being analyzed in the last 5 years
    
    select = videos_info.loc[(videos_info['everywhere_string'].str.contains(f"{place}")) & 
                             (videos_info['year_published'] >= 2018)]
    
    # selecting the same place from the google trends df 
    
    select2 = trends[['date', f"{place}"]].loc[trends['date']<'2023-1-1']
        
    # selecting the results for the same place from the google trends related df (results for flight+place and travel+place) 

    select3 = trends_related[["date", f"travel {place.lower()}", f"flight {place.lower()}"]].loc[trends_related['date']<'2023-1-1']
    
    trace1 = go.Scatter(
        x = select2['date'],
        y = select2[place],
        name= f"''{place}''- Interest over time",
        mode = 'lines'
    )
    
    trace2 = go.Scatter(
        x = select3['date'],
        y = select3[f"travel {place.lower()}"],
        name= f"''travel {place}''- Interest over time",
        mode = 'lines'
    )
    
    trace3 = go.Scatter(
        x = select3['date'],
        y = select3[f"flight {place.lower()}"],
        name= f"''flight {place}'' - Interest over time",
        mode = 'lines'
    )
    
    trace4 = go.Scatter(
        x=select['publishedAt'],
        y=select['viewCount'],
        name='Videos posted by number of views',
        yaxis='y2',
        mode = 'markers',
        marker = dict(size=4,
                      color = '#60585a')
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(trace1)
    fig.add_trace(trace2)
    fig.add_trace(trace3)
    fig.add_trace(trace4, secondary_y=True)
    
    fig['layout'].update(height = 600, width = 1000, 
                         title = f"Google Trends results for '{place}' x Views on YouTube for videos that mention '{place}'",
                         xaxis=dict(tickangle=-45),
                         xaxis_title="Date",
                         yaxis_title="Google trends - interest over time",
                         yaxis2_title="Number of views per video",
                         plot_bgcolor= 'rgba(240, 242, 247, 0.8)')
    
    fig.update_xaxes(minor=dict(ticklen=6, tickcolor="black", showgrid=True),
                     rangeslider_visible=True,
                     rangeselector=dict(
                     buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all")
                    ])
    
    ),
        rangeslider_thickness = 0.15,
        range = ('2018-01-01', '2022-12-01'),
        rangeslider_range = ('2018-01-01', '2022-12-01')
    )
    
    return fig
    
    ##################################################

# Number of views per place over time X Number of tourist arrivals over time

def plotting_tourism_data (places_mentions_views, tourism_info, place):

    '''
    Function that plots the video info (total number of views) and number of tourist arrivals
    for each place.

    :params:
        places_mentions_views(df) = a df with all the places mentioned in all the videos, the total number of mentions
        and the total number of views for each along the years
        tourism_info(df) = df with the number of tourist arrivals for many different places
    
    :returns:
        a fig
    '''

    views = places_mentions_views.loc[(places_mentions_views['places']==place) & (places_mentions_views['year']>=2018)]
    
    arrivals = number_of_tourist_arrivals.loc[(number_of_tourist_arrivals['Entity'] == place) 
                                             & (number_of_tourist_arrivals['Year']>=2018)]
    
        
    fig = make_subplots(#rows=1, cols=2, 
                    specs=[[{"secondary_y": True}]])    
    
    trace1 = go.Scatter(
                    mode = 'lines',
                    x = views['year'],
                    y = views['total_number_of_views'],
                    name= f'Total number of YouTube views for {place}',
                    yaxis='y2',
                    line = dict(width = 2),
                    marker=dict(
                                color='black'
                                line = dict(width = 2, color='black')
                                )
    )

    trace2 = go.Bar(
                    x = arrivals['Year'],
                    y = arrivals['International tourism, number of arrivals'],
                    name='Number of tourists arriving',
                    marker = dict(color = '#cf5c49')
    )

    
    fig.add_trace(trace1, secondary_y=True)
    fig.add_trace(trace2)
    

    fig['layout'].update(height = 600, width = 1000, 
                         title = f"Tourist arrivals in '{place}' x Views on YouTube for videos mentioning '{place}'",
                         xaxis=dict(tickangle=0, type = 'category', categoryorder='array', 
                                    categoryarray = ['2018', '2019', '2020', '2021', '2022']),
                         xaxis_title="Year",
                         yaxis2_title="Total views in millions",
                         yaxis_title="Number of arrivals in millions",
                         plot_bgcolor='rgba(240, 242, 247, 0.8)')
                        

    fig.update_yaxes(minor=dict(ticklen=6, tickcolor="black", showgrid=True, nticks=3))
    

    return fig

    ##################################################

    def sns_correlation_heatmap(merged_df, place, years = 'all'):
    '''
    Creates a correlation matrix heatmap of weekly google trends results and
    the sum of weekly youtube views of videos mentioning each place. Takes into consideration
    only the weeks in which videos were posted.
    
    :params:
    merged_df (df) = the videos_trends_merged dataframe
    place (str) = name of the place
    years (list) = optional parameter, if not used defaults to 'all', otherwise gathers info from
    views and trends for specific years
    
    :returns:
    figure
    
    '''
    # checking the correlation in the 5 last years
    if years == 'all':
        
        corr = merged_df[['Total_Weekly_Views', f'{place}', f'Flight {place}', f'Travel {place}']].corr()

        # Getting the Upper Triangle of the correlation matrix
        matrix = np.triu(corr)

        # using the upper triangle matrix as mask 
        fig = sns.heatmap(corr, annot=True, mask=matrix, cmap = sns.light_palette("#cf5c49", as_cmap=True))
        plt.xticks(rotation=-45)
        plt.suptitle(f'Correlation between Google Trends results and \nweekly YouTube views for videos mentioning {place}',
                     fontsize = 12, y = 1.1)
        return fig
    
    # checking the correlation only in the years in which the place was the most viewed
    else:
        
        corr = merged_df[merged_df['Year_Published'].isin(years)]
        corr = corr[['Total_Weekly_Views', f'{place}', f'Flight {place}', f'Travel {place}']].corr()

        # Getting the Upper Triangle of the correlation matrix
        matrix = np.triu(corr)

        # using the upper triangle matrix as mask 
        fig = sns.heatmap(corr, annot=True, mask=matrix, cmap = sns.light_palette("#cf5c49", as_cmap=True))
        plt.xticks(rotation=-45)
        plt.suptitle(f'Correlation between Google Trends results and \nweekly YouTube views for videos mentioning {place} in {years}',
                     fontsize = 12, y = 1.1)
        
        return fig
    
    ##################################################

    def correlation_heatmap_tourism(tourism_df, views_df, place):
    '''
    Calculates the Pearson correlation parameter between the number of tourist arrivals
    and number of youtube views. Returns a simple square figure with the parameter in the middle
    along with a title.
    
    '''
    select1 = views_df[views_df['places']==place]
    select2 = tourism_df[tourism_df['Entity']==place]
    
    corr = select1.merge(select2, left_on='year', right_on='Year')[
            ['total_number_of_views', 'International tourism, number of arrivals']].corr()

    

    # Getting the Upper Triangle of the co-relation matrix
    matrix = np.triu(corr)
    
    # using the upper triangle matrix as mask 
    fig = sns.heatmap(corr, annot=True, mask=matrix, cmap = sns.light_palette("#cf5c49", as_cmap=True), 
                yticklabels=False, xticklabels=False, cbar=False)
    
    plt.xticks(rotation=-45)
    plt.suptitle(f'Correlation between tourist arrivals \nper year and YouTube views for \nvideos mentioning {place}',
                 fontsize = 12, y = 0.8, x = 0.34, ha='center')
    
    return fig