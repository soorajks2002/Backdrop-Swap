import streamlit as st
import rembg
from PIL import Image

favicon = Image.open("favicon.ico")
st.set_page_config(page_title="Replace Image", page_icon=favicon, layout='wide')

st.title("Replace Background")
st.empty()

background_image = None

with st.form("io-form") :
    col1, col2 = st.columns(2)

    with col1 :
        st.markdown("##### Upload Target Image")
        input_image = st.file_uploader("Upload your target image", type=['png', 'jpg', 'jpeg'], label_visibility='hidden')
    with col2 :
        st.markdown("##### Upload Background Image")
        background_image = st.file_uploader("Upload your background", type=["png", 'jpg', 'jpeg'], label_visibility='hidden')

    img_col1, img_col2 = st.columns(2)
    if input_image :
        with img_col1:
            st.subheader("Target Image")
            st.image(input_image)

    if background_image :
        with img_col2:
            st.subheader("Background Image")
            st.image(background_image)
    
    if st.form_submit_button("Replace Background") :
        input_image = Image.open(input_image)
        background_image = Image.open(background_image)
        
        with st.spinner("Processing Image...") :
            input_image = rembg.remove(input_image)
            
            input_image = input_image.resize((background_image.width, background_image.height))
            
            x = (background_image.width - input_image.width)//2
            y = (background_image.height - input_image.height)//2
            
            mask = input_image.convert("L")
            mask = mask.point(lambda p: p > 0 and 255)
            
            background_image.paste(input_image, (x,y), mask)

if background_image :
    c1,_ = st.columns(2)
    with c1 :
        st.subheader("Image with new background")
        st.image(background_image)