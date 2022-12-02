import pandas as pd

# viz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# streamlit
import streamlit as st
st.set_page_config(layout="wide")
import streamlit.components.v1 as components

#from pathlib import Path
#import sys


#sys.path.append(str(Path(__file__).resolve().parent.parent))

# plotting functions files
from src import viz


# youtube data
videos_info = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\video_info.pkl')
places_mentions_views = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\all_places_views_per_year.pkl')

# google trends data
pytrends_top_places_2018= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2018.pkl')
pytrends_top_places_2019= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2019.pkl')
pytrends_top_places_2020 = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2020.pkl')
pytrends_top_places_2021= pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\pytrends_top_places_2021.pkl')

# tourist arrivals data
number_of_tourist_arrivals = pd.read_pickle(r'C:\Users\mayar\OneDrive\Área de Trabalho\Projects\Final project\data\international-tourism-number-of-arrivals.pkl')


################################################################################################


st.title('A data lover paradise: graphs!')
page_names = ["Places mentioned in the videos along the years", "Google trends for each place", "Videos posted by year x Tourist arrivals"]
page = st.radio('Choose where to go next', page_names)

if page == "Places mentioned in the videos along the years":

    st.markdown("\n \n \n")
    st.markdown("### Our first piece of information is the places that were mentioned in each video throughout the years.")
    st.markdown("On the map below we can see all the countries mentioned either on the title, description or tags of youtube videos in the span of 11 years. The darkest colored countries were mentioned the most.")
    
    col1, col2 = st.columns([2,1])
    
    with col1:
        html_temp = "<div class='tableauPlaceholder' id='viz1669920391950' style='position: relative'><noscript><a href='#'><img alt='Countries mentioned in the videos from 2010 to 2021 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlacesmentionedonYTvideos&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PlacesmentionedonYTvideos&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pl&#47;PlacesmentionedonYTvideos&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1669920391950');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
        components.html(html_temp, height=500) 
    with col2:
        st.markdown("\n \n \n \n")
        top10 =  places_mentions_views.groupby('top_places_').sum().sort_values(by = 'mentions', ascending=False).drop(columns='year')
        top10['total_number_of_views'] = top10['total_number_of_views'].astype('int')
        st.dataframe(top10, use_container_width=True)
    
    st.markdown("_It's important to mention that some of the YouTubers analysed live in Canada and posted many videos talking about this._")
    
    st.markdown("Below you can see graphs showing the top 5 most 'viewed' places, how many times they were mentioned and the total number of views of all the videos that mentioned each place.")

    st.markdown("The entire analysis was based on the top 3 places in number of views.")

    option = st.selectbox("Select the year:", 
                        (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 'From 2018 to 2021'))

    if option == 'From 2018 to 2021':

        col1, col2, col3 = st.columns([6,1,6])

        with col1:
            top_5_places_views_mentions_2018 = viz.general_data(2018,places_mentions_views)
            st.plotly_chart(top_5_places_views_mentions_2018, use_container_width=True, theme = 'streamlit')
        with col3:
            top_5_places_views_mentions_2019 = viz.general_data(2019,places_mentions_views)
            st.plotly_chart(top_5_places_views_mentions_2019, use_container_width=True, theme = 'streamlit')

        col3, col4, col5 = st.columns([6,1,6])

        with col3:
            top_5_places_views_mentions_2020 = viz.general_data(2020,places_mentions_views)
            st.plotly_chart(top_5_places_views_mentions_2020, use_container_width=True, theme = 'streamlit')
        with col5:
            top_5_places_views_mentions_2021 = viz.general_data(2021,places_mentions_views, 1)
            st.plotly_chart(top_5_places_views_mentions_2021, use_container_width=True, theme = 'streamlit')
        
        st.subheader("Comments/Conclusions")
        st.markdown("I decided to take into consideration the 3 most viewed places in each year since it's clear that number of mentions doesn't translate into views, and for this analysis the volume of people watching the videos matter the most.")

    else:
        top_5_places_views_mentions_x = viz.general_data(option,places_mentions_views)
        st.plotly_chart(top_5_places_views_mentions_x, theme = 'streamlit')

