# How far does the influence of travel youtubers go? 🌎
_An analysis of the correlation between travel videos and their impact on people's interest and tourism._  

<img src= "https://user-images.githubusercontent.com/109185207/207506141-777cca65-7f7e-4fb6-b1b7-7dc90f08a968.png" width="800" height="400">


**Have you ever been influenced by a video on YouTube to Google a place you had never heard of before? Have you ever visited a new place because of YouTube?**
That's where the inspiration for this project comes from. I'm a heavy YouTube user and I love to travel, so I wanted to see if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world', meaning, on people's online searches and on the number of tourists visiting the places mentioned.  


**You might be wondering: 'But YouTube is huge! How can you possibly check this?**  
The answer is: **I can't**! At least not for the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.  

⚠️ BE WARNED ⚠️  This is a **very** thorough README in which I'm going to explain **everything** I've done! If you want only the gist, I recommend reading the "structure of this analysis" and the "further analysis and conclusions" sections. If you have any questions or just wish to connect, feel free to send me a message on [LinkedIn](https://www.linkedin.com/in/mayara-almeida-souza/) :) Happy reading!

## The structure of this analysis was divided into 3 parts:  

1. **Data extraction**: For the YouTube data I selected 10 of the most famous travel YouTube channels (as seen below). I extracted the titles, descriptions, dates the videos were posted and tags of all the videos in each channel by using the official YouTube API.  
<img src= "https://user-images.githubusercontent.com/109185207/207507449-c2f1af7c-c373-465a-b80a-8fa04a846a51.png" width="800" height="400">

The selection of these particular channels did introduce some biases into my analysis. All of them are made by English-speaking people, so there is a linguistic-cultural bias, but since I used Natural Language Processing in my analysis and the libraries work better with the English language, this choice had to be made. Besides this, the sample is very small when we think of the "size" of the internet, so it becomes more challeging to find a correlation between only 10 channels and "real-life" impact. Initially, I tried to gather travel videos in general, without limiting the analysis to specific channels. However, since I needed to be logged into my YT account to use its API, the videos shown were always the most relevant **to me** and I judged this would introduce an even bigger bias.  

For the tourism data I used The World Bank [website](https://data.worldbank.org/indicator/ST.INT.ARVL) to find information on international tourist arrivals per year per country and also hotel occupancy rates. I used this to compare it with the most viewed places in a certain year. The database wasn't complete for all the places I was analysing, so I completed it myself by googling the missing information. 

Finally, the last piece of data was Google Trends interest over time results. My first measure to check for correlation was analysing the results for the most "viewed" places (in terms of total number of views of all the videos mentioning the place) in a given year. The results were checked for the searches "Place", "Flight Place" and "Travel Place". To access this data I used an unofficial API called PyTrends.

2. **Location extraction**: I needed to find a way to identify the places mentioned in each video. Since the API doesn't give me access to closed captions/subtitles, I decided to extract the location from the titles, descriptions and tags by using Entity Recognition through the LocationTagger pyhton library. This technique presented some challenges because it wasn't 100% precise in recognizing places for my purposes (for example, if in the text input the words 'four' or 'samsung' were present, it assumed they were refering to cities). Also, not all the videos actually mention the place in writing, so, inevitably, I had some missing information.  

3. **Further analysis and conclusions**: Having all the data needed I could finally check if there was any correlation between these travel channels and interest in the places mentioned. Naturally, for this project I can only talk about correlation and not causation because, as I mentioned before, the sample is very small and interest for a certain place is multifactorial, therefore it's impossible to talk about causation in this context.

## Step by step process  
<img src= "https://user-images.githubusercontent.com/109185207/207512278-a5912e24-7c67-44a0-b3a7-cda1a5f7bf18.jpg" width="800" height="350">  

### 1. Data Extraction  
  
**`YouTube API`**  

- The first step after deciding which channels to analyse was getting their IDs in order to use the API. There isn't any way of getting this information out of the channel name or link, so I clicked on a video from each channel, inspected the page and found the ID. The reasons why I didn't scrape the page to gather the IDs automatically were not to get blocked by YouTube for using automation, not having to deal with the different ads before each video (while in the ad the ID wasn't visible on the HTML code) and to make it faster and simpler since there were only 10 channels.  

- Having my list of channel IDs I could use the API to first get information about each channel (subscribers, number of videos, playlist with all the channel videos and total number of views), then using the id for each video playlist I could make another call to get the id for each video and, finally, another call to get all the details from each video. For the functions used in this part of the project I referenced the great work of Thu Vu that can be found [here](https://www.youtube.com/watch?v=D56_Cx36oGY&t=409s). This is a sample of the video_info dataframe (with over 9.500 rows):  

 
 
<img src= "https://user-images.githubusercontent.com/109185207/208264155-ce026c79-a455-4a56-833b-de4ff97a6e85.png" width="700" height="200">
 

- Then, it was a matter of preparing my data for the NLP and further analysis. I built functions to remove emojis from all text inputs, to convert the publication date into datetime so I could extract the year and to convert the count columns to numeric type.  
---  

**`World Bank Open Data`**  

- This part was fairly simple. I downloaded the csv file with information about number of international tourist arrivals and imported it into my notebook. At the end, when I had found out which places were being mentioned and viewed the most, I complemented the missing data myself by using Google. Unfortunately, I wasn't able to find all the missing information. Here's a sample of the dataframe:
  
  

<img src= "https://user-images.githubusercontent.com/109185207/208264971-99815042-72db-4160-b8c9-fe3242985c27.png" width="500" height="50">
  

---  

**`Google Trends`**  

- Getting all the info through code proved to be a bit tricky. I had to use the unofficial API Pytrends and Google kept blocking my access even with a VPN connected. Sometimes it wouldn't block my access but it would return missing information. So this part was tedious since I had to make one single request for each one of the trends I wanted to check (in total, there were 16) and then if during visualization I noticed values that seemed strange, I would go on Google trends website and verify manually if the values I had were the same. All the searches were made for "World" instead of my location (Spain) so I could get general results. 

- It's important to mention how these trend results work. Google doesn't share the number of searches for the term we enter, instead it normalizes it from 0 to 100 and gives us the tendency of search in this proportion. Another important aspect is that if we make a request with more than one item in the list of phrases to be searched, it actually compares all the items in the scale of 0 to 100. Because of this, I could not make a resquest with the list ['Thailand', 'Flight Thailand', 'Travel Thailand'] for example since the volume of searches for 'Thailand' was so much higher that the values for the last two were 0 in comparison. To tackle this problem, I made one request for 'Place' and a separate one for ['Flight Place, 'Travel Place'] because these last ones were similar in volume.  

- The last detail is that through the API I could either get results for specific ranges of dates, for the period of 1 year or for 5 years. I decided to choose the latter, but this means that all the data is connected and the trends from 0 to 100 are calculated taking into consderation the entire period. This means that in one particular year, say 2020 for example, there might not be a value 100 because the results are not given year by year in this option. 

---

### 2. Location Extraction  


- The library I used is called Location Tagger and the documentation can be found [here](https://github.com/kaushiksoni10/locationtagger). First, I created a function to loop through my video_info dataframe and find names of places in the description, title and tags of each video (in my code this function is called 'extracting_places'). The library separates the location entities in 'city', 'region', and 'country', so I created a new column for each one of these categories. However, there are many cities and regions that have the same name as countries. This meant that whenever this type of place was mentioned it was repeated in more than one category. This was a problem because in order to check which places were mentioned and viewed the most I had to count the number of ocurrences of each one and having repeated words would make the results incorrect. The solution I found was to create a fourth column 'everywhere' in which I added all the unique ocurrences of all the places extracted by the library. Of course that meant I had no way of knowing if the videos were mentioning a city or a country, and in the end I just assumed it was a country.  

- The next step was counting how many times each place was mentioned per year. I created the function 'counting_ocurrences_places' that looped through my df and by using a counter along with the most_common method returned the places_by_year df. This is a dataframe that contains a column for year and a list of tuples with the place and the number of times it was mentioned.  
<img src= "https://user-images.githubusercontent.com/109185207/209612365-f4cbfb47-be84-4da7-824d-9d297900ca19.jpg" width="1000" height="500">  

-  At first glance, I noticed that some things didn't make much sense. For example, why were places such as Tennessee, Nashville and Canada the most mentioned in so many years? What about the place 'Four'? To find these answers I made another function called counting_ocurrences_places_by_channel so I could check channel by channel which ones were 'skewing' my results. Having done that, I found some biased places that had to deleted, otherwise they could influence my analysis:
  
  1.  `kara and nate`: Tennessee and Nashville are in every description because it's their address;  
  
  2.  `kristen e siya`: their address is in many descriptions from the year 2017 to 2019 and it's 'Grimsby, Ontario'. They do have videos talking about Ontario after this;  
  
  3.  `yes theory`: ed, four and thomas are not places;  
  
  4.  `drew binsky`: in most of his descriptions from 2021 and 2022 he links some of his most popular videos and one of them is "► Why is Everything Free in Pakistan?"  
  
  5.  `all channels`: 'Us' was probably the word 'us' and not 'The U.S' and nationalities such as "German" and "Canadian" are not places either.  
 
- To delete them, I built a function called deleting_biased_places to take care of these specific cases I had found by going through their channels and videos. Errors such as the ones listed on item number 5 were not deleted because they could easily spotted once I started to select the places that would the object of my project.
  
- **How to decide the criteria for selecting the places to be analysed?**  

I arrived at the conclusion that choosing the most mentioned places wouldn't be the best approach. Since my sample consisted of channels with very different numbers of subscribers, this meant that a place that was mentioned a lot by smaller channels might not have been 'viewed' as much as the ones mentioned by the bigger channels and because the focus of the project is looking for any correlation in "real life" I had to prioritize the number of people watching these videos. So, I built a function called get_views_per_top_place that would add up all the views gathered throughout all the videos that were mentioning each place in a certain year (from 2009 to 2022). With this choice comes a huge sidenote: **the total number of views was not achieved on the day the video was posted and this means that older videos had much more time to gather their views. Maybe the most viewed places in a given year would be different if I had access to the total views in that particular year, but since the API doesn't give me this information I oversimplified this aspect of my analysis and just assumed the places were the same then and now.**  

After using my function, the places_by_year dataframe consisted of lists of tuples which made it hard to work with, so the next step was creating another function (organizing_places_views_df) to reorganize it and make it more readable once I had the total number of views. This is the final result:  

<img src= "https://user-images.githubusercontent.com/109185207/217399176-7dd7754a-f4e3-4957-b45c-1b7696d00fd3.jpg" width="475" height="250"> 


Since the focus of this project were the years 2018 to 2022 only, I could simply check the top 3 most viewed places in each year and conduct my analysis based on them and if there were any errors caused by the LocationTagger library I could move to the next place on the list. On the graphs below, we can see the top 5 places from 2018 to 2022 and how the number of mentions does not necessarily translate into number of views:

<img src= "https://user-images.githubusercontent.com/109185207/217399290-bebfb1c1-07a7-4195-a312-57debb3763d9.png" width="500" height="350">     <img src= "https://user-images.githubusercontent.com/109185207/217399316-6626de6c-bfa5-42d4-81a4-be922b079f1d.png" width="500" height="350">  

<img src= "https://user-images.githubusercontent.com/109185207/217399325-0259e076-ba9d-446b-92e0-95d903503119.png" width="500" height="350">      <img src= "https://user-images.githubusercontent.com/109185207/217399352-2680a5b6-f8db-490b-b4e3-da198b32fc17.png" width="500" height="350">  

<img src= "https://user-images.githubusercontent.com/109185207/217399355-d1413a99-c3b0-41cb-986a-49580a3ca6d2.png" width="500" height="350">  

**Having this information, the places that will be the subject of this analysis are:  **

- 2018: Thailand, Pakistan and Mexico. Since Bangkok is in Thailand, I decided to be more generalistic.
- 2019: Thailand, India and Pakistan
- 2020: Thailand, Tabriz and India
- 2021: Thailand, California and Arizona. Santa Monica and Los Angeles are in California and America is too broad (a whole continent!). The reason why I decided to take into consideration these two states separately instead of doing the same I did for Thailand-Bangkok is because the USA is way bigger than Thailand and has a very large volume of tourism in these two states independently.
- 2022: Thailand, India and Mexico.  
---
  
### 3. Further analysis  
  
- Now it's time to relate the main pieces of information I have so far: the total number of views for each place and the results of Google Trends. So, my first attempt for possibly finding any correlation was plotting all this information in one plot for each place. **All these plots are interactive and better visualized (meaning: less cluttered) on my app deployed on Streamlit.**  
  
![thai](https://user-images.githubusercontent.com/109185207/217666337-a11e55a2-86ae-4fae-a207-925dd053eafa.png)

![india](https://user-images.githubusercontent.com/109185207/217666396-17de90a3-5ac5-4010-8c57-e2044ada1c72.png)

![pakistan](https://user-images.githubusercontent.com/109185207/217666458-24d0c5a6-a27f-47b1-abe8-20c3637f1775.png)

![mexico](https://user-images.githubusercontent.com/109185207/217666489-aeb2fa7e-ac35-4eca-b93d-5e543934c656.png)

![Tabriz](https://user-images.githubusercontent.com/109185207/217666555-3f1351df-ecaf-47a5-840b-1fba49b2961b.png)

![california](https://user-images.githubusercontent.com/109185207/217666601-5c782a99-f2ae-438b-8fae-7ae402787685.png)

![arizona](https://user-images.githubusercontent.com/109185207/217666606-07b32191-6740-49e2-a421-0cd3573fbd3f.png)  
  
- It becomes clear by looking at these graphs that there doesn't seem to be a clear correlation between views and interest over time on Google Trends. However, these plots have too much information on them and it becomes hard to arrive at any conclusion with the "naked eye". The best approach then is using correlation heatmaps, as seen below:   







