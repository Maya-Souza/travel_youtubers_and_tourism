# streamlit
import streamlit as st
st.set_page_config(layout="wide")
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu


st.title("How far does the influence of travel youtubers go? 🌎")
st.markdown("#### _An analysis on the correlation between travel videos and their impact on people's interest and tourism._")
st.image('imgs\youtube-users.png')


st.subheader("The _what_ and the _why_")
st.write("🤔 **Have you ever been influenced by a video on YouTube to Google a place you had never heard of before? Have you ever visited a new place because of YouTube?**")
st.write("That's where the inspiration for this project comes from. I'm a heavy YouTube user and I love to travel, so I wanted to find out if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world'. In other words, do they have an impact on people's online searches and on the number of tourists visiting the places mentioned?")  
st.write("**You might be wondering: 'But YouTube is huge! How can you possibly check this?**")
st.write("The answer is: **I can't**! At least not for the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.")
st.subheader("The _how_")
st.write("**The structure of this analysis was divided into 3 parts:**") 

st.write("""1. Data Collection and Location Extraction: gathering all the data needed and identifying the places 
mentioned in the videos by using Natural Language Processing (NLP) on the titles, descriptions and tags \n 
2. What the data tells us: exploring and visualizing the data \n 
3. Final Conclusions: summarizing the insights and answering the original question: is there any correlation at all? \n""")

st.write("Topic 1 will be explored on this page. You'll read about it in general terms and learn more about the step-by-step process as well. Topics 2 and 3 can be accessed through the side menu. \n\n")
st.write("If you want to see my code, you can refer to my [GitHub repo](https://github.com/Maya-Souza/travel_youtubers_and_tourism).")
st.write(" **Happy reading!** 📖")

st.markdown("---------")

tab1, tab2 = st.tabs(["Data Collection 📁", "Location extraction 🌎"])

