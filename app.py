import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Proyecto 7 - Herramientas de Desarrollo de Software')


st.write('Mi nombre es Juan Ignacio')
st.write('https://github.com/Juaniod/notebooks')

import streamlit as st

st.header('Lanzar una moneda')

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')