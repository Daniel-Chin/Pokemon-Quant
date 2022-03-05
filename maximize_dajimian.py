print('Hey, but the tc is not weighted by score.')

from os import system
system('chcp 936')
from itertools import combinations
from all_type_combinations import allTypeCombinations, strongTo

def main():
    given = tuple(input('given = '))
    choose_n = int(input('choose_n = '))
    candidates = input('candidates = ')
    exclude = set(input('exclude = '))
    records = []
    facing = set()
    for tc in allTypeCombinations():
        if not exclude.intersection(tc):
            facing.add(tc)
    for ts in combinations(candidates, choose_n):
        all_ts = ts + given
        s = set()
        for targets in map(strongTo, all_ts):
            s = s.union(targets)
        s.intersection_update(facing)
        records.append(( ts, len(s) / len(facing) ))
    records.sort(key = lambda x : x[1])
    for ts, score in records:
        print(ts, format(score, '.0%'))

main()
