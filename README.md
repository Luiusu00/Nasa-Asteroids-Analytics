# ☄️ NASA Asteroids Analytics Dashboard
 
<div align="center">
![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
 
**Análise interativa de asteroides próximos da Terra utilizando dados oficiais da NASA**
 
</div>
---
 
## 📌 Sobre o Projeto
 
Este projeto é uma aplicação completa de **análise de dados** que explora o catálogo de asteroides próximos da Terra (NEOs — Near-Earth Objects) disponibilizado pela NASA. O pipeline cobre desde a coleta e tratamento dos dados até a visualização interativa em um dashboard web construído com Streamlit.
 
O projeto foi desenvolvido como peça de portfólio para demonstrar habilidades em **Análise de Dados**, **Visualização**, **ETL com Python** e **desenvolvimento de dashboards**.
 
---
 
## 🚀 Funcionalidades
 
- **Panorama Geral** — KPIs com total de asteroides, quantidade de asteroides perigosos, diâmetro médio e diâmetro máximo; gráfico de linha com evolução das observações ao longo dos anos.
- **Análise de Observações** — Gráfico de área comparando asteroides perigosos vs. não perigosos por ano; scatter plot de Magnitude × Diâmetro Médio.
- **Asteroides Perigosos** — Ranking dos 10 asteroides potencialmente perigosos com maior diâmetro; dataframe interativo com filtros dinâmicos por nome, magnitude, diâmetro e data.
---
 
## 🗂️ Estrutura do Projeto
 
```
nasa-asteroids-analytics/
│
├── app.py                          # Ponto de entrada da aplicação Streamlit
│
├── pages/
│   ├── panorama.py                 # Página de visão geral
│   ├── analise_observacoes.py      # Página de análise temporal
│   └── asteroides_perigosos.py     # Página de asteroides perigosos
│
├── functions/
│   └── function.py                 # Funções reutilizáveis (config, filtros)
│
├── data/
│   ├── asteroids_data.csv          # Dados brutos da NASA API
│   ├── clean_asteroids_data.csv    # Dados tratados
│   ├── dangest_asteroids.csv       # Asteroides potencialmente perigosos
│   └── observation_year.csv        # Observações agregadas por ano
│
├── notebooks/
│   └── geral_nasa.ipynb            # EDA e pipeline de transformação
│
├── graphic/
│   ├── 10_Asteroids_Dangerous.png
│   └── Observation_Asteroids_perYear.jpg
│
└── requirements.txt
```
 
---
 
## 🛠️ Tecnologias Utilizadas
 
| Tecnologia | Uso |
|---|---|
| **Python 3.14** | Linguagem principal |
| **Pandas** | Manipulação e transformação de dados |
| **Plotly Express** | Visualizações interativas |
| **Streamlit** | Framework do dashboard web |
| **Jupyter Notebook** | Análise exploratória e ETL |
| **NASA NeoWs API** | Fonte dos dados |
 
---
 
## 📊 Pipeline de Dados
 
```
NASA API → asteroids_data.csv
              ↓
       [Jupyter Notebook]
       - Conversão de tipos (datetime)
       - Tratamento de valores nulos (short_name)
       - Criação da coluna diameter_medium
       - Filtragem de asteroides perigosos
       - Agregação por ano de observação
              ↓
   clean_asteroids_data.csv
   dangest_asteroids.csv
   observation_year.csv
              ↓
     [Streamlit Dashboard]
```
 
---
 
## ⚙️ Como Executar
 
### Pré-requisitos
 
- Python 3.9+
- pip
### Instalação
 
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/nasa-asteroids-analytics.git
cd nasa-asteroids-analytics
 
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
 
# Instale as dependências
pip install -r requirements.txt
```
 
### Executando a aplicação
 
```bash
streamlit run app.py
```
 
Acesse `http://localhost:8501` no navegador.
 
---
 
## 📈 Principais Análises e Insights
 
- **Explosão de descobertas pós-1995:** o número de asteroides registrados aumentou drasticamente após 1995, impulsionado por programas de monitoração automatizados como o LINEAR e o Catalina Sky Survey.
- **Pico de asteroides perigosos entre 2000 e 2005:** período com maior concentração de PHAs (Potentially Hazardous Asteroids) catalogados pela primeira vez.
- **Relação inversa entre tamanho e magnitude:** asteroides maiores tendem a ter magnitude menor (brilho aparente mais alto), comportamento esperado pela física da reflexão de luz.
- **Top 3 asteroides mais perigosos por diâmetro:** Florence (≈6.569 m), Cuno (≈6.273 m) e QS52 (≈5.882 m).
---
 
## 🗃️ Fonte dos Dados
 
Os dados foram obtidos via **[NASA NeoWs (Near Earth Object Web Service)](https://api.nasa.gov/)**, API pública da NASA que fornece informações sobre asteroides próximos da Terra, incluindo dados orbitais, diâmetros estimados e registros de aproximação.
 
---
 
## 👨‍💻 Autor
 
Desenvolvido por **[Seu Nome]**
 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario)
 
---
 
<div align="center">
  <sub>Feito com 🪐 e dados da NASA</sub>
</div>
