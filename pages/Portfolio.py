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



st.set_page_config(
        page_title="Portfolio",
        layout="wide",
        initial_sidebar_state="expanded",)
st.title("Gary Portfolio")
image  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\AdobeStock_185294016.jpg')
st.image(image, use_column_width=True)

