import streamlit as st
import PyPDF2

# Define function to process uploaded PDF file
def process_pdf_file(uploaded_file):
    
    # Read PDF file
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    num_pages = len(pdf_reader.pages)
    st.success(f"Uploaded file '{uploaded_file.name}' contains {num_pages} pages.")
    
    # Save PDF file to variable
    pdf_data = uploaded_file.getvalue()
    
    return pdf_data

# Create Streamlit web application
def main():
    st.title("PDF Bot")
    
    # Create file uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    # Process uploaded file
    if uploaded_file is not None:
        pdf_data = process_pdf_file(uploaded_file)
        if pdf_data is not None:
            st.success("PDF file uploaded successfully.")
    
if __name__ == "__main__":
    main()
