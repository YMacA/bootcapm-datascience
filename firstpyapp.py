import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np  

st.header('10 Cool Beginner Python Tricks That Will Make Your Life Easier')


image = Image.open('minion.jpg')

st.image(image, caption='Sunrise by the mountains')

st.title('1. Walrus operator')
st.caption('Example')
st.text('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

code = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')
st.caption('Output')
code2 = ''' 3 '''
st.code(code2, language='python')
















st.write('st.dataframe Display a dataframe as an interactive table.')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.dataframe(df, 200, 100)
st.write('You can also pass a Pandas Styler object to change the style of the rendered DataFrame:')
df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

