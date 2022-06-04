import pandas as pd
import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib

from streamlit.elements import iframe

temp = pathlib.PosixPath

def app_func():
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')

    st.subheader("My place of residence")
    city = pd.DataFrame({
        'awesome cities' : ['kokand'],
        'lat' : [40.53479104108393 ],
        'lon' : [70.92957920783367]
    })
    st.map(city)