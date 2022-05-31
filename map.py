import pandas as pd
import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib

from streamlit.elements import iframe

temp = pathlib.PosixPath


city = pd.DataFrame({
    'awesome cities' : ['kokand'],
    'lat' : [40.53479104108393 ],
    'lon' : [70.92957920783367]
})
st.map(city)