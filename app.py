import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib

temp = pathlib.PosixPath

# title
st.title("Carnivores, Fruits, Transports Classification Model")
st.subheader("You can upload the following images: ")
st.text("Transportts: Car Boat Airplane Rocket Helicopter \nCarnivores: Raccoon Otter Dog Lion Tiger Red_panda Lynx Jaguar Bear Fox Cat \nFruits: Apple Grape Common_fig Pear Strawberry Tomato Lemon Banana Orange Peach \n          Mango Pineapple Grapefruit Pomegranate Watermelon Cantaloupe")

# rasm yuklash
file_img = st.file_uploader("Image upload", type=['png', 'jpg', 'jpeg', 'gif', 'svg'])
if file_img:
    st.image(file_img)
    # PIL convert
    img = PILImage.create(file_img)
    # model
    model = load_learner('AI_Image_Model.pkl')
    # predict
    pred, pred_id, probs=model.predict(img)
    st.success(f"Predict: {pred}")
    st.info(f"Probability: {probs[pred_id]*100:.1f}%")
    # plotting
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)