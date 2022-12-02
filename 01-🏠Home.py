import streamlit as st
st.set_page_config(layout="wide")


st.title("How far does the influence of travel youtubers go? 🌎")
st.markdown("#### _An analysis on the correlation between travel videos and their impact on people's interest and tourism._")
st.image('..\streamlit_files\imgs\youtube-users.png')


st.subheader("First, a bit of context! 📚")
st.write("The inspiration for this project came from two things I'm a big fan of: Youtube and traveling.")
st.write("I wanted to see if the places mentioned by famous travel youtubers in their videos have any impact on the 'real world', meaning, on people's online searches and on the number of tourists visiting the places mentioned.")

st.markdown("**You might be wondering: 'But YouTube is huge! How can you possibly check this?**")
st.write("The answer is: **I can't**! At least not with the _entirety_ of YouTube videos, of course! That's why I decided to sample some of the most famous travel channels and base my analysis on them.")

st.subheader("The data used 📁")
st.write("To find some of the most famous channels I simply used our old good friend Google and chose 11 different channels in total. It's important to mention that since the sample is small, a bias is inevitable.")
st.write("Besides that, I've only chosen English-speaking youtubers since some of the Python libraries needed for the analysis only recognized English. Therefore, another strong bias was inevitably added to the data: culture and language.")
st.write("One alternative to have a bigger sample size and more diversified videos would be to gather _general_ travel videos and not only from some specific channels. ")
st.write("However, all the data was collected by using the Youtube API, and for that I needed to be connected to my Google account. That meant that whenever I asked for videos about travel/tourism, YouTube sent me the ones it thought were relevant *to me*, which, obviously, was not ideal.")
st.write("So, in summary, bias is all around us and there's no escape! 🤷‍♀️")
st.markdown("**Before I explain what I did with these channels, you can check them out below:** ")
st.markdown("\n\n \n")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(r'../streamlit_files/imgs/drew.jpg')
with col2:
    st.image(r'../streamlit_files/imgs/yes.jpg')
with col3:
    st.image(r'../streamlit_files/imgs/mark.jpg')

col4, col5, col6 = st.columns(3)

with col4:
    st.image(r'../streamlit_files/imgs/samuel.jpg')
with col5:
    st.image(r'../streamlit_files/imgs/gone.jpg')
with col6:
    st.image(r'../streamlit_files/imgs/kara.jpg')

col7, col8, col9 = st.columns(3)

with col7:
    st.image(r'../streamlit_files/imgs/fearless.jpg')
with col8:
    st.image(r'../streamlit_files/imgs/kristen.jpg')
with col9:
    st.image(r'../streamlit_files/imgs/lost.jpg')

st.image(r'../streamlit_files/imgs/wolters.jpg', width=300)

st.markdown("\n \n \n With the channels selected, it was a matter of using various tools to analyse them: the Youtube API, Google Trends API and different databases for data on tourist arrivals and hotel occupancy rates.")

st.subheader("The methodology behind the analysis 🧑‍🔬")

st.markdown("- Extract and clean the data (YT API) ")
#st.markdown()
st.markdown("\n - Natural Language Processing (entity recognition through LocationTagger library) ")
st.markdown("\n - PyTrends API")
st.markdown("\n - Tourism data")


