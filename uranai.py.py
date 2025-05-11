import random
import streamlit as st
import pandas as pd


st.title("今日の運勢を占いましょう")
kekka = ""

if st.button("運勢を占う"):
    dice1 = random.randint(1, 50)  # 1-6までをランダムに生成
    dice2 = random.randint(1, 50)
    dice_sum = dice1 + dice2  # 2つのサイコロの値を合計
   
    if dice_sum == 1:
        kekka = "大吉"
    if dice_sum >= 2 & dice_sum <= 49:
        kekka = "小吉"
    if dice_sum >= 50 & dice_sum <= 99:
        kekka = "中吉"
    if dice_sum == 100:
        kekka = "大大吉"

st.write("占い結果: ", kekka)