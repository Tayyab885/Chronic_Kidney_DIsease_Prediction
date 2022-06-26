import streamlit as st
import numpy as np
from PIL import Image
import webbrowser
from streamlit_option_menu import option_menu


def app():
    #Row 1
    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 = st.columns(2)
    col1.image(display)
    col2.title("Chronic Kidney Disease")

    #Row 2    
    a1,a2 = st.columns(2)
    a1.title('Welcome!')
    a1.markdown('''Welcome to our Final Year Project(FYP).Our Project is to Predict the Chronic Kidney Disease(CKD) Using Data Science or Machine Learning.In this project we will implement different Data Science techinques to build a model to give insight of the dataset and predict the Chronic Kidney Disease.''')
    a2.markdown('##')
    img = Image.open('main.png')
    img = np.array(img)
    a2.image(img)

    #Row3
    x1,x2 = st.columns(2)
    x1.markdown('<p class="big-font">About this Site:</p>', unsafe_allow_html=True)
    x1.markdown('''This is a more of story telling app. The user can not only Predict the disease but also can perform some other actions.''')
    x1.markdown(
        """
        1. Genrate the report about dataset.
        2. Clean the dataser.
        3. Check Accuracy by training Multiple Algorithms.
        4. Predict the CKD. 
        5. Analyse/Visualize the Data .
        """
               )
    #Row4
    b1,b2 = st.columns(2)
    # b1.markdown("""
    # ****""")

    b1.markdown('<p class="big-font">What is Chronic Kidney Disease(CKD)?</p>', unsafe_allow_html=True)
    b2.markdown('''\n\n
    Chronic kidney disease (CKD) means your kidneys are damaged and can’t filter blood the way they should. The disease is called “chronic” because the damage to your kidneys happens slowly over a long period of time. This damage can cause wastes to build up in your body. CKD can also cause other health problems.

   ''')
    url = "https://www.niddk.nih.gov/health-information/kidney-disease/chronic-kidney-disease-ckd/what-is-chronic-kidney-disease"
    if b1.button("Learn More"):
        webbrowser.open_new_tab(url)



    

# Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:30px  !important;
        font-weight: bold; 
    }
    </style>
    """, unsafe_allow_html=True)




    hide_menu = '''
    <style>
    footer{
        visibility:hidden;
    }
    </style>'''

    st.markdown(hide_menu,unsafe_allow_html=True)