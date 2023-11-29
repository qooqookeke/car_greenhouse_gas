import streamlit as st
import matplotlib.pyplot as plt

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

from app_home import run_home_app
from app_info import run_info_app
from app_loc import run_loc_app

def main():
    st.title('지역별 병원 정보 및 의료 불균형 파악')


    menu = ['메인', '지역별 의료 불균형', '전국 병원 정보']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0]:
        run_home_app()
    elif choice == menu[1]:
        run_info_app()
    elif choice == menu[2]:
        run_loc_app()

if __name__ == '__main__':
    main()