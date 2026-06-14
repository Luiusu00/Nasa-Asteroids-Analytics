#Importando bibliotecas
import streamlit as st

pg = st.navigation(
    [
        st.Page("pages/panorama.py", title="Panorama", icon='☄️'),
        st.Page("pages/analise_observacoes.py", title="Análises de Observações", icon='🔭'),
        st.Page("pages/asteroides_perigosos.py", title="Asteroides Perigosos", icon='⚠️'),
    ]
)

pg.run()