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

    ##
    # st.subheader('전국기준 가장 많은 의사가 있는 병원')
    # st.text(' ')
    doc_count = df['총의사수'].max()
    doc_max = df.loc[df['총의사수'] == df['총의사수'].max(), ]
    max_name = doc_max['요양기관명'].iloc[0]
    st.info('전국에서 가장 많은 의사가 있는 병원은\n "{}" 이며, \n 의사 수는 "총 {}명" 입니다.'.format(max_name, doc_count) ,icon='ℹ️')
    # st.markdown(' 전국에서 가장 많은 의사가 있는 병원은')
    # st.markdown(''':green[**{}**] 이며,'''.format(max_name))
    # st.markdown('''의사 수는 :blue[**{}명**] 입니다.'''.format(doc_count))
    st.text(' ')

    # 지역별 바 차트
    # import plotly.express as px

    # df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    # fig = px.bar(df, y='pop', x='country', text_auto='.2s',
    #         title="Controlled text sizes, positions and angles")
    # fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # fig.show()

    st.subheader('지역별 의사 수')
    data00 = df.groupby('시도코드명')[['총의사수','의과인턴 인원수', '치과인턴 인원수', '한방인턴 인원수','의과레지던트 인원수','치과레지던트 인원수','한방레지던트 인원수']].sum()
    choice = st.selectbox('지역 선택', df['시도코드명'].unique())
    count = data00.loc[choice,'총의사수']
    st.markdown('{} 지역의 총 의사수는 {}명 입니다.'.format(choice, count))



    st.text(' ')
    st.subheader('지역별 인턴, 레지던트 인원수')
    data00 = df.groupby('시도코드명')[['의과인턴 인원수', '치과인턴 인원수', '한방인턴 인원수','의과레지던트 인원수','치과레지던트 인원수','한방레지던트 인원수']].sum()
    data00['인턴 총 인원수'] = data00.iloc[:,1:4].sum(axis=1)
    data00['레지던트 총 인원수'] = data00.iloc[:,4:7].sum(axis=1)
    st.dataframe(data00)
    

    
    choice2 = st.checkbox('지역 선택', df['시도코드명'].unique())
    count2 = data00.loc[choice, ['인턴 총 인원수','레지던트 총 인원수']].sum(axis=1)
    
    # import plotly.express as px
    # df = px.data.tips()
    # fig = px.histogram(df, x="sex", y="total_bill",
    #          color='smoker', barmode='group',
    #          height=400)
    # fig.show()





    #
    # st.subheader('시도별 병원의 갯수')
    # location = df['시도코드명'].value_counts().index
    # fig1 = plt.figure(figsize=(5,7))
    # sb.countplot(data=df, y='시도코드명', order=location)
    # plt.title('지역별 병원 수')
    # plt.xlabel('병원 수')
    # plt.ylabel('지역')
    # st.pyplot(fig1)