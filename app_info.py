import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

def run_info_app():
    
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    df = df.iloc[:,1:28]
    st.header('지역별 병원 현황') 
    st.dataframe(df)
    
    st.subheader('시도별 병원의 갯수')
    location = df['시도코드명'].value_counts().index
    plt.rc('font', family='Malgun Gothic')
    fig1 = plt.figure(figsize=(7,9))
    sb.countplot(data=df, y='시도코드명', order=location)
    plt.title('지역별 병원 수')
    plt.xlabel('병원 수')
    plt.ylabel('지역')
    st.pyplot(fig1)
    
    st.subheader('지역별 병원수 비율')
    loc1 = df['시도코드명'].value_counts()
    loc1 = loc1.to_frame().reset_index()
    loc1 = loc1.rename(columns={'시도코드명':'시도','count':'갯수'})
        
    chart1 = px.pie(data_frame=loc1, names='시도', values='갯수',
                    title='각 지역별 병원수 비율 파이차트')
    chart1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(chart1)