from sentence_transformers import SentenceTransformer, util
class Similarity:
    def __init__(self)->None:
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    def compute(self,sentence1:str,sentence2:str) -> float:
       embedding1 = self.model.encode(sentence1, convert_to_tensor=True)
       embedding2 = self.model.encode(sentence2, convert_to_tensor=True)
       
       return util.cos_sim(embedding1, embedding2)
    