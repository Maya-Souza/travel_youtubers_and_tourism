import pandas as pd

# viz
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# streamlit
import streamlit as st
st.set_page_config(layout="wide")
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
# from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


# plotting functions files
from src import viz


# youtube data
videos_info = pd.read_pickle('data/videos_info.pkl')
places_mentions_views = pd.read_pickle('data/all_places_views_per_year.pkl')
places_mentions_views = places_mentions_views.sort_values(by = ['year', 'total_number_of_views'], ascending=False)

# google trends data
pytrends_concat = pd.read_pickle('data/pytrends_concat.pkl')
pytrends_related_concat = pd.read_pickle('data/pytrends_related_concat.pkl')
videos_trends_merged = pd.read_pickle('data/videos_trends_merged.pkl')

# tourist arrivals data
number_of_tourist_arrivals = pd.read_pickle('data/international-tourism-number-of-arrivals.pkl')


################################################################################################


st.title("A data lover's paradise: graphs! 📈")
st.write("#")
page = option_menu(
    menu_title=None, 
    options=["Places mentioned in the videos along the years", "Google trends for each place", "Videos posted by year x Tourist arrivals"],
    icons=["youtube", "google", "globe"],
    menu_icon="cast",
    default_index=0, 
    orientation="horizontal",
    styles={
        "nav-link": {
            "font-size": "14px",
            "text-align": "justified",
            "margin": "-7px",
            "nav-link-selected": {"font-size": "14px"}
        },
    },
    )
