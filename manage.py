import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib
from streamlit_option_menu import option_menu
from apps import home, app, contact

temp = pathlib.PosixPath

with st.sidebar:
            navbar = option_menu("Main Menu", ["Home", "Project",  "Contact"],
                icons=['house', 'code-slash', "person-lines-fill"],
                menu_icon="cast", default_index=1,
                styles={
                    "container": {"padding": "0!important", "background-color": "#0AAAB3"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#C8F3DB"},
                    "nav-link-selected": {"background-color": "green"},
                }
            )

if navbar == "Home":
    home = home.app_func
    home()
if navbar == "Project":
    project = app.app_func
    project()
if navbar == "Contact":
    contact = contact.app_func
    contact()


with st.sidebar:
    st.sidebar.title("About")
    st.title("Farkhod Khojikurbonov")
    st.image("image/farkhod.jpg", width=150)
    st.sidebar.info(
        """
        Github:   \nhttps://github.com/farkhod-developer
        \nTelegram: \nhttps://t.me/Farkhod_Developerr
        \nEmail:   \nhttps://farhodand92@gmail.com
        
        ©️ 2022 Farkhod Khojikurbonov
    """
    )
