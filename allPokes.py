from functools import lru_cache
import pickle

@lru_cache()
def allPokes():
    with open('all_pokes.pickle', 'rb') as f:
        return pickle.load(f)
