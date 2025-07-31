import streamlit as st
import pandas as pd
import plotly.express as px

# leer el archivo CSV
car_data_df = pd.read_csv('vehicles_us.csv')

# Encabezado del programa
st.header('Dashboard de vehículos usados en EE. UU.')

# Boton para construir el histograma
show_hist = st.checkbox("Mostrar histograma de odometro")

if show_hist:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de ventas de coches.')
    fig = px.histogram(car_data_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

    # Calcular los 10 odometros mas frecuentes
    top_odometer = car_data_df['odometer'].value_counts().reset_index()
    top_odometer.columns = ['Odometer (km)', 'Frecuencia']

    # se agrega DataFrame con Odometros mas frecuentes
    st.subheader('Top 10 Odometros mas frecuentes')
    st.dataframe(top_odometer.head(10))

# Boton para la construir el grafico de dispersion
show_scatter = st.checkbox("Mostrar grafico de dispersion (precio vs. odometro)")

if show_scatter:
    st.write("Relacion entre kilometraje (odometro) y precio del vehiculo")
    fig2 = px.scatter(car_data_df, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader('Vista previa de los datos')
    st.dataframe(car_data_df[['odometer', 'price']].head(10))

# se muestra el grafico de lineas
show_line = st.checkbox("Mostrar grafico de lineas de precio promedio por año")

if show_line:

    # Agregamos botos deslizante para elegir año de modelo de vehiculo
    min_year = int(car_data_df['model_year'].min())
    max_year = int(car_data_df['model_year'].max())

    year_range = st.slider("Selecciona el rando de años del modelo del vehiculo", min_year, max_year, (2010, 2020))

    # Se filtran los datos y se calcula el promedio del precio
    filtered_data = car_data_df[
        (car_data_df['model_year'] >= year_range[0]) & 
        (car_data_df['model_year'] <= year_range[1])
    ]

    price_by_year = filtered_data.groupby('model_year')['price'].mean().reset_index()

    fig3 = px.line(price_by_year, x='model_year', y='price', title='Precio promedio por año del modelo')
    st.plotly_chart(fig3, use_container_width=True)




