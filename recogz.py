from PIL import Image
import pytesseract
import streamlit as st
import time

st.title("recogz")
st.subheader("text scanner tool")


img=st.file_uploader("Upload your image here",type=["jpeg","jpg","png"])

if img:
    img1=Image.open(img)
    st.success("Image uploaded successfully")

    st.write("Your Image")
    st.image(img,width=270)


    st.subheader("Your Uploaded image text is")
    

    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    txt=pytesseract.image_to_string(img1)


    st.code(txt,language=None)






