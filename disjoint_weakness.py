from itertools import combinations
from functools import lru_cache
from allPokes import allPokes
from all_type_combinations import allTypeCombinations
from rule import RULE, doubleRule

@lru_cache(len(allTypeCombinations()))
def weakTo(tc):
    for tc in allTypeCombinations():

def main():
    for tc in combinations(allTypeCombinations(), 3):


main()
