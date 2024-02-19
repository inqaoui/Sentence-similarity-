from sentence_transformers import SentenceTransformer, util
from fastapi import FastAPI
from .input.sentences import Sentences
from .similarity import Similarity
import time

model=Similarity()    
app = FastAPI ()

@app.get("/")
def home () :
    return {"Hello world"}

@app.post("/similarity")
def similarity(sentences:Sentences):
    start=time.time()
    score=model.compute(sentences.sentence1,sentences.sentence2).item()
    compute_time=time.time()-start
    return{"compute_time":compute_time,"score":score}

 