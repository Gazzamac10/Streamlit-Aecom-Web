import os
import ifcopenshell
import ifcopenshell.util.element as Element
import ifcopenshell.api
import pandas as pd
from logging import warning
import streamlit as st
from tools import ifchelper
from tools import pandashelper
from tools import graph_maker
from tools import SQLin
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

st.set_page_config (layout="wide")

# Add custom CSS styles
st.markdown(
    """
    <style>
        h1 {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 36px;
            text-align: center;
        }
        h2 {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 65px;
            text-align: center;
        }
        h3 {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: left;
        }
        h4 {
            font-weight: bold;
            color: White;
            font-family: Arial, sans-serif;
            font-size: 16px;
            text-align: left;
        }
        h5 {
            font-weight: bold;
            color: White;
            font-family: Arial, sans-serif;
            font-size: 16px;
            text-align: right;
        }
        p {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 16px;
            text-align: left;
            #margin-bottom: 24px;
        }
        p2 {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 16px;
            text-align: left;
            padding-left: 20px
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Add title
st.title("Gary McCarthy")
st.header("Data Fellowship Portfolio")
# Add image
image1  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\iStock_000070095321_Small.jpg')
st.image(image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)
# Add introduction
st.markdown("<h3>Introduction</h3>", unsafe_allow_html=True)
st.write("Welcome to the Data Analysis Level 4 Portfolio. This portfolio showcases the advanced data analysis skills \
and competencies that I have developed through the course, and demonstrates their potential value in a business context.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("I hope that this portfolio will provide a comprehensive overview of my skills and competencies, and will demonstrate my \
potential to contribute to the success of Aecom. I am confident that the skills and knowledge\
 I have gained through this course will be valuable and will enable me to make a positive impact in my role at Aecom.")

st.markdown("<h3>Personal Background</h3>", unsafe_allow_html=True)
st.markdown("<h4>Introduction to Aecom:</h4>", unsafe_allow_html=True)
st.write("I work for Aecom, a large, independent company that provides a wide range of professional services, including archaeology, architecture and design, urban planning, \
landscape architecture, asset management, construction, cost management, decommissioning and closure, economics, engineering, environmental services, international development,\
 IT and cyber security, operations and maintenance, planning and consulting, program management/construction management, risk management and resilience, and technical services. With over 86,000 employees worldwide,\
 Aecom's professional services revenue exceeds $13.2 billion, making it one of the largest corporations in the world.")
st.markdown("<h4>My Role:</h4>", unsafe_allow_html=True)
st.write("I am part of Aecom's buildings and places department, which focuses on architecture, building engineering, interiors, workplace master planning, and urban design. In this department, my colleagues and I are responsible for \
creating 3D models that include key design elements such as structural, electrical, and mechanical systems, and ensuring that all data is accurate and complete.")
st.markdown("<h4>Situation:</h4>", unsafe_allow_html=True)
st.write("The construction industry has made a transition over the years from simple 2D blueprint drawings to complex 3D data-rich models known as building information models (BIMs). These models include a variety of data points, such as material specifications, component costs, and construction and maintenance requirements, in addition to key design elements like structural, electrical, and mechanical elements.\
As part of the BIM team at Aecom, my role is to create and manage these models to ensure that all data is accurate and complete. Incomplete or erroneous data can have serious implications to the integrity of a structure and can be detrimental to the business and its stakeholders. With the digitization of the industry, it is becoming increasingly important for our team to not only create the data, but also to analyze it\
 in order to identify workflow inefficiencies or predictive patterns that could improve overall project delivery.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Project 1: Automated Data Extraction and Reporting for Building Information Models</h3>", unsafe_allow_html=True)
st.markdown("<h4>Objective</h4>", unsafe_allow_html=True)
st.write("The goal of this project is to develop a proof-of-concept automated workflow for extracting relevant data from BIMs and storing it in a database, \
as well as provide visual examples of what can be reported using this data. The ultimate aim is to improve productivity and profitability by streamlining data management and analysis processes within the BIM team.")
st.markdown("<h4>Tasks:</h4>", unsafe_allow_html=True)
st.markdown("<p2>- Review the API documentation for the BIM software and identify the relevant data points that can be extracted from the models.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Write a Python script that accesses the API and extracts the identified data points from all the elements in the model,\
 including a key element ID, element type, and element geometry.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Set up a database to store the extracted data and design the structure and schema to optimize data querying and analysis.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Use the Python script to populate the database with the extracted data.<p2>", unsafe_allow_html=True)
st.markdown("<p2>- Creating interactive visualizations and reports using the data stored in the database. This could involve using various software tools to create charts,\
 graphs, or other types of visualizations that <p2>highlight trends or patterns in the data.\The goal is to present the data in an easy to understand and meaningful way for stakeholders to make informed decisions.</p2>", unsafe_allow_html=True)
st.markdown("<h4>Outcomes:</h4>", unsafe_allow_html=True)
st.write("Upon completion of this project, I expect to have a functional proof-of-concept for an automated data extraction and reporting workflow for Building Information models. This will include a Python script that can extract data from the models and store it in a database, \
as well as visualizations or reports that demonstrate the potential of the data for identifying missing information, trends and patterns.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Brief overview of “Building Information modeling”</h3>", unsafe_allow_html=True)
image2  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\Bim2.jpg')
resized_image = image2.resize((1000, 500))
st.image(resized_image)
st.write("A Building Information Model (BIM) is a digital representation of a building or infrastructure project that contains structured, \
multi-disciplinary data throughout the entire life cycle of the building. BIM model is typically created using advanced software, which allows \
for the creation of a 3D model of a building with all the necessary information about the building's design, construction, and operation. \
This information can include architectural, structural, mechanical, electrical, and plumbing systems, as well as information about the materials used in the building.\
 BIM models can be used to extract and analyze data to identify patterns, inefficiencies, and potential issues in the building's design, construction, and operation.")
st.write("In terms of parameter information, BIM models can store a wide range of data points, including:")
st.markdown("<p2>- Spatial information, such as the location and size of different elements in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Geometric information, such as the shape and orientation of different elements.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Material information, such as the type and properties of materials used in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Component information, such as the type and properties of different building components.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Functional information, such as the intended use of different spaces in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Cost information, such as the cost of different materials and components used in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Maintenance information, such as the schedule and procedures for maintaining different building systems.</p2>", unsafe_allow_html=True)
st.write("This information can be used for cost estimation, schedule management, facility management, energy performance analysis, and many other purposes.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("Common Data Environment (CDE) is a mutually accessible online space where information in a BIM model is shared among all the stakeholders involved \
in a construction project. It serves as a central repository for all the project data, including design documents, specifications, cost estimates, schedules, \
and other relevant information. The CDE is used to manage, organize and store all the data throughout the project lifecycle, from planning and design to construction \
and operations. It ensures that all the stakeholders have access to the most current and accurate information, improving communication, collaboration and coordination \
among the different teams. The CDE also allows for version control and easy access to previous versions of the information model, making it easier to track changes and \
identify any issues that may arise during the project.")
image3  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\bim-level-2-spider.jpg')
resized_image = image3.resize((1000, 500))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h4>Actions:</h4>", unsafe_allow_html=True)
st.write("The first step in extracting and storing the relevant data from the BIM model was to identify the stakeholders who would be using the data and gather their \
specific needs and requirements. To do this, a meeting was held with Paul Witham, the BIM manager. During the meeting, Paul emphasized the importance of having the \
information accurate and up-to-date. Based on Paul's input, the available data points in the BIM model were reviewed, and those that were relevant to his needs were selected. \
Industry standards and best practices were consulted to ensure the data points chosen were appropriate.")
image4  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\Revit1.jpg')
resized_image = image4.resize((1200, 800))
st.image(resized_image)
st.write("The next step in the project was to determine the appropriate method for storing the data. After careful consideration, \
it was decided that using a SQLite database would be the most efficient option due to the lack of available company infrastructure for other database systems. \
To ensure that the data was stored in the most efficient way possible, an Entity Relationship Diagram (ERD) was created to establish the relationships between \
the different tables in the database. The data within the 3D model was structured, but when compared to data from other models, it was unstructured, \
so the ERD and database schema were designed to effectively store the data and support the queries and operations that would be performed on it.")
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\Figure3.jpg')
resized_image = image5.resize((1200, 800))
st.image(resized_image)
st.write("In order to save time, the decision was made not to fully normalize the database at this stage, but to return to the ERD when a long-term strategy \
for data storage had been established. In the meantime, the focus was on keeping the database as simple as possible by extracting each category of element into \
its own table, along with all relevant parameter values.")
st.write("The process of creating a script to batch export models to IFC files using Python was a multi-step process that included:")
st.markdown("<p2>- Importing necessary modules: The first step was to import the necessary modules or libraries in Python that were required for the script, \
including the BIM software's API module, the IFC export <p2>module, and any other necessary libraries for reading and manipulating data.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Connecting to the BIM software: The script established a connection to the BIM software using the API module by providing \
the necessary credentials and connecting to the software's API <p2>endpoint.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Identifying models to be exported: The script identified the models that needed to be exported by searching for models in a specific folder. \
All the models present in that folder were considered for <p2>export.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Extracting data: The script then used a loop to extract the necessary data from the identified models using the API's functions and methods.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Transforming data to IFC format: The data was then transformed to the IFC format using the IFC export module or library.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Error handling: The script included error handling to ensure that any issues that may occur during the process were properly \
handled and reported.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Testing the script: The script was tested with sample data to ensure that it was working as expected and that the exported models \
were in the correct format.o</p2>", unsafe_allow_html=True)
st.write("Overall, the process of creating the script was successfully completed and the script was able to batch export models to IFC files using Python.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\code1.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\ifc.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("My next step was to write some code that could extract the relevant data points from the IFC file and store them in the SQLite database.")
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\code2.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.write("Figure 6 is an example of code that uses the ifcopenshell library to open and read the IFC file, and the sqlite3 library to connect to \
and interact with the SQLite database. The script starts by connecting to the IFC file and the SQLite database. It then iterates through all the \
elements in the IFC file using the by_type method, which is a built-in method of the ifcopenshell library and extracts the element's name and category. \
For each category of element, the script will create a new table in the SQLite database with columns 'id', 'name', 'category' and any relevant data points, \
the table name will be the category name. After that, it uses the execute method of sqlite3 to insert the element's name and category into the appropriate table \
(related to the category of the element). Finally, it commits the changes made to the SQLite database and closes the connection.")
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\SQLit.jpg')
resized_image = image5.resize((1200, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\Model check.jpg')
resized_image = image5.resize((1200, 600))
st.image(resized_image)
st.write("To spot check the Data I returned to the model and extracted the model element Id number and then searched in the database for the same one.")
st.write("Figure 8 above shows the matched element in the model with the stored database element and a check on Gross_Volume and Gross_weight parameter values to see if they matched up.")
st.write("Success !! I have a working Database file representing a 3d Model.")
st.write("Once I had the data in the SQLite database, I had to extract it in a way that would allow me to present it in a simple and accessible format. \
I decided to use a web page with interactive menus, which would allow users to switch between different parameters and view the charts accordingly.  \
In order to accomplish this, I first had to extract the data from the SQLite database and convert it into a format that could be easily used in the web page. \
This involved writing code to connect to the database, retrieve the relevant data, and convert it into a Pandas DataFrame.")

def cleandataframe(df,thresh):
    dfna = df.fillna(np.NaN).reset_index(drop=True)
    return dfna.dropna(axis=1, thresh=thresh)

def getDFbycat(df1,category):
    dfna = df1[df1['I_CATEGORY'] == category]
    dfna = dfna.fillna(np.NaN).reset_index(drop=True)
    return dfna.dropna(axis = 1, thresh = 1000)

def getcountbycat(catDF,param,tol):
    dfall = catDF.groupby(param)['I_CATEGORY'].count().reset_index(name='Count')
    return (dfall[dfall['Count']>tol])

arr = os.listdir('./Databases')

inde = 3
p = './Databases/'+arr[inde]

sqtab = SQLin.importtables((p))
tabs = [pd.DataFrame(item)for item in sqtab]
merged_df = pd.concat(tabs)
merged_df = cleandataframe(merged_df,1000)

strctfrm = getDFbycat(merged_df,'Structural Framing')

structCATcount = getcountbycat(merged_df,'I_CATEGORY',10)

#test = strctfrm.groupby('I_FAMILY AND TYPE')['I_CUT LENGTH'].agg(['count','sum'])

st.markdown("<h3></h3>", unsafe_allow_html=True)

st.title("DataFrame Review")
st.write(merged_df)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Category Metrics")
graph1 = graph_maker.load_graph3(structCATcount,'I_CATEGORY','Count')
graph2 = graph_maker.plotlyBar(structCATcount,'I_CATEGORY','Count')
col1, col2, = st.columns([0.5,0.5])
with col1:
    graph1.update_layout(height=500)
    st.plotly_chart(graph1, use_container_width=True)
with col2:
    graph2.update_layout(height=500)
    st.plotly_chart(graph2, use_container_width=True)

#SQLin.makecsv(merged_df,'merged_df')
