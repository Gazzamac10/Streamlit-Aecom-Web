from logging import warning
import streamlit as st
from tools import ifchelper
from tools import pandashelper
from tools import graph_maker


session = st.session_state

def get_ifc_pandas():
    data, pset_attributes = ifchelper.get_objects_data_by_class(
        session.ifc_file,
        "IfcBuildingElement"
    )
    frame = ifchelper.create_pandas_dataframe(data, pset_attributes)
    return frame

print (get_ifc_pandas())