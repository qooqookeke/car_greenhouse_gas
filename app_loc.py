import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pydeck as pdk

def run_loc_app():
    df = pd.read_csv('./data/hospital_data.csv', encoding='euc-kr')

    df_loc = df.iloc[:,1:28]
    df_loc.iloc[:,4].unique()
    loc_name = df_loc.iloc[:,4].unique()
    selected_list = st.selectbox('지역을 선택하세요', loc_name)
    if len(selected_list) != 0:
        selected_data = df_loc[(df_loc['시도코드명'].isin([selected_list]))].reset_index(drop=True)
        st.dataframe(selected_data)
        order1 = selected_data['시군구코드명'].value_counts().head(10).index
        fig2 = plt.figure()
        sb.countplot(data= df, x='시군구코드명', order=order1)
        ax = sb.countplot(data=df, x='시군구코드명', order=order1)
        for p in ax.patches:
            height = p.get_height()
            ax.text(x = p.get_x() + p.get_width() / 2, 
                    y = height + 10, 
                    s = int(height), 
                    ha = 'center', 
                    size = 9)
        # ax.set_ylim(0, 3000)
        plt.title('시군구별 병원수 상위 10개')
        plt.xticks(rotation = 60)
        plt.xlabel('시군구')
        plt.ylabel('갯수')
        st.pyplot(fig2)
    else:
        st.text('')
        
    st.text('')


    df_search = df.iloc[:,[1,10,11,12,28,29]]
    df_search = df_search.rename(columns={'요양기관명':'병원명','좌표(Y)':'lat','좌표(X)':'lon'})
    df_search = df_search[['병원명','주소','전화번호','병원홈페이지','lat','lon']]
    df_search['병원홈페이지'] = df_search['병원홈페이지'].fillna('-')
    df2 = df_search.loc[hos_name]
    df2.loc[:,'lat':'lon'].dropna()
    mapdata2 = df2.loc[:,'lat':'lon'].dropna()

#    chart_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#    columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=mapdata2,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=mapdata2,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))


    
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
    st.dataframe(df2.loc[:,['병원명', '주소', '전화번호','병원홈페이지']],hide_index=1)
