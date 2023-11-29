import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

plt.rcParams['font.family'] = 'NanumGothic'

def run_info_app():
    
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    df = df.iloc[:,1:28]
    
    #
    st.subheader('지역별 병원수 비율')
    loc1 = df['시도코드명'].value_counts()
    loc1 = loc1.to_frame().reset_index()
    loc1 = loc1.rename(columns={'시도코드명':'시도','count':'갯수'})
        
    chart1 = px.pie(data_frame=loc1, names='시도', values='갯수',
                    title='각 지역별 병원수 비율 파이차트')
    chart1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(chart1, use_container_width=True, height=600)

    ## 
    doc_count = df['총의사수'].max()
    doc_max = df.loc[df['총의사수'] == df['총의사수'].max(), ]
    max_name = doc_max['요양기관명'].iloc[0]
    st.markdown(' 전국에서 가장 많은 의사가 있는 병원은')
    st.markdown(''':green[**{}**] 이며,'''.format(max_name))
    st.markdown('''의사 수는 :blue[**{}명**] 입니다.'''.format(doc_count))


    data11 = df.groupby('시도코드명')[['의과인턴 인원수', '치과인턴 인원수', '한방인턴 인원수']].sum()
    d1 = data11.sum(axis=1).sort_values(ascending=0)
    d1.columns = ['지역','인턴 수']
    st.dataframe(d1)







    #
    # st.subheader('시도별 병원의 갯수')
    # location = df['시도코드명'].value_counts().index
    # fig1 = plt.figure(figsize=(5,7))
    # sb.countplot(data=df, y='시도코드명', order=location)
    # plt.title('지역별 병원 수')
    # plt.xlabel('병원 수')
    # plt.ylabel('지역')
    # st.pyplot(fig1)