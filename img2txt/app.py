import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
from PIL import Image
import pathlib
import textwrap

#configuration of api
genai.configure(api_key=os.getenv('google_api_key'))

#streamlit page
st.header('📸 Gemini IMG2TXT 📄',divider = 'green')
input=''
input=st.text_input('📝 Input prompt: ', key='input')
uploaded_img=st.file_uploader('📤 Please upload your image....', type=['jpg', 'jpeg', 'png'])

image=None
if uploaded_img:
    image=Image.open(uploaded_img)
    st.image(image,caption='Image uploaded',use_container_width =True)
    
def get_gemini_response(input,image):
    model=genai.GenerativeModel('gemini-1.5-flash') # flash is used to process images
    if image:
        response=model.generate_content([input,image])
    else:
        response=model.generate_content([input])
    return response.text

submit=st.button('Submit')

if submit:
    response=get_gemini_response(input,image)
    st.subheader(' The :blue[Response] is')
    st.write(response)
