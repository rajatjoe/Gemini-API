# Health management app 

from dotenv import load_dotenv
import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image

load_dotenv()  # Load environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure Generative AI with the API key



# Function to load gemini pro Vision api and get response 

def get_gemini_response(input, image, prompt):
    # Function to load Gemini Pro model and get responses
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input ,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # read the files into bytes
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data": bytes_data
            }
        ]
        
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    
    
st.set_page_config(page_title="Gemini Health App ")

st.header("Gemini Health app")
input = st.text_input("Input prompt:" , key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
image = ""

if uploaded_file is not None:
    # as soon as i upload i want to see the image on ui 
    image = Image.open(uploaded_file)
    st.image(image , caption="Uploaded image " , use_column_width = True)
    
submit = st.button("Tell me the total calories ")
input_prompt = """
you are an expert in nutritionist where you need to see the food items from the image 
and calculate the total calories , also provide the details of every food items with calories intake 
is below format 
1. Item 1 : no. of calories 
2. Item 2 : no. of calories
-----
-----
"""
    
# if sumbit button is clicked
if submit:
    image_data=input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is ")
    st.write(response)