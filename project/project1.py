import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

def app_func():
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_b91uuvwz.json")

    st.subheader("We apologize for the inconvenience 🙃")
    st.header("we will try to add more projects soon 🙂")
    st_lottie(
        lottie_hello,
        speed=1.5,
        reverse=False,
        loop=True,
        quality="medium", # medium ; high
        # renderer="None", # canvas
        height=500,
        width=800,
        key=None,
)
