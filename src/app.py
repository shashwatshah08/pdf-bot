import openai
import streamlit as st
from key import OPEN_API_KEY

from pdf import PDF
from storage import Storage

# Define function to process uploaded PDF file
# def process_pdf_file(uploaded_file):
#     pdf = PDF(uploaded_file)
#     st.success(f"Uploaded file '{pdf.name}' contains {pdf.num_pages} pages.")
#     pdf_data = uploaded_file.getvalue()
#     return pdf_data

# # Create Streamlit web application
# def main():
#     st.title("PDF Bot")
    
#     # Create file uploader
#     uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
#     # Process uploaded file
#     if uploaded_file is not None:
#         pdf_data = process_pdf_file(uploaded_file)
#         if pdf_data is not None:
#             st.success("PDF file uploaded successfully.")
    
if __name__ == "__main__":
    #main()
    openai.api_key = OPEN_API_KEY
    st.title("PDF Bot")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        pdf = PDF(uploaded_file)
        storage = Storage(pdf.text_segments)
        st.write(storage.df)
        user_input = st.text_input()
        print(user_input)
