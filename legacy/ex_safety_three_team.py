from functools import lru_cache
from itertools import combinations, permutations
from softmax import softmax
from jdt import jdtIter
from rule import DOUBLE, HALF, IMMUNE, NORMAL, RULE
from all_type_combinations import (
    ALL_TYPES, allTypeCombinations, typeCombinationBestScore, 
    weakTo, TypeCombination, 
)

LOSS = {
    DOUBLE : 2, 
    HALF : .5, 
    IMMUNE : 0, 
    NORMAL : 1, 
}

def main():
    records = []
    for team in jdtIter([*
        combinations(allTypeCombinations(), 3)
    ], msg = '3-poke team', UPP = 2**8):
        loss = softmax([
            assess(x, y) for (x, y) in permutations(team, 2)
        ])
        overall_score = softmax([typeCombinationBestScore(x)[1] for x in team], .1)
        records.append(( team, loss , overall_score))

    result = sorted(records, key = lambda x : x[1] / x[2])
    # print()
    # display(result)
    write(result)

@lru_cache()
def allTripleTypes():
    return [*combinations(ALL_TYPES, 3)]

@lru_cache(maxsize=171**2)
def quadRule(offe, defe):
    acc = 1
    for o_t in offe:
        for d_t in defe:
            acc *= LOSS[RULE[o_t][d_t]]
    return acc

@lru_cache(maxsize=171**2)
def assess(retreat, assult):
    assult_weak_to = weakTo(assult)
    losses = []
    for x, y, z in allTripleTypes():
        best_action = []
        best_action_loss = 0
        for t in (x, y, z):
            loss = quadRule(t, retreat)
            if TypeCombination(( t, )) in assult_weak_to:
                loss *= .99     # account for same-type bonus
            if loss == best_action_loss:
                best_action.append(t)
            elif loss > best_action_loss:
                best_action = [ t ]
                best_action_loss = loss
        for t in best_action:
            losses.append((
                quadRule(t, assult), 
                1 / len(best_action), 
            ))
    return softmax(losses)

@lru_cache(maxsize=171)
def dbTypeRepr(tc):
    return ''.join(tc)

def write(result):
    with open('result_3team.csv', 'w', encoding='utf-8') as f:
        for (team, loss, score) in result:
            print(
                *map(dbTypeRepr, team), 
                loss, file=f, sep=', ', 
            )

if __name__ == '__main__':
    main()
