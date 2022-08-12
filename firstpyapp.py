import streamlit as st
from PIL import Image

st.write('1st web app')


txt = st.text_area('Text to analyze', '''
     The Walrus or := operator is one of the latest additions 
     to python 3.8. It is an assignment operator that lets you 
     assign value to a variable within an expression like 
     conditional statements, loops, etc
     ''')
st.write('1. Walrus operator', run_sentiment_analysis(txt))


txt = st.text_area('another text to test', '''
     hey there, Am i below?
     ''')
st.write('2. not sure', run_sentiment_analysis(txt))