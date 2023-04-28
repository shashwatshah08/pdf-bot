import openai
import pandas as pd

from openai.embeddings_utils import get_embedding, cosine_similarity

# def get_embedding(text, model="text-embedding-ada-002"):
#    text = text.replace("\n", " ")
#    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

class Storage:
    
    def __init__(self, text_segments):
        embeddings = []
        for text in text_segments:
            embedding = get_embedding(text, model='text-embedding-ada-002')
            embeddings.append(embedding)
        self.df = pd.DataFrame({'text': text_segments, 'embeddings': embeddings})
        
    def get_query_context(self,  query):
        query_embedding = get_embedding(query, model='text-embedding-ada-002')
        self.df['similarities'] = self.df.embeddings.apply(lambda x: cosine_similarity(x, query_embedding))
        res = self.df.sort_values('similarities', ascending=False).head(2)
        res_list = res['text'].tolist()
        return "".join(res_list)
        