elif page == "Google trends for each place":

    st.markdown("\n \n \n")
    st.markdown("### Our second piece of information is the Google Trends data showing interest over time for each one of the top places mentioned in each year.")
    st.image(r'../streamlit_files/imgs/Google-Trends.png')
    st.markdown("The graphs below show all the videos posted mentioning each of the places and the interest over time plot.")

    option = st.selectbox("Select the year:", 
                        (2018, 2019, 2020, 2021))

    if option == 2018:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Thailand")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2018, videos_info, 'Thailand', 2018), theme='streamlit')

            st.subheader("Pakistan")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2018, videos_info, 'Pakistan', 2018), theme='streamlit')

        with col2:
            #st.subheader(2018)
            st.subheader("Mexico")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2018, videos_info, 'Mexico', 2018), theme='streamlit')

        

    if option == 2019:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("India")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2019, videos_info, 'India', 2019), theme='streamlit')

            st.subheader("Pakistan")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2019, videos_info, 'Pakistan', 2019), theme='streamlit')

        with col2:
            st.subheader("Thailand")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2019, videos_info, 'Thailand', 2019), theme='streamlit')


    if option == 2020:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Thailand")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2020, videos_info, 'Thailand', 2020), theme='streamlit')

            st.subheader("Tabriz")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2020, videos_info, 'Tabriz', 2020), theme='streamlit')

        #st.subheader("Jamaica")
        #st.write(viz.plotting_trends_videos(pytrends_top_places_2020, videos_info, 'Jamaica', 2020))
        with col2:
            st.subheader("India")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2020, videos_info, 'India', 2020), theme='streamlit')

    if option == 2021:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Thailand")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2021, videos_info, 'Thailand', 2021), theme='streamlit')

            st.subheader("California")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2021, videos_info, 'California', 2021), theme='streamlit')
        
        with col2:
            st.subheader("Arizona")
            st.plotly_chart(viz.plotting_trends_videos(pytrends_top_places_2021, videos_info, 'Arizona', 2021), theme='streamlit')

    st.subheader("Comments/Conclusions")
    st.markdown("Judging solely by the graphs, there doesn't seem to be a correlation between these channels' videos and people's interest in googling the places.")
    st.markdown("This is not surprising given the size of my sample and the fact that Google trends results depend on a multitude of factors.")

if page == "Videos posted by year x Tourist arrivals":

    st.markdown("\n \n")
    st.markdown("### Our third piece of information is the number of international* tourist arrivals for each of the top mentioned places between 2018 and 2021**.")
    st.caption("*For California and Arizona, it's the total tourist arrivals, not only international. For Tabriz, the arrivals refer to Iran as a whole.")
    st.caption("**The only data on arrivals found for Pakistan was for 2018 and 2021")
    st.image(r'../streamlit_files/imgs/plane.jpg', width=400)
    st.markdown("The graphs below show the total number of views for each place along the years and the number of tourist arrivals.")

    #option = st.selectbox("Select the place:", 
                        #('All', 'Thailand', 'Pakistan', 'India', 'Mexico', 'Tabriz', 'Jamaica', 'California', 'Arizona'))
                        # To be completed
    option = 'All'
    if option == 'All':

        col1, col2, col3 = st.columns([6,1,6])

        with col1:
            st.subheader("Thailand")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Thailand"), theme='streamlit')

            st.subheader("Pakistan")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Pakistan"), theme='streamlit')

            st.subheader("Tabriz")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Tabriz"), theme='streamlit')

          
            st.subheader("Arizona")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Arizona"), theme='streamlit')

        
        with col3:
            st.subheader("California")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "California"), theme='streamlit')

            st.subheader("Mexico")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Mexico"), theme='streamlit')

            st.subheader("Jamaica")
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, "Jamaica"), theme='streamlit')

    st.subheader("Comments/Conclusions")
    st.markdown("It is difficult to say if there is any correlation judging by the graphs alone. We need need quantitative data instead.")
            

            