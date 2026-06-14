#Importando bibliotecas
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import plotly_express as px
from functions import function

#Importando dataframes
df = pd.read_csv('data/clean_asteroids_data.csv')
df_perigoso = pd.read_csv('data/dangest_asteroids.csv')
df_observation = pd.read_csv('data/observation_year.csv')

#Configurando página e header
function.config("# ☄️ :blue[NASA Asteroids Dashboard]", "##### Análise interativa de asteroides próximos da Terra")

#Criando cards
num_asteroids = df['id'].count()
num_asteroids_danger = df_perigoso['id'].count()
diam_medio = df['diameter_medium'].round(2)
diam_max = diam_medio.max().round(2)
diam_medio = diam_medio.mean().round(2)

st.space(size="medium")

with st.container(horizontal=True, horizontal_alignment="center"):
    col1, col2, col3, col4 = st.columns(4, gap='large', width=1200)
    col1.metric(label="Total de Asteroides", value=num_asteroids, width=300)
    col2.metric(label="Total de Asteroides Perigosos", value=num_asteroids_danger, width=300)
    col3.metric(label="Diâmetro Médio", value=f'{diam_medio} m', width=300)
    col4.metric(label="Diâmetro Máximo", value=f'{diam_max} m', width=300)
    style_metric_cards(background_color="#0B1E3A", border_color='0B1E3A')

#Criando gráfico com Plotly
fig_observation = px.line(df_observation, x='observation_year', y='amount', title='Observações De Asteroides Por Ano', labels={'observation_year': 'Ano', 'amount': 'Quantidade'}, template='plotly_dark')
fig_observation.update_layout(
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
fig_observation.update_traces(line=dict(width=3))
st.plotly_chart(fig_observation)

st.markdown('> Obs: O número de observações aumentou fortemente após 1995.')

st.space('large')

st.markdown('#### Dataframe Asteroides')
function.filtros(df)