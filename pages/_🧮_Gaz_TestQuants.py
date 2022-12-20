import os
import ifcopenshell
from logging import warning
import streamlit as st
from tools import ifchelper
from tools import pandashelper
from tools import graph_maker

def makecsv(t, name):
    return t.to_csv(os.path.join(p, str(name) + '.csv'))

ifc_file = ifcopenshell.open('C:\\Users\\mccarthyg\\PycharmProjects\\Gaz_Python1\\FLB-ACM-XX-ZZ-M3-AR-000001_S0_P01.ifc')

p = 'C:\\Users\\mccarthyg\\Downloads\\Multiverse\\Python'

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



makecsv(test,'test')

