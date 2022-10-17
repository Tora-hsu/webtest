import pandas as pd 
import streamlit as st
import datetime

d = st.date_input(
    "請選擇出發日期",
    datetime.datetime.now(),min_value=datetime.datetime.now(),max_value=datetime.datetime.now()+datetime.timedelta(days=183),help='請選擇出發日期')
st.write('您的出發日期是:', d)

x=pd.read_csv('./pages/airport3.csv')
# x1=x.values.tolist()#把機場名稱轉成list


option = st.selectbox(
    '請選擇出發州別',
    x['U.S'].unique())
    
fliter = (x['U.S'] == option)


option2 = st.selectbox(
    '請選擇出發機場',
    x[fliter]['airport'])



st.write('出發州別:', option ,'出發機場:',option2)

option3 = st.selectbox(
    '請選擇抵達州別',
    x['U.S'].unique())
    
fliter = (x['U.S'] == option3)


option4 = st.selectbox(
    '請選擇抵達機場',
    x[fliter]['airport'])

st.write('抵達州別:', option3 , '抵達機場:' ,option4)


if st.button('Say hello'):
    st.write('出發日期:',d+datetime.timedelta(days=1)   ,'出發地點:',option+" "+option2)
else:
    st.write('Goodbye')


# import os

# print (os.getcwd())