with tab1:
    st.subheader("Data Collection 📁")

    st.markdown("**🎥 YouTube data 🎥**")
    st.write("""The selection of these particular channels did introduce some biases into my analysis. 
            All of them are made by English-speaking people, so there is a linguistic-cultural bias, 
            but since I used Natural Language Processing in my analysis and the libraries work better with the English language, 
            this choice had to be made.\n\n Besides this, the sample is very small when we think of the "size" of the internet, 
            so it becomes more challeging to find a correlation between only 10 channels and "real-life" impact. 
            Initially, I tried to gather travel videos in general, without limiting the analysis to specific channels, so I could have
            a much larger sample. 
            However, since I needed to be logged into my YT account to use its API, the videos shown were always the most relevant **to me** 
            and I judged this would introduce an even bigger bias.""") 
    st.write("So, in summary, bias is all around us and there's no escape! 🤷‍♀️")
    st.markdown("**These were the channels selected:** ")
    st.markdown("\n\n \n")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('imgs/drew.jpg', width=200)
    with col2:
        st.image('imgs/yes.jpg', width=200)
    with col3:
        st.image('imgs/mark.jpg', width=200)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image('imgs/samuel.jpg', width=250)
    with col5:
        st.image('imgs/gone.jpg', width=250)
    with col6:
        st.image('imgs/kara.jpg', width=200)

    col7, col8, col9 = st.columns(3)

    with col7:
        st.image('imgs/fearless.jpg', width=200)
    with col8:
        st.image('imgs/kristen.jpg', width=200)
    with col9:
        st.image('imgs/lost.jpg', width=200)

    st.image('imgs/wolters.jpg', width=200)
    
    st.write("\n \n \n \n \n")
    
    st.write("🪜 **Step-by-step process** 🪜 ")

    st.write("""
    - The first step after deciding which channels to analyse was getting their IDs in order to use the API. 
    There isn't any way of getting this information out of the channel name or link, so I clicked on a video from each channel, 
    inspected the page and found the ID. The reasons why I didn't scrape the page to gather the IDs automatically were 
    not to get blocked by YouTube for using automation, not having to deal with the different ads before each video 
    (while in the ad the ID wasn't visible on the HTML code) and to make it faster and simpler since there were only 10 channels.  

    - Having my list of channel IDs I could use the API to first get information about each channel 
    (subscribers, number of videos, playlist with all the channel videos and total number of views). 
    Then, using the ID for each video playlist I could make another call to get the ID for each video and, finally, 
    another call to get all the details from each video. 
    For the functions used in this part of the project I referenced the great work of Thu Vu that can be found 
    [here](https://www.youtube.com/watch?v=D56_Cx36oGY&t=409s). This is a sample of the final video_info dataframe (with over 9.500 rows):
    """)

    st.image("images/table_screenshots/videos_info.png")

    st.write("""
    - Then, it was a matter of preparing my data for the NLP and further analysis. I built functions to remove emojis from all text inputs, 
    to convert the publication date into datetime so I could extract the year and to convert the count columns to numeric type. 
    """)

    st.markdown("---")

    st.markdown("**🌎 Tourism data 🌎**")

    st.write("""I used the World Bank [website](https://data.worldbank.org/indicator/ST.INT.ARVL) to find information on 
    international tourist arrivals per year per country. 
    I used this to compare it with the most viewed places in a certain year. 
    The database wasn't complete for all the places I was analysing, so I completed it myself by googling the missing information. 
    It's important to mention that the way countries count the number of tourists vary from one another and that the data on 
    World Bank takes into consideration number of arrivals, so if the same person travelled more than once inside the same country, 
    they would be counted multiple times. On top of that, for some countries the data was for total of tourist arrivals instead of 
    just international tourists (which for this analysis made more sense), 
    so I verified this information on governmental websites and retracted it where necessary. """)

    st.write("🪜 **Step-by-step process** 🪜 ")

    st.write("""
    - I downloaded the csv file from the World Bank's website with information about number of international tourist arrivals, 
    but the data was updated only up to 2020. So, when I had found out which places were being mentioned and viewed the most, 
    I complemented it with information I found online. I used sources such as Statista, Reuters, government websites and news outlets. 
    Unfortunately, even after a thorough research, 
    I couldn't gather all the missing data I needed and this part of the analysis is incomplete for the years 
    2021 and 2022 for some of the places. These particular cases are documented throghout the analysis.
    Here's a sample of the dataframe:
    """)
    st.image("images/table_screenshots/tourism_data.png", width=500)
    st.markdown("\n\n \n")

    st.markdown("---")

    st.markdown("**🔎 User behavior data - Google Trends 🔍**")

    st.markdown("""Finally, the last piece of data was Google Trends interest over time results. 
    Google Trends is a tool that shows us the behavior of people searching on Google for a specific term. 
    It gives us graphs varying from 0 to 100 showing how much people looked for a given word or phrase over a period of time. 
    This step was taken after the Location Extraction since I had to know which places were going to be analysed first.
    I took into consideration the most 'viewed' places 
    (in terms of total number of views of all the videos mentioning the place) in a given year. 
    The results were checked for the searches 'Place', 'Flight Place' and 'Travel Place'. 
    To access this data I used an unofficial API called PyTrends.""")

    st.write("🪜 **Step-by-step process** 🪜 ")

    st.write("""
    - Getting all the info through code proved to be a bit tricky. I had to use the unofficial API Pytrends and Google 
    kept blocking my access even with a VPN connected. Sometimes it wouldn't block my access but it would return missing information. 
    So this part was tedious since I had to make one single request for each one of the trends 
    I wanted to check (in total, there were 16) and then if during visualization I noticed values that seemed strange, 
    I would go on Google trends website and verify manually if the values I had were the same. 
    All the searches were made for "World" instead of my location (Spain) so I could get general results. 

    - It's important to clarify how these trend results work. 
    Google doesn't share the number of searches for the term we enter, 
    instead it normalizes it from 0 to 100 and gives us the tendency of search in this proportion. 
    Another important aspect is that if we make a request with more than one item in the list of phrases to be searched, 
    it actually compares all the items in the scale of 0 to 100. 
    Because of this, I could not make a request with the list ['Thailand', 'Flight Thailand', 'Travel Thailand'] 
    for example. Since the volume of searches for 'Thailand' was naturally so much higher than the others, the values for the last two were 0 in comparison. 
    To tackle this problem, I made one request for 'Place' and a separate one for ['Flight Place, 'Travel Place'] 
    because these last ones were similar in volume across all places. At the end, I ended up with two separate dataframes for each place
    one 'pytrends_place' and another one for the related searches called 'pytrends_place_related'. 

    - The last detail is that through the API I could either get results for specific ranges of dates, 
    for the period of 1 year or for 5 years. 
    I decided to choose the latter, 
    but this meant that all the data is connected and the trends from 0 to 100 are calculated taking into consderation the entire period. 
    So, in one particular year, say 2020, there might not be a value 100 because the highest volume of searches was in 2018, for example.  
    
    - After this whole process, I had 16 separate dataframes which wasn't at all ideal to work with.
    So, I decided to create one dataframe for the 'Place' searches and another one for 'Flight Place' and 'Travel Place'.
    A sample of the pytrends_mexico_related before being concatenated with the other ones:""")
    
    st.image("images/table_screenshots/pytrends_mexico_related.png", width = 350)
    st.markdown("\n\n \n")

    st.write('Having collected the data, I could finally extract the places mentioned in the videos.')

    st.markdown('[Back to the top](#data-collection)')

