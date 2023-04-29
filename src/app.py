import openai
import streamlit as st
from key import OPEN_API_KEY

from pdf import PDF
from storage import Storage


@st.cache_data(show_spinner=False)
def process_file(uploaded_file):
    with st.spinner('PDF loading..'):
        if uploaded_file is not None:
            if uploaded_file.getvalue():
                pdf = PDF(uploaded_file)
                storage = Storage(pdf.text_segments)
                st.success('PDF uploaded successfully!')
            else:
                st.error("PDF is empty!")
                return (None, False)
        else:
            return (None, False)
    return (storage, True)

@st.cache_data(show_spinner=False)
def process_user_input(user_input, _storage):
    if user_input:
            with st.spinner('Preaparing answer...'):
                if storage:
                    similar_text = _storage.get_query_context(user_input)
                    
                    gpt_query = '''
                        Provide a concise and easy-to-understand answer to the question based 
                        on the information given in a provided text. If the text does not contain the 
                        information say "Sorry, I do not know".
                        
                        Question: {}
                        
                        Text: {}
                    '''.format(user_input, similar_text)
                    
                    resp = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": gpt_query},
                        ],
                        temperature = 0.2
                    )
                    return resp["choices"][0]["message"]["content"]
                else:
                    return None
    return None
    
if __name__ == "__main__":
    openai.api_key = OPEN_API_KEY
    
    st.title("PDF Bot")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    storage, should_get_user_input = process_file(uploaded_file)
    
    
    if should_get_user_input:
        user_input = st.text_input(label="Enter you query!")
        output = process_user_input(user_input, storage)
        if output:
            st.write(output)
