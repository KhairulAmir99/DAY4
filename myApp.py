import streamlit as st

st.write('Hello')
st.write('Hello pantek')

st.markdown('streamlit *is really really cool*')
st.success('good')
st.warning('warning')

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)

select1 = st.selectbox("Kuala Lumpur is located at ",['Malaysia','Thailand','UK'])
st.multiselect("Select 2 states",['Selangor','Johor','Kedah'])
st.multiselect("Are you:",['Bodoh','Bangang','Bahalol'])

st.write("You have selected: ", select1)
c1 = st.button("Click here to proceed")

st2 = st.slider("You have click the button",1,4, value=1)
st.write("You are ",st2)
num = st.number_input("Insert a number ", value = 3, placeholder = "Type a number la babi.....")
st.write("The current number is", num)

from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampleData.xlsx')
st.dataframe(df)
st.bar_chart(df, x='Location',y='Income',x_label='Location1')
st.line_chart(df, x='Household', y='Income')
st.scatter_chart(df, x='Household', y='Income')
tab1, tab2, tab3 = st.tabs(['Cats', 'Dogs','Babi'])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Babi")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhVoYoLKufGfPnWI6UjkDT8O0h3qFjcLfFMQ&s", width=200)

col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.write('')

col4, col5, col6 = st.columns(3)

with col4:
    st.bar_chart(df, x='Location',y='Income',x_label='Location1')

with col5:
    st.write('')

with col6:
    st.select_slider("Choose",1,5,value=3)