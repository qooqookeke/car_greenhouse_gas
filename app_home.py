import streamlit as st
import pandas as pd
from PIL import Image

def run_home_app():
    st.text('지역별 병원 정보와 의료 불균형을 분석한 앱입니다.')
    
    #
    img = Image.open('./img/medical-5459654_1280.png')
    st.image(img, width=250)
    st.text(' ')
    
    ##
    st.subheader('의료 불균형 관련 기사')
    st.link_button('비수도권 의대생 절반, 졸업 후 수도권 병원서 인턴', 'https://www.yna.co.kr/view/AKR20231125028500530?input=1195m')
    st.link_button('지방은 레지던트도 못구한다…2명 중 1명 ‘서울 근무’', 'http://news.heraldcorp.com/view.php?ud=20231018000266')
    st.link_button('지역별 "의료불균형"에 영아사망률 최대 1.6배 격차', 'https://www.yna.co.kr/view/AKR20231117140100530?input=1195m')
    st.text(' ')
    
    ###
    st.subheader('공공데이터 활용')
    st.link_button('데이터 출처','https://opendata.hira.or.kr/op/opc/selectOpenData.do?sno=11925&publDataTpCd=&searchCnd=&searchWrd=%EC%A0%84%EA%B5%AD&pageIndex=1')

    ####
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    df = df.iloc[:,1:]
    if st.checkbox('전국 병원 데이터 보기'):
        st.dataframe(df)
    else:
        st.text('')