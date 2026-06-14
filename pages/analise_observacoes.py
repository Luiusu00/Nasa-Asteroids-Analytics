#Importando bibliotecas
import streamlit as st
import pandas as pd
import plotly_express as px
from functions import function

#Importando dataframes
df = pd.read_csv('data/clean_asteroids_data.csv')

#Configurando página e header
function.config("# 🔭 :blue[Análises de Observações]", "##### Análise temporal de asteroides ao longo dos anos")

st.space(size="medium")

#Convertendo coluna para datetime e criando nova coluna ano
df['first_observation_date'] = pd.to_datetime(df['first_observation_date'])
df['observation_year'] = df['first_observation_date'].dt.year

#Criando novo df contando o número de asteroides por ano e seu respectivo potencial de perigo
df_area = df.groupby(['observation_year', 'potentially_hazardous'])['id'].count().reset_index()

#Renomeando colunas e criando uma coluna para ser a legenda do gráfico
df_area = df_area.rename(columns={
    'id': 'amount',
    'potentially_hazardous': 'danger'})

df_area['danger_label'] = df_area['danger'].map({
    True: 'Perigoso',
    False: 'Não Perigoso'
})

legenda_cores = {'Perigoso': 'red','Não Perigoso': 'blue'}

#Criando gráfico de área
st.markdown('#### Quantidade de asteroides ao longo do tempo')
fig_area = px.area(df_area, x='observation_year', y='amount', color='danger_label', labels={'observation_year': 'Ano de Observação', 'amount': 'Quantidade', 'danger_label': 'Potencial de Perigo'}, color_discrete_map=legenda_cores)
fig_area.update_layout(
        xaxis=dict(
        tickmode='linear',
        dtick=5
    ),
    yaxis=dict(
        tickmode='linear',
        dtick=20
    ),
    paper_bgcolor='#050816',
    plot_bgcolor='#050816'
)
st.plotly_chart(fig_area)
st.markdown('> Entre 2000 e 2005 houve um pico de asteroides perigosos registrados')

st.space('large')

df['Potencial de Perigo'] = df['potentially_hazardous'].map({True: 'Perigoso', False: 'Não Perigoso'})
labels = {
    'diameter_medium': 'Diâmetro Médio',
    'magnitude': 'Magnitude',
}

st.markdown('#### Magnitude x Diâmetro Médio')
scatter = px.scatter(df, x='diameter_medium', y='magnitude', size='diameter_medium', color='Potencial de Perigo', labels=labels, color_discrete_map=legenda_cores, opacity=0.5, hover_name='short_name')
scatter.update_layout(
        xaxis=dict(
        tickmode='linear',
        dtick=5000
    ),
    yaxis=dict(
        tickmode='linear',
        dtick=2
    ),
    paper_bgcolor='#050816',
    plot_bgcolor='#050816'
    )
st.plotly_chart(scatter)
st.markdown('> Quanto maior o tamanho do asteroide menor seu brilho (magnitude)')