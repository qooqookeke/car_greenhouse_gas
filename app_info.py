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
    st.subheader('지역별 병원 비율')
    loc1 = df['시도코드명'].value_counts()
    loc1 = loc1.to_frame().reset_index()
    loc1 = loc1.rename(columns={'시도코드명':'시도','count':'갯수'})
        
    chart1 = px.pie(data_frame=loc1, names='시도', values='갯수',
                    title='각 지역별 병원 수 비율 파이차트')
    chart1.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(chart1, use_container_width=True, height=600)

    st.text(' ')

    # 지역별 바 차트
    # df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    df02 = df.groupby('시도코드명')['총의사수'].sum()
    df00 = df02.to_frame().reset_index(drop=0)
    print(type[df00])
    fig = px.bar(df00, x='시도코드명', y='총의사수', text_auto='S',
            title="지역별 총 의사수 바 차트")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)


    st.text(' ')
    st.subheader('지역별 인턴, 레지던트 인원수')
    data01 = df.groupby('시도코드명')[['의과인턴 인원수', '치과인턴 인원수', '한방인턴 인원수','의과레지던트 인원수','치과레지던트 인원수','한방레지던트 인원수']].sum()
    data01['인턴 총 인원수'] = data01.iloc[:,1:4].sum(axis=1)
    data01['레지던트 총 인원수'] = data01.iloc[:,4:7].sum(axis=1)
    data01 = data01[data01['인턴 총 인원수'] != 0]
    st.dataframe(data01)
    
    st.text(' ')
    i_cnt = data01['인턴 총 인원수'].max()
    r_cnt = data01['레지던트 총 인원수'].max()
    d_cnt = i_cnt + r_cnt
    i_mcnt = data01['인턴 총 인원수'].min()
    r_mcnt = data01['레지던트 총 인원수'].min()
    d_mcnt = i_mcnt + r_mcnt
    doc_max = data01.loc[data01['인턴 총 인원수']+data01['레지던트 총 인원수'] == d_cnt].reset_index(drop=0)
    max_name = doc_max.iloc[0,0]
    doc_min = data01.loc[data01['인턴 총 인원수']+data01['레지던트 총 인원수'] == d_mcnt].reset_index(drop=0)
    min_name = doc_min.iloc[0,0]
    dd = round(d_cnt/d_mcnt, 2)
    # st.info('전국에서 가장 많은 의사가 있는 병원은\n "{}" 이며, \n 의사 수는 "총 {}명" 입니다.'.format(max_name, doc_count) ,icon='ℹ️')
    st.markdown(' 가장 많은 인턴과 레지던트 의사가 있는 지역은')
    st.markdown(''':green[*{}*] 이며, 인턴 :orange[**{}**] 명, 레지던트 :orange[**{}**] 명으로 총 :blue[**{}**] 명 입니다.'''.format(max_name, i_cnt, r_cnt, d_cnt))
    st.text(' ')
    st.markdown('''가장 적은 지역인 :violet[*{}*]의 인턴과 레지던트 수는 총 :blue[**{}**] 명 으로'''.format(min_name, d_mcnt))
    st.markdown(''':green[*{}*]과 약 :red[***{}배***] 차이가 납니다.'''.format(max_name, dd))

    
    # choice2 = st.checkbox('지역 선택', df['시도코드명'].unique())
    # count2 = data01.loc[choice2, ['인턴 총 인원수','레지던트 총 인원수']].sum(axis=1)
    
    data03 = data01.reset_index(drop=0)

    # st.dataframe(data03)
    # print(type[data01])
    # data01 = px.data.tips()
    # fig1 = st.bar_chart(data03, x="시도코드명", y="인턴 총 인원수", z="레지던트 인원수",
    #          height=400)
    # st.plotly_chart(fig1)





    #
    # st.subheader('시도별 병원의 갯수')
    # location = df['시도코드명'].value_counts().index
    # fig1 = plt.figure(figsize=(5,7))
    # sb.countplot(data=df, y='시도코드명', order=location)
    # plt.title('지역별 병원 수')
    # plt.xlabel('병원 수')
    # plt.ylabel('지역')
    # st.pyplot(fig1)
    
    
    # st.subheader('지역별 의사 수')
    # data00 = df.groupby('시도코드명')[['총의사수','의과인턴 인원수', '치과인턴 인원수', '한방인턴 인원수','의과레지던트 인원수','치과레지던트 인원수','한방레지던트 인원수']].sum()
    # choice = st.selectbox('지역 선택', df['시도코드명'].unique())
    # count = data00.loc[choice,'총의사수']
    # st.markdown('{} 지역의 총 의사수는 {}명 입니다.'.format(choice, count))