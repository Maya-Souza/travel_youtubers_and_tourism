# How far does the influence of travel youtubers go? 🌎 (STILL BEING EDITED)
_An analysis of the correlation between travel videos and their impact on people's interest and tourism._  

<img src= "https://user-images.githubusercontent.com/109185207/207506141-777cca65-7f7e-4fb6-b1b7-7dc90f08a968.png" width="800" height="400">


**Have you ever been influenced by a video on YouTube to Google a place you had never heard of before? Have you ever visited a new place because of YouTube?**
That's where the inspiration for this project comes from. I'm a heavy YouTube user and I love to travel, so I wanted to see if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world', meaning, on people's online searches and on the number of tourists visiting the places mentioned.  


**You might be wondering: 'But YouTube is huge! How can you possibly check this?**  
The answer is: **I can't**! At least not for the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.  

⚠️ BE WARNED ⚠️  This is a **very** thorough README in which I'm going to explain **everything** I've done! If you want only the gist, I recommend reading the "structure of this analysis", "further analysis and considerations" and the "final conclusions" sections. If you have any questions or just wish to connect, feel free to send me a message on [LinkedIn](https://www.linkedin.com/in/mayara-almeida-souza/) :) Happy reading!

## The structure of this analysis was divided into 3 parts:  

1. **Data extraction**: For the YouTube data I selected 10 of the most famous travel YouTube channels (as seen below). I extracted the titles, descriptions, dates the videos were posted and tags of all the videos in each channel by using the official YouTube API.  
<img src= "https://user-images.githubusercontent.com/109185207/207507449-c2f1af7c-c373-465a-b80a-8fa04a846a51.png" width="800" height="400">

The selection of these particular channels did introduce some biases into my analysis. All of them are made by English-speaking people, so there is a linguistic-cultural bias, but since I used Natural Language Processing in my analysis and the libraries work better with the English language, this choice had to be made. Besides this, the sample is very small when we think of the "size" of the internet, so it becomes more challeging to find a correlation between only 10 channels and "real-life" impact. Initially, I tried to gather travel videos in general, without limiting the analysis to specific channels. However, since I needed to be logged into my YT account to use its API, the videos shown were always the most relevant **to me** and I judged this would introduce an even bigger bias.  

For the tourism data I used World Bank [website](https://data.worldbank.org/indicator/ST.INT.ARVL) to find information on international tourist arrivals per year per country. I used this to compare it with the most viewed places in a certain year. The database wasn't complete for all the places I was analysing, so I completed it myself by googling the missing information. It's important to mention that the way countries count the number of tourists vary from one another and that the data on World Bank takes into consideration number of arrivals, so if the same person travelled more than once inside the same country, they would be counted multiple times. On top of that, for some countries the data was for total of tourist arrivals instead of just international tourists (which for this analysis made more sense), so I verified this information on governmental websites and retracted it where necessary. 

Finally, the last piece of data was Google Trends interest over time results. Google Trends is a tool that shows us the behavior of people searching on Google for a specific term. It gives us graphs varying from 0 to 100 showing how much people looked for a given word or phrase over a period of time. My first measure to check for correlation was analysing the results for the most "viewed" places (in terms of total number of views of all the videos mentioning the place) in a given year. The results were checked for the searches "Place", "Flight Place" and "Travel Place". To access this data I used an unofficial API called PyTrends.

2. **Location extraction**: I needed to find a way to identify the places mentioned in each video. Since the API doesn't give me access to closed captions/subtitles, I decided to extract the location from the titles, descriptions and tags by using Entity Recognition through the LocationTagger pyhton library. This technique presented some challenges because it wasn't 100% precise in recognizing places for my purposes (for example, if in the text input the words 'four' or 'samsung' were present, it assumed they were refering to cities). Also, not all the videos actually mention the place in writing, so, inevitably, I had some missing information.  

3. **Further analysis and considerations**: Having all the data needed I could finally check if there was any correlation between these travel channels and interest in the places mentioned. Naturally, for this project I can only talk about correlation and not causation because, as I mentioned before, the sample is very small and interest for a certain place is multifactorial, therefore it's impossible to talk about causation in this context.  

4. **Final conclusions**: Section in which I'll summarize all the insights and try to answer the original question: is there any correlation at all?

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

- I downloaded the csv file from the World Bank's website with information about number of international tourist arrivals, but the data was updated only up to 2020. So, when I had found out which places were being mentioned and viewed the most, I complemented it with information I found online. I used sources such as Statista, Reuters, government websites and news outlets. Unfortunately, even after a thorough research, I couldn't gather all the missing data I needed and this part of the analysis is incomplete for the years 2021 and 2022 for some of the places. 
  
  

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

**Having this information, the places that will be the subject of this analysis are:**  

- 2018: Thailand, Pakistan and Mexico. Since Bangkok is in Thailand, I decided to be more generalistic.
- 2019: Thailand, India and Pakistan
- 2020: Thailand, Tabriz and India
- 2021: Thailand, California and Arizona. Santa Monica and Los Angeles are in California and America is too broad (a whole continent!), so I got the sixth place on the list which was Arizona. The reason why I decided to take into consideration these two states separately instead of doing the same I did for Thailand-Bangkok is because the USA is way bigger than Thailand and has a very large volume of tourism in these two states independently.
- 2022: Thailand, India and Mexico.  
---
  
### 3. Further analysis and considerations 
  
**3.1 Number of views on Youtube and Google Trends**  

  
- Now it's time to relate the main pieces of information I have so far: the total number of views for each place and the results of Google Trends. So, my first attempt for possibly finding any correlation was plotting all this information in one plot for each place. **All these plots are interactive and better visualized (meaning: less cluttered) on my app deployed on Streamlit.**  
  
![thai](https://user-images.githubusercontent.com/109185207/217666337-a11e55a2-86ae-4fae-a207-925dd053eafa.png)
---
![india](https://user-images.githubusercontent.com/109185207/217666396-17de90a3-5ac5-4010-8c57-e2044ada1c72.png)
---
![pakistan](https://user-images.githubusercontent.com/109185207/217666458-24d0c5a6-a27f-47b1-abe8-20c3637f1775.png)
---
![mexico](https://user-images.githubusercontent.com/109185207/217666489-aeb2fa7e-ac35-4eca-b93d-5e543934c656.png)
---
![Tabriz](https://user-images.githubusercontent.com/109185207/217666555-3f1351df-ecaf-47a5-840b-1fba49b2961b.png)
---
![california](https://user-images.githubusercontent.com/109185207/217666601-5c782a99-f2ae-438b-8fae-7ae402787685.png)
---
![arizona](https://user-images.githubusercontent.com/109185207/217666606-07b32191-6740-49e2-a421-0cd3573fbd3f.png)  
  
- It becomes clear by looking at these graphs that there doesn't seem to be a clear correlation between views and interest over time on Google Trends. However, these plots have too much information on them and it becomes hard to arrive at any conclusion with the "naked eye". A better approach is calculating the Pearson correlation and using heatmaps to visualize it more clearly. I plotted these heatmaps taking into consideration the whole data I had first (the 5-year period of the trends) and then just taking into consideration the years in which each place was the most viewed on YouTube to check if the correlation coefficient was any different. In order to do this, I created a new dataframe merging the weekly trends with the weeks in which there had been at least one video posted mentioning that place. These weekly views were added among all the videos. In order words, this correlation doesn't take into consideration weeks with zero views (where no videos were posted).
The results can be seen below:  
  
  
  
   
  
  
  
![thailand_heatmap](https://user-images.githubusercontent.com/109185207/217673171-8497013f-7584-4f84-9614-0fba047f22de.png)
---
  
  
  

  
![pakistan_heatmap](https://user-images.githubusercontent.com/109185207/217673085-2d5fa23e-7b4e-487c-a442-87f4d26bbc3d.png)      ![pakistan_specific_years_heatmap](https://user-images.githubusercontent.com/109185207/217673109-fad5ffa1-8ba7-4f1a-9452-fc95935474d1.png)
---

  
  

  
![india_heatmap](https://user-images.githubusercontent.com/109185207/217672909-a7d40e6a-ec7f-4204-88fc-771164cc498a.png)  ![india_specific_years_heatmap](https://user-images.githubusercontent.com/109185207/217672944-ad28f11f-b9cf-4746-a5e0-8c3190ee3d68.png)
---

  
  

  
![mexico_heatmap](https://user-images.githubusercontent.com/109185207/217672796-1571b6d5-40a3-454f-935b-a75a7d82d5f4.png)  ![mexico_specific_years_heatmap](https://user-images.githubusercontent.com/109185207/217672820-c59b83bb-4beb-44c8-86ee-364754e50546.png)
---
  
  

![california_heatmap](https://user-images.githubusercontent.com/109185207/217672605-d9df5c71-ecc7-4d15-ab29-d7bb126a6b1b.png) ![california_specific_years_heatmap](https://user-images.githubusercontent.com/109185207/217672609-56529ece-8e88-4523-b0a8-a3998fe6732f.png)
---  
  
  
  
![arizona_heatmap](https://user-images.githubusercontent.com/109185207/217672514-2ebd8f81-ecea-4800-bbb6-67c070cc0dbe.png) ![arizona_specific_years_heatmap](https://user-images.githubusercontent.com/109185207/217672576-51211ab8-42c0-4d6c-8510-7a30a787c122.png)  
  
  
  
**`First considerations:` It seems that the total number of videos mentioning a specific place is not at all correlated with the volume of searches about this place. This was in a certain way expected since the volume of views (meaning: the number of people that watched these videos) is not expressive enough to have an impact on the totality of searches on Google. Besides, despite having the date in which the videos were posted, the data for how many views they had in the week in which they were posted is not available. This is extremely relevant because maybe they went viral weeks or even months after the publication date and the correlation between the trends results from the week they were posted would be close to zero. Ideally, I would need to have access to the sum of weekly views for each video so I could compare the results week by week with more precision.
Another interesting aspect is that some of the searches seem to have a moderate correlation between themselves. That makes sense because if there's a higher volume of people searching "travel to Thailand" there could be an increase in searches such as "flight to Thailand" as well.**  


---  

  
  
**3.2 Number of views on YouTube and number of tourists arriving**  
  
- The data I gathered gave me the information of arrivals per year, so I had to take into consideration the sum of all yearly YouTube views for each place in order to compare the two pieces of information. As mentioned before, for some places I couldn't find data for 2021 and/or 2022, so unfortunately this part of the analysis has missing information. Below, we can see the plots for tourist arrivals x yearly youtube views and the Pearson correlation coefficient for this two variables in the period of the last 5 years:  
  
  
  
  
  
**Correlation coefficient:**  0.1
 
 ![thai_tourism](https://user-images.githubusercontent.com/109185207/218336923-e3851d1d-2d17-42ac-b150-f5d31546459d.png)
---
 
 
 
  **Correlation coefficient:**  0.31

 ![india_tourism](https://user-images.githubusercontent.com/109185207/218336863-c20fccc5-0830-4cb6-bbbc-e29a98ae868e.png)
---


  
 **Correlation coefficient:** -0.51 

![mexico_tourism](https://user-images.githubusercontent.com/109185207/218336963-6d851e9c-e801-414b-a05b-e897ee524040.png)
---

 

**Tourism data in this case refers to Iran as a whole and not just Tabriz because this information was not available online. Even taking into consideration the entire country, the data for 2021 and 2022 couldn't be found.**  
  
**Correlation coefficient:** For this particular case it made no sense to calculate it because there was a single data point for YouTube views since neither before nor after 2020 any of the YouTube channels analyzed mentioned Tabriz.
 
![tabriz_tourism](https://user-images.githubusercontent.com/109185207/218337093-15bc8060-9a7d-43ac-b987-c59c0fc1a997.png)
---
 


 **Correlation coefficient:** Another case in which it would make no sense to calculate it because of the amount of data available.
  
![pakistan_tourism](https://user-images.githubusercontent.com/109185207/218337154-736ade16-76fb-40f7-9523-d79285b16e68.png)
---

  
 **Correlation coefficient:** 0.2 

![arizona_tourism](https://user-images.githubusercontent.com/109185207/218337221-304b5eb1-8ad2-4624-b890-1907b6e23714.png)
---
 
 
 **Correlation coefficient:** 0.15 
   
 ![california_tourism](https://user-images.githubusercontent.com/109185207/218337254-c24d16b6-2018-4240-b165-739b6865c1fa.png)
---

  


  
    
**`Second considerations:`**  

---  
  
  
### 4. Final conclusions

