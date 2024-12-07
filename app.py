import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Proyecto 7 - Herramientas de Desarrollo de Software')


st.write('Mi nombre es Juan Ignacio')
st.write('https://github.com/Juaniod/notebooks')

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if st.checkbox('Generar grafico de dispersion'): # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para la columna odómetro')

    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)


if st.checkbox('Generar grafico de barra'): # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de barra para la columna odómetro')

    fig = px.bar(car_data, x='odometer', y='price')
    st.plotly_chart(fig)

