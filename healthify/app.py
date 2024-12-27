import streamlit as st 
from dotenv import load_dotenv
load_dotenv() # acitvate the local variables
import google.generativeai as genai
import os
import pandas as pd

# configuring the api_key
api=genai.configure(api_key=os.getenv('google_api_key'))

#streamlit page
st.header("👨‍⚕️ Healthcare :blue[Advisor] ⚕️",divider='green')
input=st.text_input(''' Hey! I am your healthcare advisor 💊. Ask me about health, diseases, or fitness''' )
submit=st.button("Get Advice") 

#BMI calulator
st.sidebar.subheader('BMI Calculator 📏')
weight=st.sidebar.text_input('Weight (in kgs)')
height=st.sidebar.text_input('Height (in cms)')
weight=pd.to_numeric(weight)
height=pd.to_numeric(height)
height_mts=height/100
bmi=weight/(height_mts**2)

# Scale of the BMI
notes = f'''The BMI value can be interpreted as:
* Underweight: BMI<18.5
* Normal Weight: BMI 18.5 – 24.9
* Overweight: BMI 25 – 29.9
* Obese: BMI > 30'''

if bmi:
    st.sidebar.markdown(" The BMI is: ")
    st.sidebar.write(f"Your BMI: {bmi:.1f}")
    st.sidebar.write(notes)

# GenAI application

def get_response(text):
    model=genai.GenerativeModel('gemini-pro')
    prompt = '''I want you to act as a healthcare advisor with expertise in diet and wellness. Please follow these guidelines:
                ALLOWED TOPICS:
                - General health information
                - Diet and nutrition advice
                - Fitness and exercise guidance
                - Disease prevention and awareness
                - Wellness tips and lifestyle recommendations
                RESPONSES:
                - For non-health topics: "I'm a healthcare advisor and can only provide guidance on health, nutrition, and fitness topics."
                - For medication requests: "For medication advice, please consult your healthcare provider directly."
                Please address the following health-related question:'''
    if text:
        response= model.generate_content(prompt+text)
        return response.text    
    else:
        st.write('Please Enter the Prompt !!!')
        
if submit:
    response=get_response(input)
    st.subheader('The :orange[Response] is :')
    st.write(response)
    
#Disclaimer
st.caption("""
⚠️ Disclaimer: This is an AI advisor, not medical advice. 
Please consult a healthcare professional for medical decisions.
""")






























