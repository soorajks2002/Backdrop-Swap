import streamlit as st
import rembg
from PIL import Image

st.title("Replace Background")

input_image = st.file_uploader("Upload your image", type=[
                         'png', 'jpg', 'jpeg'], label_visibility='visible')

background_image = st.file_uploader("Upload your background", type=["png", 'jpg', 'jpeg'], label_visibility='visible')

if input_image:
    st.image(input_image)

if background_image:
    st.image(background_image)

if input_image and background_image :
    
    input_image = Image.open(input_image)
    input_image = rembg.remove(input_image)
    
    background_image = Image.open(background_image)
    
    input_image = input_image.resize((background_image.width, background_image.height))
    
    x = (background_image.width - input_image.width)//2
    y = (background_image.height - input_image.height)//2
    
    mask = input_image.convert("L")
    mask = mask.point(lambda p: p > 0 and 255)
    
    background_image.paste(input_image, (x,y), mask)
    
    st.image(background_image)
