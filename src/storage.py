import openai
import pandas as pd


def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

class Storage:
    
    def __init__(self, text_segments):
        embeddings = []
        for text in text_segments:
            embedding = get_embedding(text, model='text-embedding-ada-002')
            embeddings.append(embedding)
        self.df = pd.DataFrame({'text': text_segments, 'embeddings': embeddings})
        