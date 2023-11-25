import streamlit as st
import pandas as pd
from PIL import Image

def run_home_app():
    st.text('이 앱은 전국의 병원 데이터를 모아둔 곳입니다.')

    img = Image.open('./img/medical-5459654_1280.png')
    st.image(img)
    
    st.subheader('공공데이터')
    st.link_button('데이터 보러가기','https://opendata.hira.or.kr/op/opc/selectOpenData.do?sno=11925&publDataTpCd=&searchCnd=&searchWrd=%EC%A0%84%EA%B5%AD&pageIndex=1')

    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    df = df.iloc[:,1:]
    st.dataframe(df)