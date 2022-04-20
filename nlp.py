from gensim.summarization import summarize
import streamlit as st 

import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob 


text1 = "Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion. "

def text_process(mess):

    nopunc = [char for char in mess if char not in string.punctuation] #remove punct
    nopunc = ''.join(nopunc)
    
    word_seq=[word for word in nopunc.split() if word.lower() not in stopwords.words('english')] #remove stopwords
    
    # print(word_seq)

    text = re.sub('[^a-zA-Z]', ' ', str(word_seq))

    return text

lemmatizer = WordNetLemmatizer()

message = st.text_input("Enter Text",key='1')


if st.button("Summarize"):
    st.write('Summarize: ', summarize(message))

messagePreprocessing = st.text_input("Enter Text",key='2')

if st.button("Sentiment analysis"):
    blob = TextBlob(messagePreprocessing)
    result_sentiment = blob.sentiment
    st.write('Sentiment analysis: ', result_sentiment)   

messageTokenize = st.text_input("Enter Text",key='3')

if st.button("Text Prerocess"):
    st.write('Text Prerocess: ', text_process(messageTokenize))  

