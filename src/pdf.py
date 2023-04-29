import PyPDF2


def get_text(pdf_reader, num_pages):
    pdf_text = []
    for page_num in range(num_pages):
        page_obj = pdf_reader.pages[page_num]
        extracted_text = page_obj.extract_text()
        pdf_text.append(extracted_text)
    return "".join(pdf_text)


def text_to_segments(text):
    segment_size = 5000
    overlap_size = 100
    segments = []
    start = 0
    end = segment_size
    while start < len(text):
        segment = text[start:end]
        segments.append(segment)
        start = end - overlap_size
        end = start + segment_size
    return segments


class PDF:
    
    def __init__(self, uploaded_file):
        self.reader = PyPDF2.PdfReader(uploaded_file)
        self.num_pages = len(self.reader.pages)
        self.name = uploaded_file.name
        self.text = get_text(self.reader, self.num_pages)
        self.text_segments = text_to_segments(self.text)