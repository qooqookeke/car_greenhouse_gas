import streamlit as st
import pandas as pd

def run_loc_app():
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')

    df_search = df.iloc[:,[1,10,11,12,28,29]]
    df_search = df_search.rename(columns={'요양기관명':'병원명','좌표(Y)':'lat','좌표(X)':'lon'})
    df_search = df_search[['병원명','주소','전화번호','병원홈페이지','lat','lon']]
    df_search = df_search.fillna('-')

    search_hos = st.text_input(label='병원 이름 검색')
    search_word = list(search_hos)
    print(search_word)
    hos_name = df_search['병원명']
    hos_name[1].split()
    print(list(hos_name))
    print(search_word)
    
    if len(search_hos) != 0:
        search_data = df_search[df_search['병원명'].isin([search_word])]
        st.dataframe(search_data)   
    else:
        st.text('')
    
    # map_data = pd.dataFrame(np.random.rand(1,2)/[50,50] + maplatlon, columns=['lat', 'lon']) 
    # if df_search.loc[:,['lat','lon']].isin(['-']):
    #     st.map(None)
    # st.map(data=df_search, )