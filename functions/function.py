import streamlit as st
import pandas as pd

def config(title, subtitle):
    #Configurando página e header
    st.set_page_config(page_title='NASA Asteorids Dashboard', layout='wide')
    st.markdown(title, text_alignment='center')
    st.markdown(subtitle, text_alignment='center')

def filtros(df):
    #Definindo Filtros
    col1, col2, col3, col4 = st.columns(4)

    #Filtro do Nome do Asteroide
    filtro_nome = col1.selectbox(
        'Digite o Nome',
        options=df['short_name'].unique(),
        index=None,
        width=300
    )

    #Filtro da Magnitude do Asteroide
    filtro_mag = col2.slider(
        'Magnitude',
        min_value=float(df['magnitude'].min()),
        max_value=float(df['magnitude'].max()),
        width=300
    )

    #Filtro do Diâmetro do Asteroide
    filtro_diam = col3.slider(
        'Diâmetro Médio',
        min_value=float(df['diameter_medium'].min()),
        max_value=float(df['diameter_medium'].max()),
        width=300
    )

    #Convertendo coluna para datetime
    df['first_observation_date'] = pd.to_datetime(df['first_observation_date'])

    #Filtro Data de Observação
    filtro_date = col4.date_input(
        label='Data de Observação',
        value=df['first_observation_date'].min(),
        min_value=df['first_observation_date'].min(),
        max_value=df['first_observation_date'].max(),
        width=300
    )

    #Verificando as opções selecionadas por nome, se None então retornar todas os valores
    if filtro_nome is None:
        filtro_nome_cond = True
    else:
        filtro_nome_cond = df['short_name'] == filtro_nome

    #Fazendo o filtro no dataframe
    df_filtrado = df[(df['diameter_medium'] >= filtro_diam) &
                            (df['first_observation_date'] >= pd.to_datetime(filtro_date)) &
                            filtro_nome_cond &
                            (df['magnitude'] >= filtro_mag)]

    #Definindo colunas a ser mostrada e inserindo dataframe no dashboard
    colunas = ['name', 'short_name', 'magnitude', 'diameter_medium', 'first_observation_date']
    st.dataframe(df_filtrado[colunas], column_config={'name': 'Nome_Completo', 'short_name': 'Nome', 'magnitude': 'Magnitude', 'diameter_medium': 'Diâmetro_Médio', 'first_observation_date': 'Primeira_Observação'})