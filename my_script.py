import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles.csv")

st.title("Análise de Veículos")

st.write(df)