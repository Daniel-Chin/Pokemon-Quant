# lian fang, but only two pokes. 

from os import system
system('chcp 936')
import pickle
from softmax import softmin
from graphic_terminal import printTable
from allPokes import allPokesTotalScore
from all_type_combinations import allTypeCombinations, TcsDoubleTo
from jdt import jdtIter

def sumScores(tc_set):
    acc = 0
    for tc in tc_set:
        acc += tc.total_score
    return acc

def main():
    with open('ex_safety_2.pickle', 'rb') as f:
        ex_safety = pickle.load(f)
    s = []
    n_all_tc = len(allTypeCombinations())
    for a_i in jdtIter(range(n_all_tc), UPP = 4):
        a = allTypeCombinations()[a_i]
        if a.hasQuadWeakness():
            continue
        for b_i in range(a_i + 1, n_all_tc):
            b = allTypeCombinations()[b_i]
            if b.hasQuadWeakness():
                continue
            loss = 0
            a_w = TcsDoubleTo(a)
            b_w = TcsDoubleTo(b)
            ab_w = a_w.intersection(b_w)
            loss += sumScores(ab_w)
            # loss /= allPokesTotalScore()
            score = softmin((
                a.high_score,
                b.high_score,
            ), coldness = .1)
            team = tuple(sorted((a, b)))
            s.append((
                *team, 
                loss, 
                score, 
                ex_safety[team], 
            ))
    s.sort(
        reverse = True, 
        key = lambda x : (x[3] - x[2] * .5) / x[4], 
    )
    printTable(
        s[:80], 
        header=[
            '宝可梦 1', '宝可梦 2', 
            '防盲', '综分', '替换', 
        ], 
        formatter=[
            None, 
            None, 
            # lambda x : format(x, '02.2%'), 
            round, 
            round, 
            lambda x : format(x, '4.0%'), 
        ], 
        delimiter = ' ', padding = 0, 
    )
    # for team, loss, common_w in s[:20]:
    #     buffer = [*team, round(loss)]
    #     if common_w:
    #         buffer.append('团灭 from')
    #         buffer.append(common_w)
    #     print(*buffer)
    #     print()

main()
