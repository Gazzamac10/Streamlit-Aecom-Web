import os
import ifcopenshell
import pandas as pd
from logging import warning
import streamlit as st
from tools import ifchelper
from tools import pandashelper
from tools import graph_maker
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff

def makecsv(t, name):
    return t.to_csv(os.path.join(p, str(name) + '.csv'))

ifc_file = ifcopenshell.open('C:\\Users\\mccarthyg\\PycharmProjects\\Gaz_Python1\\FLB-ACM-XX-ZZ-M3-AR-000001_S0_P01.ifc')

p = 'C:\\Users\\mccarthyg\\Downloads\\Multiverse\\Python'

df1 = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv")

fig = px.scatter(
    df1,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

def get_ifc_pandas(ifcfile):
    data, pset_attributes = ifchelper.get_objects_data_by_class(
        ifcfile,
        "IfcBuildingElement"
    )
    frame = ifchelper.create_pandas_dataframe(data, pset_attributes)
    return frame

df =  (get_ifc_pandas(ifc_file))

testClasses = df["Class"].value_counts().keys().tolist()

test = pandashelper.filter_dataframe_per_class(df, testClasses[1])

#makecsv(test,'test')

st.set_page_config(
        page_title="Gaz_Quantities",
        layout="wide",
        initial_sidebar_state="expanded",)
image  = Image.open('C:\\Users\\mccarthyg\\Downloads\\Multiverse\\Python\\pythonProject221214\\Aecomlogo.png')
st.image(image)
st.header(" 🧮 Model Quantities")
st.header("Step 1: Load a file from the Home Page")

graph = graph_maker.load_graph2(df1)
st.plotly_chart(graph)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: show;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)