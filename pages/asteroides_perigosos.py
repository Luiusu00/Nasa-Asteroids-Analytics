#Importando bibliotecas
import streamlit as st
import pandas as pd
import plotly_express as px
from functions import function

#Importando dataframes
df_perigoso = pd.read_csv('data/dangest_asteroids.csv')

#Configurando página e header
function.config("# ⚠️ :blue[Asteroides Perigosos]", "##### Análise interativa de asteroides potencialmente perigosos")

st.space(size="medium")

#Gráfico de Barras - Top 10 Asteroides Perigosos
df_perigoso['diameter_medium'] = df_perigoso['diameter_medium'].round(2)
top10 = df_perigoso.iloc[0:10]
fig = px.bar(top10, x='diameter_medium', y='short_name', orientation='h', title='10 Asteroides Mais Perigosos', color='diameter_medium', labels={'short_name': 'Nome', 'diameter_medium': 'Diâmetro Médio (m)'}, height=800)
fig.update_layout(
    paper_bgcolor='#050816',
    plot_bgcolor='#050816'
)
st.plotly_chart(fig)

st.space('large')

st.markdown('#### Dataframe Asteroides Perigosos')
function.filtros(df_perigoso)