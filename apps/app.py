import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib
from streamlit_option_menu import option_menu
from project import DP_project, project1, project2

temp = pathlib.PosixPath

def app_func():
    navbar = option_menu(None, ["DL Project", "Project 1",  "Project 2"],
    icons=['image-alt', 'file-code', "file-earmark-code"],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
                    "container": {"padding": "0!important", "background-color": "#0AAAB3"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#C8F3DB"},
                    "nav-link-selected": {"background-color": "green"},
                }
            )

    if navbar == "DL Project":
        dpl = DP_project.app_func
        dpl()
    if navbar == "Project 1":
        pro1 = project1.app_func
        pro1()
    if navbar == "Project 2":
        pro2 = project2.app_func
        pro2()
