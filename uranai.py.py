import random
import streamlit as st
import pandas as pd
import time

st.title("今日の運勢を占いましょう")
kekka = ""
dice_sum = 0

if st.button("本日の運勢"):
    uranaiDice1 = random.randint(1, 10)  # 1-6までをランダムに生成
    uranaiDice2 = random.randint(1, 10)
    uranaiDice_sum = uranaiDice1 + uranaiDice2  # 2つの値を合計
    with st.spinner('占い中.'):
        time.sleep(3)	
   
    if uranaiDice_sum == 1:
        kekka = "大大吉"
    elif uranaiDice_sum >=2  and uranaiDice_sum <= 9:
        kekka = "小吉"
    elif uranaiDice_sum >= 10 and uranaiDice_sum <= 16:
        kekka = "中吉"
    else:
        kekka = "大吉"

st.write("占い結果: ", kekka)