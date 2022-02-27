from os import system
system('chcp 936')
from functools import lru_cache
import csv
from jdt import jdtIter
from softmax import softmin
from graphic_terminal import printTable
from all_type_combinations import allTypeCombinations, typeCombinationBestScore, weakTo
from ex_safety_three_team import dbTypeRepr

def main():
    s = []
    for i in jdtIter(range(len(allTypeCombinations()))):
        tci = allTypeCombinations()[i]
        for j in range(i + 1, len(allTypeCombinations())):
            tcj = allTypeCombinations()[j]
            w_tci = weakTo(tci)
            w_tcj = weakTo(tcj)
            if w_tci.isdisjoint(w_tcj):
                for k in range(j + 1, len(allTypeCombinations())):
                    tck = allTypeCombinations()[k]
                    w_tck = weakTo(tck)
                    if (
                        w_tck.isdisjoint(w_tci) and
                        w_tck.isdisjoint(w_tcj)
                    ):
                        s.append([ tci, tcj, tck ])
    with open('result_3team.csv', 'r', encoding='utf-8') as f:
        for line in s:
            overall_score = softmin(
                [typeCombinationBestScore(x)[1] for x in line], 
                coldness = .1, 
            )
            ex_loss = getExchangeLoss(f, line)
            line.append(round(overall_score))
            line.append(ex_loss)

    printTable([
        (x, y, z, sc, format(ex, '.2f')) for (x, y, z, sc, ex) in
        sorted(s, key = lambda x : x[3] / x[4], reverse = True)
    ])

def getExchangeLoss(f, tcs):
    tcs = [*map(dbTypeRepr, tcs)]
    f.seek(0)
    c = csv.reader(f)
    for line in c:
        line = [*map(lambda x : x.strip(), line)]
        if line[:3] == tcs:
            return float(line[-1])
    raise ValueError(tcs)

if __name__ == '__main__':
    main()
