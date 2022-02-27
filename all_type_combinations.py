THRESHOLD = 233

from functools import lru_cache
from allPokes import allPokes

@lru_cache()
def allTypeCombinations():
    all_p = allPokes()
    s = set()
    for poke in all_p.values():
        if int(poke['综合分']) >= THRESHOLD:
            s.add(poke['type'])
    return s

if __name__ == '__main__':
    print(len(allTypeCombinations()))
