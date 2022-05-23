import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib

temp = pathlib.PosixPath

# title
st.title("Transportni klassifikatsiya qiluvchi model")
# rasm yuklash
file_img = st.file_uploader("Rasm yuklash", type=['png', 'jpg', 'jpeg', 'gif', 'svg'])
if file_img:
    st.image(file_img)
    # PIL convert
    img = PILImage.create(file_img)
    # model
    model = load_learner('trans_model.pkl')
    # predict
    pred, pred_id, probs=model.predict(img)
    st.success(f"Bashorat: {pred}")
    st.info(f"Ehtimollik: {probs[pred_id]*100:.1f}%")
    # plotting
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)