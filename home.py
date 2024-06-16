import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py",),
        Section("Applications"),
        Page("pages/crop_recom_streamlitapp.py", "Prediction", "1️⃣", in_section=True),
        Page("pages/basic_sentiment_analyzer.py", "Sentiment Analysis", "2️⃣", in_section=True),
        Page("pages/img_classification.py", "Image Classification", "3️⃣", in_section=True),


        Section("SRCs"),
        Page("pages/crop_src.py", "Prediction Source", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "Sentiment Analysis Source", "2️⃣", in_section=True),
        Page("pages/image_classification_src.py", "Image Classification Source", "3️⃣", in_section=True),
]
)



st.markdown("""

##### About Me:
Good day! I am Nubben Christy O. Teñoso,  23 years old. I am currently pursuing a Bachelor of Science in Information Systems at Carlos Hilado Memorial State University. I live in Hda Sto Domingo Brgy Granada Bacolod City. I have two sisters and I am the middle child. To tell you about myself well  I'm just a simple girl who has a big dream  for her self and for my family I may not  that intelligent like others but I always give my best in everything, I like watching movies  especially the comedy and action. I'm also a bit of a foodie and love trying out new recipes and restaurants. It's great meeting new people who share similar interests in foods When I'm not studying, I love spending time with friends and family, and I'm always up for trying new things.        


##### 💻 Applications

* Prediction
* Sentiment Analysis
* Image Classification



### 🔎 Overview""", unsafe_allow_html=True)

st.markdown("""
For the whole Semester I learned  that Quantitative methods  emphasized the importance of accuracy and reliability in data collection and analysis, ensuring that conclusions are based on solid evidence. this course provided me with valuable skills in using quantitative data to understand and solve real-world problems effectively.

""", unsafe_allow_html=True)

st.markdown("""
For the Sentiment Analyzer as you can see in the first column  you need to put your Name. And then proceed to the next column which you need to classify your emotions. The Output we'll base on the sentence that you stated, it  should be equal to have the same outcome
""", unsafe_allow_html=True)


st.markdown("""
For The Image classification on  the right side it has a drop file button in which you can upload your files in PNG,JPG, JPEG, and it has also a limitations for each files which is 200 MB Peru file only. So once you uploaded the file the picture will showed.
""", unsafe_allow_html=True)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
