import streamlit as st


col1, col2,col3 = st.columns([2,1.2,0.7])
with col1:
    st.write('#')
    st.write('#')
    st.subheader("📊 Hey, there! I'm Mayara, a data analyst 📈")
    st.subheader(" Let me tell you why I'm not just another one ✨")
with col2:
    st.image("imgs/me.jpg")
    st.write('#')
st.write("""
I'm a 28-year-old Brazilian living in Barcelona and ever since I was a little kid, I've always been an extremely curious person. 
I used to drive my family crazy by constantly asking them questions
and reminding them that "because" was not a satisfactory answer.
I would finally get a good answer and run off to find someone I could share it with. I would try to teach my sister, my mom, my dad...
even my teacher. I remember writing this short book when I was about 7 or 8 to teach her about the power
of friendship!
\n\n
As you can see, finding answers and sharing them is deeply rooted in me, so no wonder I've become a data analyst.""")

st.markdown("""##### :red[My background is a bit more diverse, though:]
- My high school curriculum was integrated with a technical course on **Industrial Automation** which made me realize a career in STEM 
was something I really wanted. I loved all things technical.
\n
- Then, during college, I pursued a Bachelor's degree in **Control and Automation Engineering**. Lots of math, statistics and probability, 
programming in C, and specially A LOT of problem solving. 
\n
- Through this degree I was awarded with a **full scholarship in Dublin, Ireland**, oferred by the Brazilian government through a program 
called **Science Without Borders**. I studied 2 semesters in their **Control and Automation Systems** bachelor's. I had contact with a type
of teaching I had never seen before. It was project-based learning and it really pushed me out of my comfort zone.
\n
- Back to Brazil, because of personal reasons, I had to unfortunately quit my studies after nearly 4 years.
This forced me into a path that was uninmagined until that moment but that resonated with my personality as well: teaching.
""")

st.markdown("""##### :red[From STEM to teaching English. Why?]
For 6 years I taught English. It started as a first job when I had to quit college, but it became a true passion,
one I invested a lot of time and money to improve by constantly studying and working on my teaching techniques.
During this time, I had the opportunity to build incredibly strong connections with people from the most diverse backgrounds, 
**to learn how to actively listen in order to understand their goals and what they needed from me,
and mainly, to communicate and explain complex ideas better.** 
\n

Each student had specific challenges, goals and learning preferences. I had to understand where they were
and which strategies I needed to use to help them get where they wanted to be. I developed a personalized
plan for each one of them by using SMART goals and project-based teaching. **Being a teacher definitely helped me
to be able to indentify problems and challenges and come up with creative and innovative ways to overcome them.**

**Aren't these skills invaluable for a data analyst too?!**
\n
When I moved to Spain, I had been running my own business for a year and half already. 
Then, I realized it was time for a change, for something bigger, something different, but something I always wanted:
**a career in STEM.**
""")

st.markdown("""##### :red[Finally a Data Analyst. How?]
I did my fair share of research, talked to many different people in the industry, until
I decided data analytics was the right choice for me.
\n
That's when I enrolled into the **Data Analytics full-time bootcamp in-person at Ironhack Barcelona.** 
For 9 weeks (from October to December 2022), every day from 9am to 6pm (plus weekends and countless nights) I studied all the essential
tools to be a successful data analyst. 
\n 
Not only the technical skills such as **Python (Pandas, NumPy, Matplotlib, Plotly, NLTK, Requests, Re, among others), 
SQL, MongoDB, Tableau, Git and the basics of Machine Learning and Statistics**,
but, most importantly, how to make sense of all these tools and actually develop even further an analytical, inquisitive mindset. 
\n
During the bootcamp I could develop a number of projects to put these tools to the test,
and now, while I'm looking for an opportunity for a data analyst role, I'm still studying and developing my abilities even further.
I've recently completed an IBM certification on **Excel for Data Analysis** and have also been studying **PowerBI** on my own. 
\n
Besides, I'm in the second semester of an Associate's college degree on **Analysis and Development of Systems**
in which I'm studying the foundations of software engineering to create and improve systems, while also focusing on topics such as BI and Big Data.
I believe this degree - which is 100% remote and self-paced - will allow me to become a more complete data science professional. 
""")

col4, col5 = st.columns([2,1.5])
with col4:
    st.image("imgs/presentation-final.jpeg")

st.markdown("""##### :red[Last but not least]
Thank you so much for reading this far!
If you want to see some of my other projects you can check out my [GitHub here](https://github.com/Maya-Souza) (I'm currently working on my portfolio), or,
If you want to connect, here's my [LinkedIn](https://www.linkedin.com/in/mayara-almeida-souza/).
\n
As I mentioned, I'm looking for an opportunity to break into the Data Analytics world. If you think
I would be a good fit for your company, or if you know someone who is currently looking for a data analyst,
don't hesitate to contact me :)
\n
Below, you can download my resume if needed! 
\n
""")

with open("./imgs/Mayara_Data_Analyst_CV.pdf", "rb") as file:
    btn = st.download_button(
            label="Download my CV",
            data=file,
            file_name="Mayara_Data_Analyst_CV.pdf",
            mime=None,
            use_container_width=True
          )