import streamlit as st
class MultiPage: 
    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )

    def run(self):
        page = st.sidebar.selectbox(
            'App Menu', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        page['function']()
    
    hide_menu = '''
    <style>
    footer{
        visibility:hidden;
    }
    </style>'''

    st.markdown(hide_menu,unsafe_allow_html=True)