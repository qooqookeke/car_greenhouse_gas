import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_info_app():
    st.header('지역별 병원 현황')

    st.subheader('공공데이터')
    st.link_button('데이터 보러가기','https://opendata.hira.or.kr/op/opc/selectOpenData.do?sno=11925&publDataTpCd=&searchCnd=&searchWrd=%EC%A0%84%EA%B5%AD&pageIndex=1')

    