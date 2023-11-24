import streamlit as st

from app_home import run_home_app
from app_info import run_info_app
from app_loc import run_loc_app

def main():
    st.title('전국 병원 정보')


    menu = ['홈', '지역별 병원', '병원위치']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0]:
        run_home_app()
    elif choice == menu[1]:
        run_info_app()
    elif choice == menu[2]:
        run_loc_app()

if __name__ == '__main__':
    main()