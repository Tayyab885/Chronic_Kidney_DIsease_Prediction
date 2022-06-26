import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
from PIL import  Image
import os

def app():
    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 = st.columns(2)
    col1.image(display, width = 300)
    col2.title("Chronic Kidney Disease")

    if 'clean_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        df_analysis = pd.read_csv('data/clean_data.csv')
        categorical = ['<Select>','Red Blood Cells','Pus Cells','Pus Cell Clumps','Bacteria',
                        'Hypertension','Diabetes Mellitus','Coronary Artery Disease',
                        'Appetite','Pedal Edema','Anemia',"HeatMap"]
        
        category = st.selectbox("Select a Category:", categorical )
        values = ['Red Blood Cells','Pus Cells','Pus Cell Clumps','Bacteria',
                  'Hypertension','Diabetes Mellitus','Coronary Artery Disease',
                  'Appetite','Pedal Edema','Anemia']
        if category in values:
            style.use('seaborn-darkgrid')
            
            # BarCart
            st.header("Bar Chart:")
            fig = plt.figure(figsize=(10, 5))
            g = df_analysis[category].value_counts().plot.bar(colormap="tab20c")
            g.set_ylabel(category,fontsize = 15)
            st.pyplot(fig)

            # Pie Chart
            st.header("Pie Chart:")
            style.use('seaborn-darkgrid')
            fig = plt.figure(figsize=(10, 4))
            g = df_analysis[category].value_counts().plot.pie(autopct='%1.1f%%',
                colormap="tab20c",fontsize=8,shadow=False,explode=[0.1,0])
            st.pyplot(fig)
        
        elif category == "HeatMap":
            st.header("HeatMap:")
            df = df_analysis.iloc[:,:-1]
            corr = df.corr()
            fig = plt.figure(figsize=(20, 15))
            sns.heatmap(corr,cmap=sns.diverging_palette(280, 280, s=100, l=35, as_cmap=True,sep=60),
                        square=True,annot=True,annot_kws={'fontsize':7},fmt='.2%',cbar=False)
            st.pyplot(fig)
        else:
            st.warning("Please Select a Category.")

        













        

    hide_menu = '''
    <style>
    footer{
        visibility:hidden;
    }
    </style>'''

    st.markdown(hide_menu,unsafe_allow_html=True)