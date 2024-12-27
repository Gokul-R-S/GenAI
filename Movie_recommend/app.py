import streamlit as st 
from langchain import PromptTemplate,LLMChain
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import warnings 
warnings.filterwarnings('ignore')


# setup up the API
genai.configure(api_key=os.getenv('google_api_key'))

# designing the page
st.title('Movie Recommendation System using Gemini-Pro')
user_input=st.text_input('Enter the Movie title , Genre or Keywords (eg: sci-fi, horror, thriller..etc)')

# Prompt Template
template=PromptTemplate(input_variables=['user_input'],
                        template="""You are a movie recommendation assistant. 
    Based on the input preferences "{user_input}", suggest 5 movies, ensuring they are popular, relevant, 
    and from a mix of old and recent releases. Provide a short description for each movie.""")

# Initialise the model
llm=ChatGoogleGenerativeAI(model='gemini-pro')

if user_input:
    prompt=template.format(user_input=user_input)
    recommendations=llm.predict(text=prompt)
    st.write(f'Recommendations based on your preferences are :\n{recommendations}')
else:
    st.write('Please enter your preferences')   

















































