### **Ejercicio 1: Dashboard Interactivo Simple**

##Utilizando el dataset proporcionado (`dashboard_simple_data.csv`), crea un dashboard interactivo con los siguientes elementos:

##1. **Título y Subtítulo**: Añade un título claro y un subtítulo descriptivo.
##2. **Filtro Básico**: Utiliza un filtro para seleccionar una de las categorías (A, B o C).
##3. **Visualización Básica**: Muestra una visualización básica (como un gráfico de barras) que muestre el total de valores por fecha para la categoría seleccionada.

import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import altair as alt

# Crear un DataFrame de ejemplo
df=pd.read_csv('dashboard_simple_data.csv')

## 1
st.title  ("Dashboard Ventas ")
st.header ("Ventas por Fecha")

## 2
st.sidebar.header('Filtros')
categoria = st.sidebar.multiselect('Selecciona Categoria : ',df['Categoria'].unique())
#st.write(f"Categoria seleccionada {categoria}")


# Filtrar datos según selección
df_filtrado = df.copy()
df_filtrado = df_filtrado[df_filtrado['Categoria'].isin(categoria)]


# Visualización 1: Gráfico de Barras de Ventas por Producto
fig1 = px.bar(df_filtrado, x='Fecha', y='Valor', title=f"Categoria seleccionada {categoria}")
st.plotly_chart(fig1)
