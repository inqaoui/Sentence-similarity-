from Similarity import model
from fastapi import FastAPI

m=model.Similarity()
a=m.compute("The cat sits outside","A man is playing guitar")
# print(float(a.item()))
app = FastAPI ()
@app . route ("/")
def home () :
    return {"Hello world"}