
from  similarity import model
m=model.Similarity()
a=m.compute("The cat sits outside","A man is playing guitar")
print(float(a.item()))