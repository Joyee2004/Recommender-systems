import pandas as pd
from surprise import Dataset
from surprise import Reader

def load_data():

    movie_data = Dataset.load_builtin('ml-100k')
    raw_ratings = movie_data.raw_ratings[:5]
    print("Sample raw ratings:")
    for r in raw_ratings:
        print(r)
    return movie_data
