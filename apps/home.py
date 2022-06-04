import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

def app_func():
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_coding = load_lottiefile("lottiefiles/coding.json")  # replace link to local lottie file
    lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_FYx0Ph.json")


    st.subheader("Hi 👋, my name is Farhod")
    st.header("I am a future Data Science and AI engineer")
    st_lottie(
        lottie_hello,
        speed=1.5,
        reverse=False,
        loop=True,
        quality="medium", # medium ; high
        # renderer="None", # canvas
        height=420,
        width=800,
        key=None,
)

    # st_lottie(lottie_coding, key="coding")

    st.header("I am currently a student of Data Science and AI practicum of mohirdev.uz platform")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        key=None,
        height=500,
        width=1000,
    )