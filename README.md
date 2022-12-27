# How far does the influence of travel youtubers go? 🌎
_An analysis of the correlation between travel videos and their impact on people's interest and tourism._  

<img src= "https://user-images.githubusercontent.com/109185207/207506141-777cca65-7f7e-4fb6-b1b7-7dc90f08a968.png" width="800" height="350">


**Have you ever been influenced by a video on YouTube to Google a place you had never heard of before? Have you ever visited a new place because of YouTube?**
That's where the inspiration for this project comes from. I'm a heavy YouTube user and I love to travel, so I wanted to see if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world', meaning, on people's online searches and on the number of tourists visiting the places mentioned.  


**You might be wondering: 'But YouTube is huge! How can you possibly check this?**  
The answer is: **I can't**! At least not for the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.  

## The structure of this analysis was divided into 3 parts:  

1. **Data extraction**: For the YouTube data I selected 10 of the most famous travel YouTube channels (as seen below). I extracted the titles, descriptions, dates the videos were posted and tags of all the videos in each channel by using the official YouTube API.  
<img src= "https://user-images.githubusercontent.com/109185207/207507449-c2f1af7c-c373-465a-b80a-8fa04a846a51.png" width="800" height="400">

The selection of these particular channels did introduce some biases into my analysis. All of them are made by English-speaking people, so there is a linguistic-cultural bias, but since I used Natural Language Processing in my analysis and the libraries work better with the English language, this choice had to be made. Besides this, the sample is very small when we think of the "size" of the internet, so it becomes more challeging to find a correlation between only 10 channels and "real-life" impact. Initially, I tried to gather travel videos in general, without limiting the analysis to specific channels. However, since I needed to be logged into my YT account to use its API, the videos shown were always the most relevant **to me** and I judged this would introduce an even bigger bias.  

For the tourism data I used The World Bank [website](https://data.worldbank.org/indicator/ST.INT.ARVL) to find information on international tourist arrivals per year per country and also hotel occupancy rates. I used this to compare it with the most viewed places in a certain year. The database wasn't complete for all the places I was analysing, so I completed it myself by googling the missing information. 

Finally, the last piece of data was Google Trends interest over time results. My first measure to check for correlation was analysing the results for the most "viewed" places (in terms of total number of views of all the videos mentioning the place) in a given year. The results were checked for searches such as "Place Name" and "Place Name Travel". To access this data I used an unofficial API called PyTrends.

2. **Location extraction**: I needed to find a way to identify the places mentioned in each video. Since the API doesn't give me access to closed captions/subtitles, I decided to extract the location from the titles, descriptions and tags by using Entity Recognition through the LocationTagger pyhton library. This technique presented some challenges because it wasn't 100% precise in recognizing places for my purposes (for example, if in the text input the words 'four' or 'samsung' were present, it assumed they were refering to cities). Also, not all the videos actually mention the place in writing, so, inevitably, I had some missing information.  

3. **Conclusions**: Having all the data needed I could finally check if there was any correlation between these travel channels and interest in the places mentioned. Naturally, for this project I can only talk about correlation and not causation because, as I mentioned before, the sample is very small and interest for a certain place is multifactorial, therefore it's impossible to talk about causation in this context.

## Step by step process  
<img src= "https://user-images.githubusercontent.com/109185207/207512278-a5912e24-7c67-44a0-b3a7-cda1a5f7bf18.jpg" width="800" height="350">  

### 1. Data Extraction  
  
**`YouTube API`**  

- The first step after deciding which channels to analyse was getting their IDs in order to use the API. There isn't any way of getting this information out of the channel name or link, so I clicked on a video from each channel, inspected the page and found the ID. The reasons why I didn't scrape the page to gather the IDs automatically were not to get blocked by YouTube for using automation, not having to deal with the different ads before each video (while in the ad the ID wasn't visible on the HTML code) and to make it faster and simpler since there were only 10 channels.  

- Having my list of channel IDs I could use the API to first get information about each channel (subscribers, number of videos, playlist with all the channel videos and total number of views), then using the id for each video playlist I could make another call to get the id for each video and, finally, another call to get all the details from each video. For the functions used in this part of the project I referenced the great work of Thu Vu that can be found [here](https://www.youtube.com/watch?v=D56_Cx36oGY&t=409s). This is a sample of the video_info dataframe (with over 9.500 rows):  

 
 
<img src= "https://user-images.githubusercontent.com/109185207/208264155-ce026c79-a455-4a56-833b-de4ff97a6e85.png" width="950" height="300">
 

- Then, it was a matter of preparing my data for the NLP and further analysis. I built functions to remove emojis from all text inputs, to convert the publication date into datetime so I could extract the year and to convert the count columns to numeric type.  
---  

**`World Bank Open Data`**  

- This part was fairly simple. I downloaded the csv file with information about number of international tourist arrivals and imported it into my notebook. At the end, when I had found out which places were being mentioned and viewed the most, I complemented the missing data myself by using Google. Unfortunately, I wasn't able to find all the missing information. Here's a sample of the dataframe:
  
  

<img src= "https://user-images.githubusercontent.com/109185207/208264971-99815042-72db-4160-b8c9-fe3242985c27.png" width="500" height="45">
  

---  

**`Google Trends`**  

---

### 2. Location Extraction  


- The library I used is called Location Tagger and the documentation can be found [here](https://github.com/kaushiksoni10/locationtagger). First, I created a function to loop through my video_info dataframe and find names of places in the description, title and tags of each video (in my code this function is called 'extracting_places'). The library separates the location entities in 'city', 'region', and 'country', so I created a new column for each one of these categories. However, there are many cities and regions that have the same name as countries. This meant that whenever this type of place was mentioned it was repeated in more than one category. This was a problem because in order to check which places were mentioned and viewed the most I had to count the number of ocurrences of each one and having repeated words would make the results incorrect. The solution I found was to create a fourth column 'everywhere' in which I added all the unique ocurrences of all the places extracted by the library. Of course that meant I had no way of knowing if the videos were mentioning a city or a country, and in the end I just assumed it was a country.  
- The next step was counting how many times each place was mentioned per year. I created the function 'counting_ocurrences_places' that looped through my df and by using a counter along with the most_common method returned the places_by_year df. This is a dataframe that contains a column for year and a list of tuples with the place and the number of times it was mentioned.  
<img src= "https://user-images.githubusercontent.com/109185207/209612365-f4cbfb47-be84-4da7-824d-9d297900ca19.jpg" width="500" height="45">  

-  









