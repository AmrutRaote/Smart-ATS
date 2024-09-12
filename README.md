
# 🛠 Smart ATS

## Overview
**Smart ATS** is an AI-powered tool that evaluates a resume against a provided job description using Google Gemini's generative model. It acts like an Applicant Tracking System (ATS) and provides feedback on resume-job description match percentage, missing keywords, and profile summary. The tool is built with **Streamlit** to provide an interactive web interface, where users can upload a PDF of their resume and receive actionable insights on how well it matches a specific job description.

## 📦 Dependencies
To run this code, you will need the following Python packages:

- `streamlit` for creating the web interface
- `PyPDF2` for extracting text from PDFs
- `langchain` for managing prompts
- `google-generativeai` for interacting with the Google Gemini API
- `python-dotenv` for loading environment variables

### Install dependencies
```bash
pip install streamlit google-generativeai PyPDF2 langchain python-dotenv
```

Make sure you have your Google Gemini API key saved in a `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key
```

## 🗂 Code Structure

- **`main.py`**: The main script that runs the Streamlit app, handles file uploads, and processes the inputs.
  
  - **`get_gemini_response(input)`**: This function sends a formatted prompt to the Google Gemini API and returns the response.
  
  - **`input_pdf_text(uploaded_file)`**: This function extracts the text from the uploaded PDF resume using PyPDF2.
  
  - **`prompt_template`**: This prompt structure (via LangChain) asks the Gemini API to evaluate the resume based on a job description and provide concise feedback.

- **`.env`**: This file stores environment variables like the Google Gemini API key. (You need to create this manually.)

---

## ▶️ Output
![image](https://github.com/user-attachments/assets/086920b5-8b1a-44f4-939e-1e1f2caf78f5)

---

😊 Feel free to explore, modify, and enhance this project to suit your needs. If you encounter any issues or have questions, don't hesitate to reach out.
