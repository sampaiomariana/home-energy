from curses import def_prog_mode
import io
from os import write
from re import template
import tkinter
from turtle import left, right, title
from cv2 import sort
from numpy import average 
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title= "Dashboard",
                    page_icon=":bar_chart:",
                    layout= "wide")
def dash():
  #  st.subheader('Dashboard')

    df = pd.read_excel(
    io = 'consumo.xlsx',
    engine= 'openpyxl',
    skiprows=2,
    nrows=100,
    )

    #st.dataframe(df)


    #----SIDEBAR----

    st.sidebar.header("Filre aqui:")

    componente = st.sidebar.multiselect(
        "Selecione o componente:",
        options=df["componente"].unique(),
        default=df["componente"].unique()
    )


    id = st.sidebar.multiselect(
        "Selecione o id:",
        options=df["id"].unique(),
        default=df["id"].unique()
    )

    df_selection = df.query(
        "componente == @componente & id == @id"
    )

    #---MAIN---

    st.subheader(":bar_chart: Dashboard")
    st.markdown("##")

    #Indicadores

    total = int(df_selection["Jan"].sum())
    average_by = round(df_selection["Jan"].mean(),2)

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Consumo em janeiro")
        st.subheader(f"R$ {total:},")
    with right_column:
        st.subheader("Média por componente:")
        st.subheader(f" R$ {average_by}")

    st.markdown("---")

    consumo_componente_jan = (
         df_selection.groupby(by=["componente"]).sum()[["Jan"]].sort_values(by="Jan")
    )
    fig_product_jan = px.bar(
        consumo_componente_jan,
        x = "Jan",
        y = consumo_componente_jan.index,
        orientation = "h",
        title = "<b>Consumo por componente em Janeiro</b>",
        color_discrete_sequence=["#008388"] * len(consumo_componente_jan),
        template = "plotly_white",
    )

    st.plotly_chart(fig_product_jan)

    consumo_componente_fev = (
         df_selection.groupby(by=["componente"]).sum()[["Fev"]].sort_values(by="Fev")
    )
    fig_product_fev = px.bar(
        consumo_componente_fev,
        x = "Fev",
        y = consumo_componente_fev.index,
        orientation = "h",
        title = "<b>Consumo por componente em fevereiro</b>",
        color_discrete_sequence=["#008388"] * len(consumo_componente_fev),
        template = "plotly_white",
    )

    st.plotly_chart(fig_product_fev)

    consumo_componente_marc = (
         df_selection.groupby(by=["componente"]).sum()[["Mar"]].sort_values(by="Mar")
    )
    fig_product_marc = px.bar(
        consumo_componente_marc,
        x = "Mar",
        y = consumo_componente_marc.index,
        orientation = "h",
        title = "<b>Consumo por componente em março</b>",
        color_discrete_sequence=["#008388"] * len(consumo_componente_marc),
        template = "plotly_white",
    )

    st.plotly_chart(fig_product_marc)


#---HIDE STYLE---

hide_st_style = """
    <style>
    #MainMenu{visibility: hidden;}
    #footer {visibility: hidden;}
    #header{visibility: hidden;}
    </style>
"""

st.markdown(hide_st_style,unsafe_allow_html=True)