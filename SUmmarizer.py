# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:54:04 2021

@author: rrust
"""
import streamlit as st
from transformers import pipeline 




    
@st.cache(allow_output_mutation=True)
def instantiate_generator():
    summarizer= pipeline('summarization')
    return summarizer

if __name__ == '__main__':
    st.title('Text Summarizer')
    starting_text = st.text_area('Let GPT-2 Summarize the text for you.')
    summarizer = instantiate_generator()
    
    if st.sidebar.button('About Project'):
        st.sidebar.write('The project is built on the transformers model imported by huggingface')
        st.sidebar.write('The Transformer in NLP is a novel architecture that aims to solve sequence-to-sequence tasks while handling long-range dependencies with ease. The Transformer was proposed in the paper Attention Is All You Need. It is recommended reading for anyone interested in NLP.')

    if st.sidebar.button('About Developer'):
        st.sidebar.write('Hi my name is Rahul Rustagi and I am a university of Michigan certified data science professional . Most of my projects and training have been centered around the concept of automation and improved system usability. Not only do I have experience in building and optimization of machine learning and deep learning models ,I also have experience in their front end development and cloud deployment on services like Azure ,GCP and AWS.  ')
        st.sidebar.write('Linkedin profile - https://www.linkedin.com/in/rahul-rustagi-4a1836133/ ')
        st.sidebar.write('Github profile - https://github.com/rrustagi9 ')
    if st.button('summarize'):
        response=[]
        
        
        if starting_text:
            response.appned(summarizer(starting_text)[0]['summary_text'])
            
            st.markdown('Summary:',[response][0])
            st.balloons()