with tab2:
    st.subheader("Location extraction 🌎")

    st.write("""
    I needed to find a way to identify the places mentioned in each video. 
    Since the API doesn't give me access to closed captions/subtitles, I decided to extract the location from the titles, 
    descriptions and tags by using Entity Recognition through the LocationTagger python library 
    (the documentation can be found [here](https://github.com/kaushiksoni10/locationtagger)). 
    This technique presented some challenges because it wasn't 100% precise in recognizing places for my purposes. 
    For example, if in the text input the words 'four' or 'samsung' were present, it assumed they were refering to cities
    because there are cities called Four and Samsung. 
    Also, not all the videos actually mention the place in writing, so, inevitably, I had some missing information.
    """)

    st.write("🪜 **Step-by-step process** 🪜 ")

    st.write("""
    - First, I created a function to loop through my video_info dataframe and find names of places in the description, 
    title and tags of each video (in my code this function is called 'extracting_places'). 
    The library separates the location entities in 'city', 'region', and 'country', so I created a new column for 
    each one of these categories. However, there are many cities and regions that have the same name as countries. 
    This meant that whenever this type of place was mentioned it was repeated in more than one category. 
    This was a problem because in order to check which places were mentioned and viewed the most 
    I had to count the number of ocurrences of each one and having repeated words would make the results incorrect. 
    The solution I found was to create a fourth column 'everywhere' in which I added all the unique ocurrences of 
    all the places extracted by the library. Of course that meant I had no way of knowing if the 
    videos were mentioning a city or a country, and in the end I felt it was more likely they were countries and just assumed it was.""")  
    
    st.write("""- The next step was counting how many times each place was mentioned per year. 
    I created the function 'counting_ocurrences_places' that looped through my df and by using a counter 
    along with the 'most_common' method returned the places_by_year df. This is a dataframe that contains a 
    column for year and a list of tuples with the place and the number of times it was mentioned. \n The places_by_year dataframe: 
    """)
    st.markdown("\n\n \n")

    st.image("images/table_screenshots/places_per_year_before_filtering.jpg")
    st.markdown("\n\n \n")

    st.write("""
    -  At first glance, I noticed that some things didn't make much sense. 
    For example, why were places such as Tennessee, Nashville and Canada the most mentioned in so many years? 
    What about the place 'Four'? To find these answers I made another function called counting_ocurrences_places_by_channel 
    so I could check channel by channel which ones were 'skewing' my results and why. 
    Having done that, I found some biased places that had to deleted, otherwise they could influence my analysis:
  
    1.  `kara and nate`: Tennessee and Nashville are in every description because it's their address;  
    
    2.  `kristen e siya`: their address is in many descriptions from the year 2017 to 2019 and it's 'Grimsby, Ontario'. 
    They do have videos talking about Ontario after this;  
    
    3.  `yes theory`: ed, four and thomas are not places;  
    
    4.  `drew binsky`: in most of his descriptions from 2021 and 2022 he links some of his most popular videos and one of them is 
    "► Why is Everything Free in Pakistan?"  
    
    5.  `all channels`: 'Us' was probably the word 'us' and not 'The U.S' and nationalities such as "German" and "Canadian" are not places either.  
    
    - To delete them, I built a function called deleting_biased_places to take care of these specific cases 
    I had found by going through their channels and videos. 
    Errors such as the ones listed on item number 5 were not deleted because they could be easily spotted once 
    I started to select the places that would be the object of my project. 
    """)

    st.write("""
    **How to decide the criteria for selecting the places to be analysed?**  

    I arrived at the conclusion that choosing the most mentioned places wouldn't be the best approach. 
    Since my sample consisted of channels with very different numbers of subscribers, this meant that a place that was mentioned 
    a lot by smaller channels might not have been 'viewed' as much as the ones mentioned by the bigger channels. Since the focus of the project 
    is looking for any correlation in "real life", I had to prioritize the number of people watching these videos. 
    So, I built a function called get_views_per_top_place that would add up all the views gathered throughout all the videos that were mentioning 
    each place in a certain year (from 2009 to 2022). \n
    With this choice comes a huge sidenote: **the total number of views was not achieved on the day 
    the video was posted and this means that older videos had much more time to gather their views. Maybe the most viewed places in a given 
    year would be different if I had access to the distribution of views over time, but since 
    the API doesn't give me this information I oversimplified this aspect of my analysis and just assumed the places were the same then and now.
    Having a weekly or monthly distribution of views would allow me to compare it to Google Trends results more accurately, which would be ideal.**
    """)

    st.write("""
    After extracting the places, deleting the biased ones and adding up all the views, the places_by_year dataframe still consisted of 
    lists of tuples of, which made it unecessarily hard to work with. 
    So, the next step was creating another 
    function (organizing_places_views_df) to reorganize my dataframe and make it more workable. 
    This is the final result:
    """)

    st.image("images/table_screenshots/places_per_year_views_mentions.jpg", width = 550)

    st.write("""
    Having all the pieces together, it's time to dig into the data and analyse it! 
    You can now go to the section "What the data tells us" :)
    """)
    st.markdown('[Back to the top](#location-extraction)')
