from dotenv import load_dotenv
load_dotenv() #loads all env variables

import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#function to load Gemini pro vision 
model = genai.GenerativeModel('gemini-1.5-flash')


# parameters classification:
# input is for how you want the gemini model to act 
# prompt is what information you want  
def get_gemini_response(input , image , prompt ):
    response = model.generate_content([input , image[0],prompt])
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
    

# initialize our streamlit app 
st.set_page_config(page_title="Multilingual Invoice extractor ")

st.header("Gemini app")
input = st.text_input("Input prompt:" , key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
image = ""

if uploaded_file is not None:
    # as soon as i upload i want to see the image on ui 
    image = Image.open(uploaded_file)
    st.image(image , caption="Uploaded image " , use_column_width = True)
    
submit = st.button("Tell me about the invoice ")
input_prompt = """
You are an expert in understanding invoices . We will upload a image as invoice 
and you will have to answer any questions based on the uploaded invoice image 
"""
    
# if sumbit button is clicked
if submit:
    image_data=input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is ")
    st.write(response)
    