st.markdown("---------")
if page == "Places mentioned in the videos along the years":
    
    

    #st.markdown('/n/n/n')
    st.subheader("🗺️📌 Our first piece of information is the places that were mentioned in each video throughout the years ")
    st.write("""
                Below, you can explore the data for yourself and see the most 'viewed' places, 
                how many times they were mentioned and the total number of views of all the videos that mentioned each place.
                This data is available for the years 2010 to 2022, but the focus of this entire analysis is the period from 2018 to 2022.
                As discussed in the previous section, the library used to extract the locations gave me some problems, and
                that's why you'll see places such as "Four" or "Samsung" in the dataframe.
             """)
    st.markdown("---------")

    # option = st.selectbox("**Select the year:**", places_mentions_views['year'].unique())
    years=places_mentions_views['year'].unique().tolist()
    st.write("**Select the year:**")

    option = option_menu(
    menu_title=None,#'Select the year', 
    options= years,
    icons=[".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    menu_icon="calendar",
    default_index=0, 
    orientation="horizontal",
    styles={
        "nav-link": {
            "font-size": "14px",
            "text-align": "justified",
            "margin": "-7px",
            "nav-link-selected": {"font-size": "14px"},
            "menu-size":"14px"
        },
    },
    )
    st.markdown("---------")

    col1, col2, col3 = st.columns([1,0.1,2])
    with col1:
        data = places_mentions_views.loc[places_mentions_views.year == option].set_index('places').drop('year', axis=1)
        data.rename(columns={'total_number_of_views':'views'}, inplace=True)
        st.write("  ")
        st.markdown('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        st.write(" ")
        st.dataframe(data, height=490)

    with col3:
        top_5_places_views_mentions_x = viz.general_data(option,places_mentions_views)
        st.plotly_chart(top_5_places_views_mentions_x, theme = 'streamlit', use_container_width = True)

# Another possibility would be to use streamlit.aggrid if I wanted the user to filter the data
# or to create pivot tables 
    st.markdown("---------")
    st.subheader("💡Comments💡")
    st.write("""
    On the graphs above 
    we can see clearly that the the number of mentions does not necessarily translate into number of views.
    Since I decided this analysis would be based off the **``top 3``** most viewed places from 2018 to 2022,
    these are the places that are the subject of this analysis: 
    - **2018: Thailand, Pakistan and Mexico.** Since Bangkok is in Thailand, I decided to be more generalistic
    - **2019: Thailand, India and Pakistan**
    - **2020: Thailand, Tabriz and India**
    - **2021: Thailand, California and Arizona.** Santa Monica and Los Angeles are in California and America is too broad 
    (a whole continent!), so I got the sixth place on the list which was Arizona. 
    The reason why I decided to take into consideration these two states separately instead of doing the same 
    I did for Thailand-Bangkok is because the USA is way bigger than Thailand and has a very large volume of tourism in these 
    two states independently
    - **2022: Thailand, India and Mexico.**  
    """)
    st.write("""
    Many of the places repeat themselves throughout the years. So, in the next steps 
    I'll analyse each of them in the period of five years, not only in the year they were the most viewed,
    so we can have a better sense of possible correlations.
    """)

elif page == "Google trends for each place":

    st.markdown("\n\n\n")
    st.subheader("Our second piece of information is the Google Trends data showing interest over time for each one of the top places mentioned in each year.")
    st.image('imgs/Google-Trends.png')
    st.write("""The graphs below show all the videos posted mentioning each of the places 
            and the Google Trends results for interest over time. These results refer to the three keywords analysed: 
            Place, Flight Place and Travel Place. They do contain a lot of information, so to better visualize 
            them I suggest using the '1y' filter on the top.""")
    st.write("""
           It becomes clear by looking at these graphs that there doesn't seem to be a clear correlation between views and 
           interest over time on Google Trends. However, these plots have too much information on them and it becomes hard to arrive 
           at any conclusion with the "naked eye".""")
    st.write(
            """A better approach is calculating the Pearson correlation and using heatmaps 
           to visualize it more clearly. I plotted these heatmaps taking into consideration the whole data I had first 
           (the 5-year period of the trends) and then just taking into consideration the years in which each place was the most viewed 
           on YouTube to check if the correlation coefficient was any different, but the difference was close to none. 
            """)
    st.write(
            """
            In order to calculate the correlation, I created a new dataframe
           merging the weekly trends with the weeks in which there had been at least one video posted mentioning that place. 
           These weekly views were added among all the videos. 
           In other words, this correlation doesn't take into consideration weeks with zero views (where no videos were posted).
            The closer to 1, the highest the correlation.
            """)
    st.markdown("\n\n\n\n\n\n\n\n")

    selected = option_menu(
            menu_title=None,  # required
            options=["Thailand", "---", "Pakistan","---", "Mexico","---", "India", "---","Tabriz","---", "California", "---","Arizona", "---","Comments"],  # required
            icons=["youtube", "youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube", "book","book"],  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "nav-link": {
                    "font-size": "13px",
                    "text-align": "left",
                    "margin": "0px",
                },
            },
        )
    '---'
    if selected == "Comments":

        st.subheader("💡Comments💡")
        st.write("""
        It seems that the total number of videos mentioning a specific place is not at all correlated with the volume of searches about this place. 
        This was in a certain way expected since the volume of views (meaning: the number of people that watched these videos) 
        is not expressive enough to have an impact on the totality of searches on Google. 
         
        """)
        st.write("""
        Besides, despite having the date in which the videos were posted, the data for how many views they had 
        in the week in which they were posted is not available. This is extremely relevant because maybe 
        they went viral weeks or even months after the publication date and the correlation between the trends results from the week 
        they were posted would be close to zero.  
        """)
        st.write("""
        Ideally, I would need to have access to the sum of weekly views for each video 
        so I could compare the results week by week with more precision.
        Another interesting aspect is that some of the searches seem to have a moderate correlation between themselves. 
        That makes sense because if there's a higher volume of people searching 
        "travel to Thailand" there could be an increase in searches such as "flight to Thailand" as well.
        """)

    else:
        st.subheader(selected)
        st.plotly_chart(viz.plotting_trends_videos(pytrends_concat, pytrends_related_concat, videos_info, selected), theme='streamlit', use_container_width=True)
        
        col1, col2 = st.columns([1,1])
        
        with col1:
            st.pyplot(viz.sns_correlation_heatmap(videos_trends_merged, selected).figure)

    
    
        
if page == "Videos posted by year x Tourist arrivals":

    st.markdown("\n \n")
    st.subheader("✈️ Finally, our third piece of information is the number of international tourist arrivals for each of the top mentioned places between 2018 and 2021 ")
    st.write("""
    The data I gathered gave me the information of arrivals per year, 
    so I had to take into consideration the sum of all yearly YouTube views for each place in order to compare the two pieces of information. 
    As mentioned before, for some places I couldn't find data for 2021 and/or 2022, 
    so unfortunately this part of the analysis has missing or inconsistent data.
    """)

    st.write("""
    For **California** and **Arizona**, it's the total tourist arrivals, not only international. This decision was made because the channels
    are in English and it would make sense that it influenced tourists from the USA to travel the country.  
    """)
    st.write("""
    Tourism data in the case of **Tabriz** refers to Iran as a whole and not just the city because this information was not available online. 
    Even taking into consideration the entire country, the data for 2021 and 2022 couldn't be found.
    """)
    st.write(""" Lastly, the only data on arrivals found for **Pakistan** was for the years of 2018 and 2021.
     """)

    st.write("""The graph below shows the total number of views for each place along the years 
    and the number of tourist arrivals. Next to it we can see numerically through the Pearson coefficient if
    there seems to be a correlation of the two pieces of data or not.""")

    selected2 = option_menu(
            menu_title=None,  
            options=["Thailand", "---", "Tabriz","---","Pakistan","---", "Mexico","---", "India", "---", "California", "---","Arizona", "---","Comments"],  # required
            icons=["youtube", "youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube","youtube", "book","book"],  # optional
            default_index=0,  
            orientation="horizontal",
            styles={
                "nav-link": {
                    "font-size": "13px",
                    "text-align": "left",
                    "margin": "0px",
                },
            },
        )
    st.markdown("---------")
    col1,col2 = st.columns([2.4,1])

    if selected2 == "Comments":
        st.subheader("💡Comments💡")
        st.write("""
                No strong or moderate correlation was found. 
                Given that the data sample is small, even if there was a moderate or strong correlation
                I wouldn't be able to say whether it was a coincidence or not. 
                I would need much more data stretching throughout a longer period of time in order to accurately show whether there's a 
                correlation between these too variables - 
                at least for some places - or not.
                """)

    elif selected2 == "Tabriz":
        with col1:
            st.subheader(selected2)
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, selected2), 
                            theme='streamlit',use_container_width=True)
            
        st.write("""For this particular case it made no sense to calculate the correlation because there was just a single data point 
                 for YouTube views. Neither before nor after 2020 any of the YouTube channels analyzed mentioned Tabriz.
                 It was a case of a viral video about this not-so-known city that made it show up as one of the top places
                 in 2020.""")
        
    elif selected2 == "Pakistan":
        with col1:
            st.subheader(selected2)
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, selected2), 
                            theme='streamlit',use_container_width=True)
            
        st.write(""" Another case in which it would make no sense to calculate the correlation
          since there's a lot of missing data.""")
    else:
        with col1:
            st.subheader(selected2)
            st.plotly_chart(viz.plotting_tourism_data(places_mentions_views, number_of_tourist_arrivals, selected2), 
                            theme='streamlit',use_container_width=True)
        with col2:
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st.pyplot(viz.correlation_heatmap_tourism(number_of_tourist_arrivals, places_mentions_views, selected2).figure, 
                            use_container_width=True)
    

                 

if page == "Comments":
  st.subheader("💡Comments💡")
 