import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import home, clean_dataset, machine_learning, data_visualize,dataset_report,prediction


# Create an instance of the app 
app = MultiPage()


# Add all your application here
app.add_page("Home", home.app)
app.add_page("Generate Report",dataset_report.app)
app.add_page("Clean Dataset",clean_dataset.app)
app.add_page("Machine Learning", machine_learning.app)
app.add_page("CKD Prediction",prediction.app)
app.add_page("Data Analysis",data_visualize.app)


# The main app
app.run()
