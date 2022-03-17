'''
onyl 2 pokes. 
Assume:
    I only exchange when 对边本系克我
    -> 对面一定出克我招，没有其他情况。
'''

from os import system
system('chcp 936')
from functools import lru_cache
from itertools import combinations, permutations
import pickle
from softmax import softmax
from jdt import jdtIter
from rule import DOUBLE, HALF, IMMUNE, NORMAL, doubleRule
from all_type_combinations import (
    allTypeCombinations, 
    TypesDoubleTo, 
)

LOSS = {
    DOUBLE : 2, 
    HALF : .5, 
    IMMUNE : 0, 
    NORMAL : 1, 
}

def main():
    result = {}
    for team in jdtIter([*
        combinations(allTypeCombinations(), 2)
    ], msg = '2-poke team', UPP = 2**7):
        loss = softmax([
            assess(x, y) for (x, y) in permutations(team, 2)
        ])
        result[tuple(sorted(team))] = loss

    with open('ex_safety_2.pickle', 'wb') as f:
        pickle.dump(result, f)

@lru_cache(maxsize=171**2)
def assess(retreat, assult):
    return softmax([
        doubleRule(t, assult) for t in TypesDoubleTo(retreat)
    ])

@lru_cache(maxsize=171)
def dbTypeRepr(tc):
    return ''.join(tc)

if __name__ == '__main__':
    main()
