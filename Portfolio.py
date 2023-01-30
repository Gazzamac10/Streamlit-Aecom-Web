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
            padding-left: 50px
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Add title
st.title("Gary McCarthy Portfolio")
st.header("Data Fellowship Portfolio")
# Add image
image1  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio\\AdobeStock_185294016.jpg')
st.image(image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)
# Add introduction
st.markdown("<h3>Introduction</h3>", unsafe_allow_html=True)
st.write("Welcome to the Data Analysis Level 4 Portfolio. This portfolio showcases the advanced data analysis skills and competencies that I have developed through the course, and demonstrates their potential value in a business context.\
I hope that this portfolio will provide a comprehensive overview of my skills and competencies, and will demonstrate my potential to contribute to the success of Aecom. I am confident that the skills and knowledge\
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
st.markdown("<h3></h3>", unsafe_allow_html=True)
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
resized_image = image4.resize((1000, 500))
st.image(resized_image)
