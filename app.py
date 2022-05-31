import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib

temp = pathlib.PosixPath

# title
st.latex('''** Carnivores, Fruits, Transports, Classification Model **''')
st.subheader("You can upload the following images: ")
st.text("TRANSPORTS: Car Boat Airplane Rocket Helicopter \n\nCARNIVORES: Raccoon Otter Dog Lion Tiger Red_panda Lynx Jaguar Bear Fox Cat \n\nFRUITS: Apple Grape Common_fig Pear Strawberry Tomato Lemon Banana Orange Peach \n        Mango Pineapple Grapefruit Pomegranate Watermelon Cantaloupe")

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
    fig = px.bar(x=probs*100, y=model.dls.vocab, width=200, height=200)
    st.plotly_chart(fig)