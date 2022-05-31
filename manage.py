import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib
from streamlit_option_menu import option_menu
temp = pathlib.PosixPath

with st.sidebar:
    # selected = option_menu("Main Menu", ["Home", 'Project', 'About'],
    #     icons=['house', 'gear'], menu_icon="cast", default_index=1)
    # selected

# 3. CSS style definitions
    selected3 = option_menu("Main Menu", ["Home", "Upload",  "Tasks", 'Settings'],
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=1,
        styles={
            "container": {"padding": "0!important", "background-color": "#0AAAB3"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#C8F3DB"},
            "nav-link-selected": {"background-color": "green"},
        }
    )