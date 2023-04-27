import textwrap
import PyPDF2


def get_text(pdf_reader, num_pages):
    pdf_text = []
    for page_num in range(num_pages):
        page_obj = pdf_reader.pages[page_num]
        extracted_text = page_obj.extract_text()
        pdf_text.append(extracted_text)
    return "".join(pdf_text)

def get_text_chunks(text):
    chunk_size = 2000
    overlap_size = 100
    chunks = textwrap.wrap(text, width=chunk_size, step=chunk_size-overlap_size)
    chunk_arr = []
    for chunk in chunks:
        chunk_arr.append(chunk)
    return chunk_arr



class PDF:
    
    def __init__(self, uploaded_file):
        self.reader = PyPDF2.PdfReader(uploaded_file)
        self.num_pages = len(self.reader.pages)
        self.name = uploaded_file.name
        self.text = get_text(self.reader, self.num_pages)
        self.chunk_arr = get_text_chunks(self.text)