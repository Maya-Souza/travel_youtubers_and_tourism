import pandas as pd
import numpy as np
# viz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

###########################################

# Most mentioned places X Most views per place

def general_data(year, places, option=2):

    '''
    Function that returns a plot (bar and line) showing the number of mentions and the total views
    for the top 5 most mentioned places in the videos.

    :params:
        year(int) = the video publication year to be analysed
        places(df) = a dataframe with all the places mentioned accross all the videos analysed

    :returns:
        a fig 
    '''
    #fig = make_subplots(rows=1, cols=2)

    if option == 1:
        top_views = places[places['year'] == year][:7]
    else:
        top_views = places[places['year'] == year][:5]    
    
    trace3 = go.Scatter(
                    mode="lines",
                    x = top_views['top_places_'],
                    y = top_views['mentions'],
                    name='Number of mentions',
                    marker = dict(color = 'black')
                    
    )
    
    trace4 = go.Bar(
                    x = top_views['top_places_'],
                    y = top_views['total_number_of_views'],
                    name='Number of views',
                    marker = dict(color = '#04cad8')
                    
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(trace3, secondary_y=True,)
    fig.add_trace(trace4)
            
    if option == 1:
                fig['layout'].update(height = 700, width = 1200, 
                                title = f"{year}'s top places in number of views <br><sup>Ranking order is not necessarily the same for mentions</sup>",
                                xaxis=dict(tickangle=-45),
                                xaxis_title="Top places",
                                yaxis_title="Number of mentions",
                                yaxis2_title="Total views in millions",
                                plot_bgcolor='rgba(240, 242, 247, 0.8)',
                                legend=dict(
                                            yanchor="bottom",
                                            y=0.8,
                                            xanchor="right",
                                            x=0.9
                                        ))
    else:
        fig['layout'].update(height = 700, width = 1200, 
                                title = f"{year}'s top places in number of views <br><sup>Ranking order is not necessarily the same for mentions</sup>",
                                xaxis=dict(tickangle=0),
                                xaxis_title="Top places",
                                yaxis_title="Number of mentions",
                                yaxis2_title="Total views in millions",
                                plot_bgcolor='rgba(240, 242, 247, 0.8)',
                                legend=dict(
                                            yanchor="bottom",
                                            y=0.8,
                                            xanchor="right",
                                            x=0.9
                                        ))


    return fig

    ##################################################

# Videos mentioning a place X Google trends interest over time for the same place

def plotting_trends_videos(trends, videos_info, place, year):

    '''
    Function that plots all the videos mentioning a certain place in a given year and
    the Google trends interest over time results for the same place in the same year.

    :params:
        trends(df) = google trends df
        videos_info(df) = a df created using the yt API with all the info about all the videos analysed (year published, view count, etc)
        place(str) = the place to be plotted
        year(int) = the year to be analysed

    :returns:
        a fig
    '''

    select = videos_info.loc[(videos_info['everywhere_string'].str.contains(f"{place}")) & 
                             (videos_info['year_published'] == year)]

    trace1 = go.Line(
        x = trends['date'],
        y = trends[place],
        name= f'<b>Google trends results for {place}',
        marker=dict(
            color= 'black'#'rgb(34,163,192)'
                   )
    )
    trace2 = go.Scatter(
        x=select['publishedAt'],
        y=select['viewCount'],
        name='Videos posted by <b> number of views',
        yaxis='y2',
        mode = 'markers',
        marker = dict(size=8,
                      symbol = 'diamond-dot',
                      color = '#04cad8')#'rgba(190, 167, 9, 0.8)')

    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(trace1)
    fig.add_trace(trace2, secondary_y=True)
    
    fig['layout'].update(#height = 600, width = 1000, 
                         title = f"Google Trends results for '{place}' x <br>Views for videos that mention '{place}'",
                         title_y = 0.99,
                         title_x = 0.15,
                         xaxis=dict(tickangle=-45),
                        #xaxis_title="Date",
                        yaxis_title="Google trends - interest over time",
                        yaxis2_title="Number of views per video in millions",
                        plot_bgcolor='rgba(240, 242, 247, 0.8)',
                        legend=dict(
                                    #yanchor="bottom",
                                    y=-0.5,
                                    #xanchor="left",
                                    x=-0.1,
                                    font_size = 10

                                ),
                        font = dict(size=10))
                        #,legend_title="Legend")
    
    fig.update_xaxes(minor=dict(ticklen=6, tickcolor="black", showgrid=True))
    fig.update_layout(width=1100,height=900)
    
    return fig
    
    ##################################################

# Number of views per place over time X Number of tourist arrivals over time

def plotting_tourism_data (places_mentions_views, number_of_tourist_arrivals, place):

    '''
    Function that plots the video info (total number of views) and number of tourist arrivals
    for each place.

    :params:
        places_mentions_views(df) = a df with all the places mentioned in all the videos, the total number of mentions
        and the total number of views for each along the years
        tourism_info(df) = df with the number of tourist arrivals for many different countries
    
    :returns:
        a fig
    '''
    
    #place = input('Type the place \n')
    
    views = places_mentions_views.loc[(places_mentions_views['top_places_']==place) & ((places_mentions_views['year']>=2018))]
    
    arrivals = number_of_tourist_arrivals.loc[(number_of_tourist_arrivals['Entity'] == place) 
                                             & (number_of_tourist_arrivals['Year']>=2018)]
    
        
    fig = make_subplots(#rows=1, cols=2, 
                    specs=[[{"secondary_y": True}]])    
    
    trace1 = go.Line(
                    #mode = 'lines',
                    x = views['year'],
                    y = views['total_number_of_views'],
                    name= f'Total number of views',
                    yaxis='y2',
                    line = dict(width = 2),
                    marker=dict(
                                color='black',#rgb(34,163,192)
                                line = dict(width = 2, color='black')
                                )
    )

    trace2 = go.Bar(
                    x = arrivals['Year'],
                    y = arrivals['International tourism, number of arrivals'],
                    name='Number of tourists arriving',
                    marker = dict(color = '#04cad8')#rgba(221, 206, 103, 0.8)
    )

    
    fig.add_trace(trace1, secondary_y=True)
    fig.add_trace(trace2)
    

    fig['layout'].update(height = 600, width = 1000, 
                         title = f"Tourist arrivals in '{place}' x <br>Views for videos mentioning '{place}'",
                         xaxis=dict(tickangle=0, type = 'category', categoryorder='array', 
                                    categoryarray = ['2018', '2019', '2020', '2021']),
                         xaxis_title="Year",
                         yaxis2_title="Total views in millions",
                         yaxis_title="Number of arrivals in millions",
                         plot_bgcolor='rgba(240, 242, 247, 0.8)',
                         legend=dict(
                                    #yanchor="bottom",
                                    y=-0.5,
                                    #xanchor="left",
                                    x=-0.1,
                                    font_size = 10
                                ))
                        #,legend_title="Legend")

    fig.update_yaxes(minor=dict(ticklen=6, tickcolor="black", showgrid=True, nticks=3))
    

    return fig
    ##################################################

def correlation_heatmap(merged_df, place):
    
    x_cor = merged_df[['total_number_of_views', 'tourist_arrivals', 'google_trends']].corr()

    fig=go.Figure()

    fig.add_trace(go.Heatmap(
    x = x_cor.columns,
    y = x_cor.index,
    z = np.array(x_cor),
    colorscale=px.colors.diverging.RdBu,
    zmin=-1,
    zmax=1
    ))

    fig['layout'].update(height = 600, width = 1000, 
                         title = f"Correlation between '{place}' videos x <br>Google trends results x Tourist arrivals",
                         title_x = 0.5,
                         plot_bgcolor='rgba(240, 242, 247, 0.8)')
                         

    return fig

    ##################################################

    