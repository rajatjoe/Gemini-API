from dotenv import load_dotenv
import streamlit as st 
import os 
import google.generativeai as genai 

load_dotenv()  # Load environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure Generative AI with the API key

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("GEMINI APP")

# User input and submission button
input = st.text_input("Input:", key="input")
submit = st.button("Ask the Question")

# Display response when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
