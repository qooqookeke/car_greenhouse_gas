import streamlit as st
import pandas as pd
import numpy as np

def run_loc_app():
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')

    st.subheader('병원 위치 및 대표전화')

    df_search = df.iloc[:,[1,10,11,12,28,29]]
    df_search = df_search.rename(columns={'요양기관명':'병원명','좌표(Y)':'lat','좌표(X)':'lon'})
    df_search = df_search[['병원명','주소','전화번호','병원홈페이지','lat','lon']]
    df_search['병원홈페이지'] = df_search['병원홈페이지'].fillna('-')
    
    #
    search_hos = st.text_input(label='병원명 검색')
    hos_name = df_search['병원명'].str.contains(search_hos)
    df2 = df_search.loc[hos_name]

    ##
    df2.loc[:,'lat':'lon'].dropna()
    mapdata = df2.loc[:,'lat':'lon'].dropna()
    st.map(mapdata)

    ###
    st.dataframe(df2.loc[:,['병원명', '주소', '전화번호','병원홈페이지']])
