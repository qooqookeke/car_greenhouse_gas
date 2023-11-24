import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

def run_info_app():
    st.header('지역별 병원 현황') 

    st.subheader('공공데이터')
    st.link_button('데이터 보러가기','https://opendata.hira.or.kr/op/opc/selectOpenData.do?sno=11925&publDataTpCd=&searchCnd=&searchWrd=%EC%A0%84%EA%B5%AD&pageIndex=1')

    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    st.dataframe(df)
    
    loc1 = df['시도코드명'].value_counts()
    loc1 = loc1.to_frame().reset_index()
    
    st.dataframe(loc1)
        
    chart1 = px.pie(data_frame=loc1, names='시도코드명', values='count',
                    title='각 지역별 병원 비율 파이차트')
    chart1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(chart1)