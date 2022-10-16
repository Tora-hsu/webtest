import time


# import os
# os.environ['NUMEXPR_MAX_THREADS'] = '16'
import streamlit as st

import numpy as np
import pandas as pd


st.set_page_config(
    page_title="測試",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)


st.title('我的第一個應用程式')

st.write("嘗試創建**表格**：")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)


# option = st.selectbox(
#     '你喜歡哪種動物？',
#     ['狗', '貓', '鸚鵡', '天竺鼠'])
# '你的答案：', option

option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option

left_column,mean_column ,right_column = st.columns(3)
left_column.write("這是左邊欄位。")
mean_column.write("這是中間欄位。")
right_column.write("這是右邊欄位。")


expander = st.expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")

# 增加一個空白元件，等等要放文字
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'目前進度 {i+1} %')
    bar.progress(i + 1)
    time.sleep(0.01)

@st.cache(suppress_st_warning=True)
def expensive_computation(a):
    st.write(f"沒有快取：expensive_computation({a})")
    time.sleep(2)
    return a * 2

a = st.slider("選擇一個數字", 0, 10)
result = expensive_computation(a)
st.write("結果：", result)







