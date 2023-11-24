import streamlit as st
import pandas as pd

def run_loc_app():
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')

    st.text_input('병원 검색')
    df_search = df.iloc[:,[1,10,11,12,28,29]]
    df_search = df_search.rename(columns={'요양기관명':'병원이름','좌표(Y)':'lat','좌표(X)':'lon'})
    df_search = df_search[['병원이름','주소','전화번호','병원홈페이지','lat','lon']]
    df_search = df_search.fillna('-')
    
    
    st.dataframe(df_search)
    st.map(data=df_search, )