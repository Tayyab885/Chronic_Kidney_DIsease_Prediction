import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import pickle


def app():
    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 = st.columns(2)
    col1.image(display,width = 300)
    col2.title("Chronic Kidney Disease")

    st.header("Predict the Chronic Kidney Disease(CKD):")
    # Inputs
    diabetes_mellitus = st.text_input("Diabetes Mellitus:",placeholder = "Yes = 1 & No = 0")
    specific_gravity = st.text_input("Specific Gravity:",placeholder = "Ex: (1.005,1.010,1.015,1.020,1.025)")
    hypertension = st.text_input("Hypertension:",placeholder = "Yes = 1 , No = 0")
    hemoglobin = st.text_input("Hemoglobin (gms):",placeholder = "In gms")
    albumin = st.text_input("Albumin:",placeholder = "(0,1,2,3,4,5)")
    packed_cell_volume = st.text_input("Packed Cell Volume:",placeholder = "(1,....,60)")
    appetite = st.text_input("Appetite:",placeholder = "Good = 1 , Poor = 0")
    red_blood_cells = st.text_input("Red Blood Cells (millions/cmm):",placeholder="In Millions/cmm")
    
    if st.button("CKD Prediction"):
        try: 
            model = pickle.load(open("ckd_model.pkl","rb"))
            input_values = np.array([[diabetes_mellitus,specific_gravity,hypertension,hemoglobin,
                albumin,packed_cell_volume,appetite,red_blood_cells ]])

            result = model.predict(input_values)

            if result == 1:
                st.write("### **You have Chronic Kidney Disease.**")
            else:
                st.write("### **You Don't have Chronic Kidney Disease.**")
        except ValueError:
            st.warning("Please fill the values correctly.")
    
    



    
    
    hide_menu = '''
    <style>
    footer{
        visibility:hidden;
    }
    </style>'''

    st.markdown(hide_menu,unsafe_allow_html=True)