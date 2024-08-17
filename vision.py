from dotenv import load_dotenv
import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image

load_dotenv()  # Load environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure Generative AI with the API key

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_resposne(uinput , image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
        
    return response.text

st.set_page_config(page_title="Gemini image demo ")
st.header("gemini application")
input = st.text_input("Input prompt :" , key="input")

uploaded_file = st.file_uploader("Choose an image ..." , type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None : 
    image = Image.open(uploaded_file)
    st.image(image , caption="Uploaded image " , use_column_width=True)
    
submit = st.button("Tell me about the image")

#if submit button is clicked 
if submit:
    response = get_gemini_resposne(input,image)
    st.subheader("The response is ")
    st.write(response)
