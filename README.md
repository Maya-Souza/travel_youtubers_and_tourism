# How far does the influence of travel youtubers go? 🌎
_An analysis of the correlation between travel videos and their impact on people's interest and tourism._  

<img src= "https://user-images.githubusercontent.com/109185207/207506141-777cca65-7f7e-4fb6-b1b7-7dc90f08a968.png" width="800" height="350">


**Have you ever been influenced by a video on YouTube to Google a place you had never heard of before? Have you ever visited a new place because of YouTube?**
That's where the inspiration for this project comes from. I'm a heavy YouTube user and I love to travel, so I wanted to see if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world', meaning, on people's online searches and on the number of tourists visiting the places mentioned.  


**You might be wondering: 'But YouTube is huge! How can you possibly check this?**  
The answer is: **I can't**! At least not for the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.  

## The structure of this analysis was divided into 4 parts:  

1. **YouTube data**: I selected 10 of the most famous travel YouTube channels (as seen below). I extracted the titles, descriptions, dates the videos were posted and tags of all the videos in each channel by using the official YouTube API.  
<img src= "https://user-images.githubusercontent.com/109185207/207507449-c2f1af7c-c373-465a-b80a-8fa04a846a51.png" width="800" height="400">

The selection of these particular channels did introduce some biases into my analysis. All of them are made by English-speaking people, so there is a linguistic-cultural bias, but since I used Natural Language Processing in my analysis and the libraries work better with the English language, this choice had to be made. Besides this, the sample is very small when we think of the "size" of the internet, so it becomes more challeging to find a correlation between only 10 channels and "real-life" impact. Initially, I tried to gather travel videos in general, without limiting to specific channels. However, since I needed to be logged into my YT account to use its API, the videos shown were always the most relevant **to me** and I judged this would be an even bigger bias. 


2. **Location extraction**: I needed to find a way to identify the places mentioned in each video. Since the API doesn't give me access to closed captions/subtitles, I decided to extract the location from the titles, descriptions and tags by using Entity Recognition through the LocationTagger pyhton library. This technique presented some challenges because it wasn't 100% precise in recognizing places for my purposes (for example, if in the text input the words 'four' or 'samsung' were present, it assumed they were refering to cities). Also, not all the videos actually mention the place in writing, so, inevitably, I had some missing information.  

3. **Google Trends**: My first measure to check for correlation was analysing Google Trends interest over time results for the most "viewed" places (in terms of total number of views of all the videos mentioning the place) in a given year. The results were checked for searches such as "Place Name" and "Place Name Travel". To access this data I used an unofficial API called PyTrends.  

4. **Real-life data: tourism**: The World Bank provides data on international tourist arrivals per year per country and also hotel occupancy rates. I used this information to compare it with the most viewed places in a certain year. The database wasn't complete for all the places I was analysing, so I completed it myself by googling the missing information.  

## Step by step process  
<img src= "https://user-images.githubusercontent.com/109185207/207512278-a5912e24-7c67-44a0-b3a7-cda1a5f7bf18.jpg" width="800" height="350">










