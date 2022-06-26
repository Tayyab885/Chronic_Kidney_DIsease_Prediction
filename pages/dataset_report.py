import numpy as np
import pandas as pd
import streamlit as st
from PIL import  Image
from pandas_profiling import ProfileReport, profile_report
from streamlit_pandas_profiling import st_profile_report

def app():
    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 = st.columns(2)
    col1.image(display, width = 300)
    col2.title("Chronic Kidney Disease")
    #Page Title
    st.markdown('##')
    st.header('Generate The Report Of The Dataset:')

    # Now Upload Dataset
    with st.header("Upload your dataset (.csv)"):
        upload_file_data = st.file_uploader("Upload the Dataset File:",type = ['csv'],key="report")


    # Getting insights of Dataset
    if upload_file_data is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(upload_file_data)
            return csv
        data = load_csv()
        report = ProfileReport(data,explorative = True)
        st.header("**Dataset**")
        st.write(data)
        if st.button("Generate Report"):
            st.write("---")
            st.header("**Dataset Report:**")
            st_profile_report(report)
            export = report.to_html()
            st.download_button(label = "Download Report" , data = export, file_name = "Profile_Report.html")
    else:
        st.info('File is not Uploaded Yet!')



    hide_menu = '''
    <style>
    footer{
        visibility:hidden;
    }
    </style>'''

    st.markdown(hide_menu,unsafe_allow_html=True)


