import streamlit as st
import pandas as pd
import plotly.express as px

# Ler os dados
car_data = pd.read_csv("vehicles.csv")

# Título do aplicativo
st.header("Análise de veículos")

# Texto
st.write("Visualização dos preços dos veículos.")

# Botão para criar o histograma
hist_button = st.button("Criar histograma")

if hist_button:
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig)
   
st.subheader("Preço dos veículos por condição")

fig_box = px.box(
    car_data,
    x="condition",
    y="price",  
    title="Preço dos veículos por condição"
)
    
st.plotly_chart(fig_box)

st.subheader("Relação entre preço e quilometragem")

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Preço dos veículos por quilometragem"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)