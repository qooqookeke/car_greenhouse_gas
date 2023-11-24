import streamlit as st
import pandas as pd

def run_loc_app():
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')
    df_location = df.iloc[:,[28,29]]
    df_location = df.rename(columns={'좌표(Y)':'lat','좌표(X)':'lon'})
    df_location = df_location[['lat','lon']]
    df_location = df_location.dropna()

    st.dataframe(df_location)
    st.map(data=df_location, )