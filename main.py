import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Define the prompt template using LangChain
prompt_template = PromptTemplate(
    input_variables=["text", "jd"],
    template="""
    Hey Act Like a skilled or very experienced ATS (Applicant Tracking System)
    with a deep understanding of tech field, software engineering, data science, data analyst,
    and big data engineering. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive, and you should provide 
    the best assistance for improving the resumes. Assign the percentage matching based 
    on the JD and the missing keywords with high accuracy.
    the profile summary must include the candidates name.
    
    Resume: {text}
    Description: {jd}
    
    I want the response in 3 lines having the structure:
    OUTPUT:\n
    JD Match: %\n
    Missing Keywords: []\n
    Profile Summary: ""
    """
)

# Streamlit app
st.title("Smart ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        resume_text = input_pdf_text(uploaded_file)

        # Format the prompt using LangChain's PromptTemplate
        formatted_prompt = prompt_template.format(text=resume_text, jd=jd)

        # Send the formatted prompt to Gemini for a response
        response = get_gemini_response(formatted_prompt)

        # Display the response in the Streamlit app
        st.subheader(response)
    else:
        st.write("Please upload a resume!")
