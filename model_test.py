from src.similarity import Similarity
import pytest
def test_predict():
    model=Similarity() 
    score=model.compute("hello","whatever")
    assert score<1